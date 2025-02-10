import os
import subprocess
from pathlib import Path

def compress_images(input_dir, output_dir, quality=85):
    """
    压缩指定目录下的所有图片
    
    参数:
        input_dir: 输入目录路径
        output_dir: 输出目录路径
        quality: 压缩质量 (1-100)
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 支持的图片格式
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    
    # 遍历输入目录
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(image_extensions):
                # 构建输入输出路径
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                
                # 确保输出目录存在
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # 使用 ImageMagick 压缩图片
                cmd = [
                    'convert',
                    input_path,
                    '-strip',  # 移除元数据
                    '-quality', str(quality),  # 设置压缩质量
                    '-resize', '1920x1920>',  # 限制最大尺寸，保持比例
                    output_path
                ]
                
                try:
                    subprocess.run(cmd, check=True)
                    
                    # 获取压缩前后的文件大小
                    original_size = os.path.getsize(input_path)
                    compressed_size = os.path.getsize(output_path)
                    
                    # 计算压缩比例
                    ratio = (1 - compressed_size / original_size) * 100
                    
                    print(f'已压缩: {relative_path}')
                    print(f'原始大小: {original_size/1024:.1f}KB')
                    print(f'压缩后大小: {compressed_size/1024:.1f}KB')
                    print(f'压缩率: {ratio:.1f}%\n')
                    
                except subprocess.CalledProcessError as e:
                    print(f'压缩失败: {relative_path}')
                    print(f'错误信息: {str(e)}\n')

if __name__ == '__main__':
    # 设置输入输出目录
    input_dir = 'static/images'  # 原始图片目录
    output_dir = 'static/images_compressed'  # 压缩后的图片目录
    
    # 执行压缩
    compress_images(input_dir, output_dir)
    print('所有图片压缩完成！') 