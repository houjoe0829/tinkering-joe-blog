import os
import subprocess
from pathlib import Path

def compress_images(input_dir, output_dir, quality=85, convert_to_webp=False):
    """
    压缩指定目录下的所有图片
    
    参数:
        input_dir: 输入目录路径
        output_dir: 输出目录路径
        quality: 压缩质量 (1-100)
        convert_to_webp: 是否转换为 WebP 格式
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
                
                # 如果转换为 WebP，修改输出文件扩展名
                if convert_to_webp:
                    output_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.webp')
                else:
                    output_path = os.path.join(output_dir, relative_path)
                
                # 确保输出目录存在
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # 使用 ImageMagick 压缩图片
                cmd = [
                    'magick',
                    input_path,
                    '-strip',  # 移除元数据
                    '-quality', str(quality),  # 设置压缩质量
                    '-resize', '1920x1920>',  # 限制最大尺寸，保持比例
                    '-sampling-factor', '4:2:0',  # 优化采样
                    '-interlace', 'Plane',  # 渐进式加载
                    '-colorspace', 'sRGB',  # 使用 sRGB 色彩空间
                ]
                
                # 如果是 PNG 格式的图片，使用无损压缩
                if file.lower().endswith('.png'):
                    if convert_to_webp:
                        cmd.extend(['-define', 'webp:lossless=true'])
                    else:
                        cmd.extend(['-define', 'png:compression-level=9'])
                
                # 添加输出路径
                cmd.append(output_path)
                
                try:
                    subprocess.run(cmd, check=True)
                    
                    # 获取压缩前后的文件大小
                    original_size = os.path.getsize(input_path)
                    compressed_size = os.path.getsize(output_path)
                    
                    # 如果压缩后的文件更大，且不是转换为 WebP 的情况，使用原始文件
                    if compressed_size >= original_size and not convert_to_webp:
                        os.replace(input_path, output_path)
                        print(f'保持原始文件: {relative_path} (压缩无效)')
                        continue
                    
                    # 计算压缩比例
                    ratio = (1 - compressed_size / original_size) * 100
                    
                    print(f'已处理: {relative_path} -> {os.path.basename(output_path)}')
                    print(f'原始大小: {original_size/1024:.1f}KB')
                    print(f'处理后大小: {compressed_size/1024:.1f}KB')
                    print(f'压缩率: {ratio:.1f}%\n')
                    
                except subprocess.CalledProcessError as e:
                    print(f'处理失败: {relative_path}')
                    print(f'错误信息: {str(e)}\n')

if __name__ == '__main__':
    # 设置输入输出目录
    input_dir = 'static/images'  # 原始图片目录
    output_dir = 'static/images_compressed'  # 压缩后的图片目录
    
    # 执行压缩
    # 对于 PNG 使用无损压缩，对于 JPEG 使用 85 的质量
    compress_images(input_dir, output_dir, quality=85, convert_to_webp=True)
    print('所有图片处理完成！') 