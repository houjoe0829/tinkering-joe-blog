#!/usr/bin/env python3
import os
import sys
from PIL import Image
import piexif
from pathlib import Path
import shutil

def compress_image(input_path, output_path, max_size=(1920, 1920), quality=85):
    """压缩单张图片并转换为 WebP 格式
    
    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径
        max_size: 最大尺寸，默认 1920x1920
        quality: 压缩质量，默认 85%
    """
    try:
        # 读取图片
        img = Image.open(input_path)
        
        # 应用 EXIF 旋转
        try:
            if hasattr(img, '_getexif'):
                exif = img._getexif()
                if exif is not None:
                    orientation = exif.get(274)  # 274 是 Orientation 标记的 ID
                    if orientation is not None:
                        # 根据 Orientation 值旋转图片
                        if orientation == 3:
                            img = img.rotate(180, expand=True)
                        elif orientation == 6:
                            img = img.rotate(270, expand=True)
                        elif orientation == 8:
                            img = img.rotate(90, expand=True)
        except:
            pass  # 如果无法读取或应用 EXIF 数据，就使用原始图片
        
        # 移除 EXIF 数据
        if "exif" in img.info:
            img.info.pop("exif")
        
        # 调整尺寸，保持比例
        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # 确保输出目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 判断原图格式
        is_png = input_path.lower().endswith('.png')
        
        # PNG 使用无损压缩，JPG 使用有损压缩
        if is_png:
            img.save(output_path, 'WEBP', lossless=True, quality=100)
        else:
            img.save(output_path, 'WEBP', quality=quality)
        
        # 计算压缩率
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)
        ratio = (original_size - compressed_size) / original_size * 100
        
        print(f"处理完成: {os.path.basename(input_path)}")
        print(f"原始大小: {original_size/1024:.1f}KB")
        print(f"压缩大小: {compressed_size/1024:.1f}KB")
        print(f"压缩率: {ratio:.1f}%\n")
        
    except Exception as e:
        print(f"处理图片出错 {input_path}: {str(e)}")

def process_article_images(article_path):
    """处理指定文章的所有图片
    
    Args:
        article_path: 文章的完整路径
    """
    # 从文章路径中提取文章类型和名称
    path_parts = article_path.split('/')
    if len(path_parts) < 2:
        print(f"错误：无效的文章路径: {article_path}")
        sys.exit(1)
        
    article_type = path_parts[-2]  # posts 或 thoughts
    article_name = path_parts[-1].replace('.md', '')
    
    # 构建源目录和目标目录
    source_dir = f"static/images/{article_type}/{article_name}"
    target_dir = f"static/images_compressed/{article_type}/{article_name}"
    
    # 检查源目录是否存在
    if not os.path.exists(source_dir):
        print(f"错误：文章目录不存在: {source_dir}")
        sys.exit(1)
    
    # 清理目标目录（如果存在）
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    
    # 创建目标目录
    os.makedirs(target_dir, exist_ok=True)
    
    print(f"\n开始处理文章 '{article_name}' 的图片...")
    
    # 获取所有图片文件
    image_files = []
    for ext in ('*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG'):
        image_files.extend(Path(source_dir).glob(ext))
    
    if not image_files:
        print(f"警告：在目录 {source_dir} 中没有找到图片文件")
        return
    
    # 处理每张图片
    for img_path in image_files:
        output_path = os.path.join(
            target_dir,
            os.path.splitext(img_path.name)[0] + '.webp'
        )
        compress_image(str(img_path), output_path)
    
    print(f"\n文章 '{article_name}' 的图片处理完成！")
    print(f"压缩后的图片保存在: {target_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python compress_article_images.py <article-path>")
        print("示例: python compress_article_images.py content/posts/my-article.md")
        print("      python compress_article_images.py content/thoughts/my-thought.md")
        sys.exit(1)
    
    article_name = sys.argv[1]
    process_article_images(article_name) 