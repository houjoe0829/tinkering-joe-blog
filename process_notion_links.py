#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
处理 Notion 导出文章中的图片链接
功能：
1. 解析 Markdown 文件中的图片链接
2. 下载远程图片到本地
3. 更新 Markdown 文件中的图片引用路径
"""

import os
import re
import sys
import requests
import argparse
from pathlib import Path
from urllib.parse import urlparse
import frontmatter
import hashlib
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import shutil

def download_image(url, output_dir):
    """下载图片并返回本地文件名"""
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            # 使用 URL 的 MD5 作为文件名，保留原始扩展名
            url_hash = hashlib.md5(url.encode()).hexdigest()
            parsed_url = urlparse(url)
            ext = os.path.splitext(parsed_url.path)[1]
            if not ext:
                # 如果 URL 没有扩展名，根据内容类型判断
                content_type = response.headers.get('content-type', '')
                if 'jpeg' in content_type or 'jpg' in content_type:
                    ext = '.jpg'
                elif 'png' in content_type:
                    ext = '.png'
                elif 'webp' in content_type:
                    ext = '.webp'
                else:
                    ext = '.jpg'  # 默认使用 jpg
            
            temp_filename = f"{url_hash}{ext}"
            output_path = os.path.join(output_dir, temp_filename)
            
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            return temp_filename
    except Exception as e:
        print(f"下载图片失败 {url}: {str(e)}")
        return None

def extract_metadata(content):
    """从 Notion 导出的 Markdown 内容中提取元数据"""
    metadata = {}
    
    # 提取标题
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1)
    
    # 提取标签
    tags_match = re.search(r'Tags:\s*(.+)$', content, re.MULTILINE)
    if tags_match:
        tags = [tag.strip() for tag in tags_match.group(1).split(',')]
        metadata['tags'] = tags
    
    # 提取创建时间
    created_match = re.search(r'Created:\s*(.+)$', content, re.MULTILINE)
    if created_match:
        try:
            created_date = datetime.strptime(created_match.group(1), '%B %d, %Y %I:%M %p')
            metadata['date'] = created_date.strftime('%Y-%m-%d')
        except:
            metadata['date'] = datetime.now().strftime('%Y-%m-%d')
    
    # 提取描述（使用第一个非标题、非元数据的文本段落）
    lines = content.split('\n')
    description = ''
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('Tags:') and \
           not line.startswith('Created:') and not line.startswith('Updated:') and \
           not line.startswith('[') and not line.startswith('<aside>'):
            # 移除 emoji 和其他特殊字符
            description = re.sub(r'[^\u4e00-\u9fff\u3040-\u30ff\u0020-\u007e]', '', line)
            description = description.strip()[:200]  # 限制描述长度为200字符
            break
    if description:
        metadata['description'] = description
    
    # 设置其他必要的元数据
    metadata['draft'] = False
    metadata['author'] = 'Joe'
    
    return metadata

def clean_content(content):
    """清理 Markdown 内容"""
    # 移除 Notion 特有的元数据
    content = re.sub(r'Tags:.*\n', '', content)
    content = re.sub(r'Created:.*\n', '', content)
    content = re.sub(r'Updated:.*\n', '', content)
    
    # 移除原始链接和提示框
    content = re.sub(r'\[朝鲜四日行纪录\].*\n', '', content)
    content = re.sub(r'<aside>[\s\S]*?</aside>\n*', '', content)
    
    # 移除重复的标题（保留第一个）
    title_pattern = re.compile(r'^#\s+(.+)$', re.MULTILINE)
    matches = list(title_pattern.finditer(content))
    if len(matches) > 1:
        for match in matches[1:]:
            content = content[:match.start()] + content[match.end()+1:]
    
    # 移除多余的空行
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()

def process_local_images(content, article_name, temp_dir):
    """处理本地图片引用"""
    # 查找本地图片引用
    local_image_pattern = r'!\[([^\]]*)\]\(([^)]+\.(?:jpg|jpeg|png|webp))\)'
    local_images = re.findall(local_image_pattern, content, re.IGNORECASE)
    
    for alt_text, image_path in local_images:
        if not image_path.startswith(('http://', 'https://', '/')):
            # 获取图片文件名
            image_name = os.path.basename(image_path)
            # 复制图片到临时目录
            src_path = os.path.join(os.path.dirname(temp_dir), image_name)
            if os.path.exists(src_path):
                dst_path = os.path.join(temp_dir, image_name)
                shutil.copy2(src_path, dst_path)
                print(f"复制本地图片: {image_name}")
    
    return content

def process_markdown_file(input_file, article_name):
    """处理 Markdown 文件中的图片链接"""
    # 创建临时图片目录
    temp_image_dir = os.path.join('temp_notion', 'downloaded_images')
    os.makedirs(temp_image_dir, exist_ok=True)
    
    # 读取 Markdown 文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取元数据
    metadata = extract_metadata(content)
    
    # 清理内容
    content = clean_content(content)
    
    # 处理本地图片
    content = process_local_images(content, article_name, temp_image_dir)
    
    # 查找所有图片链接，保持顺序
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    image_links = list(re.finditer(image_pattern, content))
    
    if not image_links:
        print("未找到图片链接")
        return
    
    print(f"找到 {len(image_links)} 个图片链接")
    
    # 创建图片信息映射，包含所有图片（无论是否下载成功）
    image_info_map = {}
    download_success_count = 0
    
    # 按顺序处理每个图片
    for i, match in enumerate(image_links, 1):
        alt_text, url = match.groups()
        img_info = {
            'alt_text': alt_text,
            'url': url,
            'start': match.start(),
            'end': match.end(),
            'original_text': match.group(0),
            'position': i,  # 记录在文章中的位置
            'downloaded': False,  # 标记是否下载成功
            'local_filename': None
        }
        
        if url.startswith('http'):
            print(f"下载图片 {i}/{len(image_links)}: {url}")
            local_filename = download_image(url, temp_image_dir)
            if local_filename:
                img_info['downloaded'] = True
                img_info['local_filename'] = local_filename
                download_success_count += 1
                print(f"✓ 成功下载 {i}/{len(image_links)}: {local_filename}")
            else:
                print(f"✗ 下载失败 {i}/{len(image_links)}: {url}")
        else:  # 本地图片
            img_info['downloaded'] = True  # 本地图片视为已下载
            img_info['local_filename'] = os.path.basename(url)
            download_success_count += 1
        
        image_info_map[url] = img_info
    
    # 处理下载的图片
    if os.listdir(temp_image_dir):
        print("\n处理下载的图片...")
        # 使用图片处理脚本处理下载的图片
        os.system(f'python process_notion_images.py {article_name} --input "{temp_image_dir}"')
        
        # 按照原始顺序更新 Markdown 文件中的图片引用
        new_content = content
        for match in reversed(image_links):  # 从后向前替换，避免位置变化
            alt_text, url = match.groups()
            img_info = image_info_map[url]
            position = img_info['position']  # 使用原始位置作为图片编号
            
            if img_info['downloaded']:  # 只替换成功下载的图片
                webp_filename = f"image-{position}.webp"
                new_path = f"/images/posts/{article_name}/{webp_filename}"
                new_content = (
                    new_content[:match.start()] +
                    f'![{alt_text}]({new_path})' +
                    new_content[match.end():]
                )
            # 下载失败的图片保持原始链接不变
        
        content = new_content
    
    # 创建新的 Front Matter
    post = frontmatter.Post(content, **metadata)
    
    # 保存更新后的 Markdown 文件
    output_file = os.path.join('content', 'posts', f'{article_name}.md')
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    
    print(f"\n处理完成:")
    print(f"- 总计图片链接: {len(image_links)}")
    print(f"- 成功下载: {download_success_count}")
    if len(image_links) > download_success_count:
        print(f"- 下载失败: {len(image_links) - download_success_count}")
    print(f"- 更新后的文件: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='处理 Notion 导出文章中的图片链接')
    parser.add_argument('article_name', help='文章的英文名称（用作目录名和文件名）')
    parser.add_argument('--input', '-i', required=True, help='Notion 导出的 Markdown 文件路径')
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"错误: 输入文件 {args.input} 不存在")
        sys.exit(1)
    
    process_markdown_file(args.input, args.article_name)

if __name__ == '__main__':
    main() 