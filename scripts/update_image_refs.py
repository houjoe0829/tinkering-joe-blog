import os
import re

def update_image_references(content_dir):
    """
    更新 Markdown 文件中的图片引用：
    1. 将相对路径转换为绝对路径 (filename.png -> /images/posts/article-name/filename.webp)
    2. 将 .jpg/.jpeg/.png 扩展名替换为 .webp

    参数:
        content_dir: 内容目录路径 (如 content/posts 或 content/thoughts)
    """
    # 图片引用的正则表达式（匹配 Markdown 图片语法）
    image_pattern = r'!\[([^\]]*)\]\(([^)]*\.(jpg|jpeg|png|JPG|JPEG|PNG))\)'

    # 从 content_dir 提取内容类型 (posts 或 thoughts)
    content_type = os.path.basename(content_dir)

    # 遍历所有 Markdown 文件
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                article_name = file.replace('.md', '')

                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 查找所有图片引用
                matches = list(re.finditer(image_pattern, content))
                modified = False

                # 从后往前替换，避免位置偏移问题
                for match in reversed(matches):
                    alt_text = match.group(1)
                    image_path = match.group(2)
                    ext = match.group(3).lower()

                    # 获取图片文件名（去掉路径部分）
                    image_filename = os.path.basename(image_path)
                    # 替换扩展名为 webp
                    webp_filename = re.sub(r'\.(jpg|jpeg|png)$', '.webp', image_filename, flags=re.IGNORECASE)

                    # 判断是相对路径还是绝对路径
                    if image_path.startswith('/'):
                        # 已经是绝对路径，只需替换扩展名
                        new_image_path = re.sub(r'\.(jpg|jpeg|png)$', '.webp', image_path, flags=re.IGNORECASE)
                        absolute_webp_path = os.path.join('static', new_image_path.lstrip('/'))
                    else:
                        # 相对路径：转换为标准绝对路径格式
                        new_image_path = f'/images/{content_type}/{article_name}/{webp_filename}'
                        absolute_webp_path = f'static/images/{content_type}/{article_name}/{webp_filename}'

                    # 检查 WebP 文件是否存在
                    if os.path.exists(absolute_webp_path):
                        # 替换图片引用
                        old_ref = f'![{alt_text}]({image_path})'
                        new_ref = f'![{alt_text}]({new_image_path})'
                        content = content.replace(old_ref, new_ref)
                        modified = True
                        print(f'在 {file} 中更新: {image_path} -> {new_image_path}')
                    else:
                        print(f'警告：WebP 文件不存在: {absolute_webp_path}')

                # 如果文件被修改，保存更新
                if modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)

if __name__ == '__main__':
    # 更新 posts 和 thoughts 目录
    for content_type in ['posts', 'thoughts']:
        content_dir = f'content/{content_type}'
        if os.path.exists(content_dir):
            print(f'正在更新 {content_type} 目录...')
            update_image_references(content_dir)

    print('所有图片引用更新完成！') 