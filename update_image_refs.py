import os
import re

def update_image_references(content_dir):
    """
    更新 Markdown 文件中的图片引用，将 .jpg/.jpeg/.png 替换为 .webp
    
    参数:
        content_dir: 内容目录路径
    """
    # 图片引用的正则表达式
    image_pattern = r'!\[([^\]]*)\]\(([^)]+\.(jpg|jpeg|png))\)'
    
    # 遍历所有 Markdown 文件
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 查找所有图片引用
                matches = re.finditer(image_pattern, content)
                modified = False
                
                # 替换图片引用
                for match in matches:
                    alt_text = match.group(1)
                    image_path = match.group(2)
                    ext = match.group(3)
                    
                    # 构建新的图片路径
                    new_image_path = image_path.replace(ext, 'webp')
                    
                    # 检查新的图片文件是否存在
                    absolute_new_path = os.path.join(os.path.dirname(file_path), '..', '..', 'static', new_image_path.lstrip('/'))
                    if os.path.exists(absolute_new_path):
                        # 替换图片引用
                        old_ref = f'![{alt_text}]({image_path})'
                        new_ref = f'![{alt_text}]({new_image_path})'
                        content = content.replace(old_ref, new_ref)
                        modified = True
                        print(f'在 {file} 中更新图片引用: {image_path} -> {new_image_path}')
                
                # 如果文件被修改，保存更新
                if modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)

if __name__ == '__main__':
    content_dir = 'content/posts'  # Markdown 文件目录
    update_image_references(content_dir)
    print('所有图片引用更新完成！') 