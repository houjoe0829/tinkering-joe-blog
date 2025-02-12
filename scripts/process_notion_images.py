#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
处理 Notion 导出文章图片的专用脚本
功能：
1. 将 Notion 导出的图片重命名为规范格式
2. 压缩图片并转换为 WebP 格式
3. 保持单一职责，只处理当前文章的图片
"""

import os
import sys
import shutil
from pathlib import Path
from PIL import Image
import argparse
import re

def sanitize_filename(filename):
    """清理文件名，确保符合规范"""
    # 移除非法字符，只保留字母、数字、连字符和点
    clean_name = re.sub(r'[^a-zA-Z0-9\-\.]', '-', filename)
    # 将多个连字符替换为单个
    clean_name = re.sub(r'-+', '-', clean_name)
    # 移除开头和结尾的连字符
    clean_name = clean_name.strip('-')
    return clean_name.lower()

def process_image(input_path, output_path, quality=85):
    """处理单个图片：压缩并转换为 WebP"""
    try:
        with Image.open(input_path) as img:
            # 保持原始尺寸，但限制最大尺寸为 1920x1920
            max_size = 1920
            if img.width > max_size or img.height > max_size:
                ratio = min(max_size/img.width, max_size/img.height)
                new_size = (int(img.width * ratio), int(img.height * ratio))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # 如果是 PNG，使用无损压缩
            if input_path.lower().endswith('.png'):
                img.save(output_path, 'WEBP', lossless=True, quality=100)
            else:
                img.save(output_path, 'WEBP', quality=quality, optimize=True)
            
            return True
    except Exception as e:
        print(f"处理图片 {input_path} 时出错: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='处理 Notion 导出文章的图片')
    parser.add_argument('article_name', help='文章的英文名称（用作目录名）')
    parser.add_argument('--input', '-i', required=True, help='Notion 导出的图片所在目录')
    parser.add_argument('--quality', '-q', type=int, default=85, help='压缩质量 (1-100), 默认 85')
    args = parser.parse_args()

    # 确保输入目录存在
    if not os.path.exists(args.input):
        print(f"错误: 输入目录 {args.input} 不存在")
        sys.exit(1)

    # 创建输出目录
    output_dir = f"static/images/posts/{args.article_name}"
    os.makedirs(output_dir, exist_ok=True)

    # 获取所有图片文件
    image_files = []
    for ext in ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG', '.webp', '.WEBP'):
        image_files.extend(Path(args.input).glob(f'*{ext}'))

    if not image_files:
        print("未找到任何图片文件")
        sys.exit(0)

    print(f"找到 {len(image_files)} 个图片文件")
    
    # 处理每个图片
    success_count = 0
    for i, img_path in enumerate(sorted(image_files), 1):
        # 生成新的文件名
        new_name = f"image-{i}.webp"
        output_path = os.path.join(output_dir, new_name)
        
        print(f"处理第 {i}/{len(image_files)} 个图片: {img_path.name} -> {new_name}")
        
        if process_image(str(img_path), output_path, args.quality):
            success_count += 1
            print(f"✓ 成功处理: {new_name}")
        else:
            print(f"✗ 处理失败: {img_path.name}")

    print(f"\n处理完成:")
    print(f"- 总计图片: {len(image_files)}")
    print(f"- 成功处理: {success_count}")
    print(f"- 失败数量: {len(image_files) - success_count}")
    print(f"\n处理后的图片位置: {output_dir}")

if __name__ == '__main__':
    main() 