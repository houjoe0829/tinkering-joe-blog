import os
import re

def update_image_references(content_dir):
    """
    更新 Markdown 文件中的图片引用，将 .jpg/.jpeg/.png 替换为 .webp
    
    参数:
        content_dir: 内容目录路径
    """
    # 图片引用的正则表达式（更宽松的匹配，包含特殊字符）
    image_pattern = r'!\[([^\]]*)\]\(([^)]*\.(jpg|jpeg|png|JPG|JPEG|PNG))\)'
    
    # 遍历所有 Markdown 文件
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
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
                    
                    # 构建新的图片路径（替换扩展名为 webp）
                    new_image_path = re.sub(r'\.(jpg|jpeg|png)$', '.webp', image_path, flags=re.IGNORECASE)
                    
                    # 检查新的图片文件是否存在
                    if image_path.startswith('/'):
                        # 绝对路径，从 static 开始
                        absolute_new_path = os.path.join('static', new_image_path.lstrip('/'))
                    else:
                        # 相对路径
                        absolute_new_path = os.path.join(os.path.dirname(file_path), new_image_path)
                    
                    if os.path.exists(absolute_new_path):
                        # 替换图片引用
                        old_ref = f'![{alt_text}]({image_path})'
                        new_ref = f'![{alt_text}]({new_image_path})'
                        content = content.replace(old_ref, new_ref)
                        modified = True
                        print(f'在 {file} 中更新图片引用: {os.path.basename(image_path)} -> {os.path.basename(new_image_path)}')
                    else:
                        print(f'警告：WebP 文件不存在: {absolute_new_path}')
                
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