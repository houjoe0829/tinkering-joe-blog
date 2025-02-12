import os
import argparse
from pathlib import Path

def clean_original_images(images_dir, dry_run=True):
    """
    清理已转换为WebP格式的原始图片文件
    
    参数:
        images_dir: 图片目录路径
        dry_run: 如果为True，只显示将被删除的文件而不实际删除
    """
    # 要清理的图片格式
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    
    # 不删除的特殊文件（完整匹配）
    protected_files = (
        'favicon.ico',
        'apple-touch-icon.png',
        'android-chrome-192x192.png',
        'android-chrome-512x512.png'
    )
    
    # 不删除的文件模式（部分匹配）
    protected_patterns = (
        'favicon',
        'apple-touch-icon',
        'android-chrome'
    )
    
    # 统计信息
    total_files = 0
    total_size = 0
    
    print(f"{'预览' if dry_run else '开始'}清理原始图片...")
    print("-" * 50)
    
    # 遍历目录
    for root, _, files in os.walk(images_dir):
        for file in files:
            file_lower = file.lower()
            
            # 跳过完全匹配的保护文件
            if file in protected_files:
                continue
                
            # 跳过包含保护模式的文件
            if any(pattern in file_lower for pattern in protected_patterns):
                continue
                
            # 检查是否是目标格式
            if file_lower.endswith(image_extensions):
                file_path = os.path.join(root, file)
                webp_path = os.path.splitext(file_path)[0] + '.webp'
                
                # 检查对应的WebP文件是否存在
                if os.path.exists(webp_path):
                    file_size = os.path.getsize(file_path)
                    total_files += 1
                    total_size += file_size
                    
                    print(f"将删除: {os.path.relpath(file_path, images_dir)}")
                    print(f"文件大小: {file_size/1024:.1f}KB")
                    
                    if not dry_run:
                        os.remove(file_path)
    
    print("-" * 50)
    print(f"总计{'将' if dry_run else '已'}删除 {total_files} 个文件")
    print(f"总计{'将' if dry_run else '已'}释放 {total_size/1024/1024:.1f}MB 空间")
    
    if dry_run:
        print("\n这是预览模式，没有实际删除文件。")
        print("如果确认无误，请使用 --execute 参数运行脚本来实际删除文件。")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='清理已转换为WebP格式的原始图片文件')
    parser.add_argument('--execute', action='store_true', help='实际执行删除操作（默认为预览模式）')
    args = parser.parse_args()
    
    # 设置图片目录
    images_dir = 'static'  # 修改为 static 目录
    
    # 执行清理
    clean_original_images(images_dir, dry_run=not args.execute) 