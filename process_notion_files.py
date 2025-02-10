import os
import shutil
import re
from pathlib import Path
from datetime import datetime
import yaml

def sanitize_filename(filename):
    """清理文件名，移除非法字符"""
    # 移除文件名中的 ID
    filename = re.sub(r'\s+[\da-f]{32}$', '', filename)
    # 替换空格为短横线
    filename = filename.replace(' ', '-')
    # 移除其他非法字符
    filename = re.sub(r'[^\w\-\.]', '', filename)
    return filename

def extract_front_matter(content):
    """从 Markdown 内容中提取 Front Matter"""
    front_matter = {}
    content_lines = content.split('\n')
    
    # 检查第一行是否为标题
    if content_lines[0].startswith('# '):
        front_matter['title'] = content_lines[0][2:].strip()
    
    # 查找 Tags、Created、Updated 等信息
    for line in content_lines[:10]:  # 只检查前10行
        if line.startswith('Tags: '):
            front_matter['tags'] = [tag.strip() for tag in line[6:].split(',')]
        elif line.startswith('Created: '):
            date_str = line[9:].strip()
            try:
                date = datetime.strptime(date_str, '%B %d, %Y %I:%M %p')
                front_matter['date'] = date.strftime('%Y-%m-%d')
            except ValueError:
                print(f"无法解析日期: {date_str}")
    
    # 设置默认值
    if 'draft' not in front_matter:
        front_matter['draft'] = False
    if 'author' not in front_matter:
        front_matter['author'] = 'Joe'
    
    return front_matter

def update_image_links(content, article_slug):
    """更新 Markdown 内容中的图片链接"""
    # 替换 Notion 风格的图片链接
    pattern = r'!\[(.*?)\]\((.*?)\)'
    
    def replace_link(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        # 获取图片文件名
        image_name = os.path.basename(image_path)
        # 构建新的图片路径
        new_path = f'/images/posts/{article_slug}/{sanitize_filename(image_name)}'
        return f'![{alt_text}]({new_path})'
    
    return re.sub(pattern, replace_link, content)

def process_markdown_file(src_path, dest_dir, images_base_dir):
    """处理单个 Markdown 文件"""
    try:
        # 读取文件内容
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取 Front Matter
        front_matter = extract_front_matter(content)
        
        # 构建文章 slug（用于文件名和图片目录）
        if 'title' in front_matter:
            article_slug = sanitize_filename(front_matter['title']).lower()
        else:
            article_slug = sanitize_filename(os.path.basename(src_path)).lower()
            if article_slug.endswith('.md'):
                article_slug = article_slug[:-3]
        
        # 检查文件是否已存在
        new_filename = f"{article_slug}.md"
        dest_path = os.path.join(dest_dir, new_filename)
        if os.path.exists(dest_path):
            print(f"文件已存在，跳过处理: {new_filename}")
            return None
        
        # 更新图片链接
        content = update_image_links(content, article_slug)
        
        # 确保目标目录存在
        os.makedirs(dest_dir, exist_ok=True)
        
        # 构建新的文件内容
        new_content = '---\n'
        new_content += yaml.dump(front_matter, allow_unicode=True)
        new_content += '---\n\n'
        new_content += content
        
        # 写入新文件
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"处理完成: {new_filename}")
        
        return article_slug
    except Exception as e:
        print(f"处理文件 {src_path} 时出错: {str(e)}")
        return None

def process_images(src_dir, article_slug, images_base_dir):
    """处理图片文件"""
    if not article_slug:
        return
    
    # 构建文章的图片目录
    article_images_dir = os.path.join(images_base_dir, 'posts', article_slug)
    os.makedirs(article_images_dir, exist_ok=True)
    
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
    image_counter = 1
    
    for root, _, files in os.walk(src_dir):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                src_path = os.path.join(root, file)
                
                # 构建新的文件名
                base_name = sanitize_filename(file)
                if base_name.startswith('Untitled'):
                    # 为 Untitled 图片生成更有意义的名称
                    ext = os.path.splitext(base_name)[1]
                    base_name = f"image-{image_counter}{ext}"
                    image_counter += 1
                
                # 复制图片文件
                dest_path = os.path.join(article_images_dir, base_name)
                try:
                    shutil.copy2(src_path, dest_path)
                    print(f"复制图片: {article_slug}/{base_name}")
                except Exception as e:
                    print(f"复制图片 {file} 时出错: {str(e)}")

def cleanup_processed_files(processed_dir):
    """清理已处理的文件"""
    try:
        if os.path.exists(processed_dir):
            shutil.rmtree(processed_dir)
            print(f"已删除处理完成的目录: {processed_dir}")
    except Exception as e:
        print(f"删除目录 {processed_dir} 时出错: {str(e)}")

def main():
    # 设置目录路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    content_dir = os.path.join(base_dir, 'content', 'posts')
    images_dir = os.path.join(base_dir, 'static', 'images')
    extracted_dir = os.path.join(base_dir, 'Notionfiles', 'extracted_new')
    
    # 确保目标目录存在
    os.makedirs(content_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    
    # 处理所有解压的目录
    for item in os.listdir(extracted_dir):
        item_path = os.path.join(extracted_dir, item)
        if os.path.isdir(item_path):
            # 查找目录中的 Markdown 文件
            for file in os.listdir(item_path):
                if file.endswith('.md'):
                    md_path = os.path.join(item_path, file)
                    article_slug = process_markdown_file(md_path, content_dir, images_dir)
                    if article_slug:
                        # 处理目录中的图片
                        process_images(item_path, article_slug, images_dir)
        elif item.endswith('.md'):
            # 直接处理 Markdown 文件
            article_slug = process_markdown_file(item_path, content_dir, images_dir)
            if article_slug:
                # 处理同目录下的图片
                process_images(os.path.dirname(item_path), article_slug, images_dir)
    
    # 清理已处理的文件
    cleanup_processed_files(extracted_dir)

if __name__ == '__main__':
    main() 