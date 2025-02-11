import os
import zipfile
import shutil
from pathlib import Path
import subprocess
import glob

def clean_temp_files(temp_dir, zip_path):
    """清理所有临时文件和目录
    
    Args:
        temp_dir: 临时目录路径
        zip_path: ZIP 文件所在目录
    """
    print("\n开始清理临时文件...")
    
    # 1. 删除临时目录
    if os.path.exists(temp_dir):
        try:
            shutil.rmtree(temp_dir)
            print(f"✓ 已删除临时目录: {temp_dir}")
        except Exception as e:
            print(f"! 删除临时目录失败: {str(e)}")
    
    # 2. 删除 ZIP 文件
    try:
        # 使用 glob 模块查找所有 ZIP 文件
        zip_files = glob.glob(os.path.join(zip_path, "*.zip"))
        for zip_file in zip_files:
            os.remove(zip_file)
            print(f"✓ 已删除 ZIP 文件: {zip_file}")
    except Exception as e:
        print(f"! 删除 ZIP 文件失败: {str(e)}")

def convert_images_to_webp(article_name):
    """将文章的图片转换为 WebP 格式并删除原始文件
    
    Args:
        article_name: 文章的英文名称
    """
    image_dir = f"static/images/posts/{article_name}"
    if not os.path.exists(image_dir):
        return
    
    print(f"\n处理图片目录: {image_dir}")
    
    # 1. 转换为 WebP
    try:
        cmd = ('cd "{}" && for img in *.jpeg *.jpg *.png; do '
               '[ -f "$img" ] && cwebp -q 85 "$img" -o "${img%.*}.webp"; '
               'done').format(image_dir)
        subprocess.run(['bash', '-c', cmd], check=True)
        print("✓ 图片转换完成")
    except subprocess.CalledProcessError as e:
        print(f"! 图片转换失败: {str(e)}")
        return
    
    # 2. 删除原始图片
    try:
        cmd = 'cd "{}" && rm -f *.jpeg *.jpg *.png'.format(image_dir)
        subprocess.run(['bash', '-c', cmd], check=True)
        print("✓ 已删除原始图片文件")
    except subprocess.CalledProcessError as e:
        print(f"! 删除原始图片失败: {str(e)}")

def extract_zip_utf8(zip_path="Notionfiles"):
    """解压并处理 Notion 导出的 ZIP 文件
    
    Args:
        zip_path: ZIP 文件所在目录
    """
    # 创建临时目录
    temp_dir = "temp_notion"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # 查找 ZIP 文件
    zip_files = [f for f in os.listdir(zip_path) if f.endswith('.zip')]
    if not zip_files:
        print("未找到 ZIP 文件")
        return
    
    for zip_file in zip_files:
        full_path = os.path.join(zip_path, zip_file)
        print(f"正在解压文件: {full_path}")
        
        try:
            with zipfile.ZipFile(full_path, 'r') as zip_ref:
                # 解压所有文件
                for file_info in zip_ref.filelist:
                    try:
                        # 使用 CP437 编码处理文件名
                        file_name = file_info.filename.encode('cp437').decode('utf-8')
                    except:
                        # 如果转换失败，尝试直接使用原始文件名
                        file_name = file_info.filename
                    
                    # 创建目标路径
                    target_path = os.path.join(temp_dir, file_name)
                    
                    # 确保目标目录存在
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    
                    # 解压文件
                    try:
                        source = zip_ref.open(file_info)
                        target = open(target_path, "wb")
                        with source, target:
                            shutil.copyfileobj(source, target)
                        print(f"成功提取: {file_name}")
                    except Exception as e:
                        print(f"提取文件失败: {file_name}")
                        print(f"错误信息: {str(e)}")
                        continue
                
                # 处理所有 Markdown 文件
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        if file.endswith('.md'):
                            md_path = os.path.join(root, file)
                            # 从文件名生成文章英文名
                            article_name = os.path.splitext(file)[0]
                            article_name = article_name.split()[0]  # 取第一个空格前的部分
                            article_name = ''.join(c.lower() if c.isalnum() else '-' for c in article_name)
                            article_name = article_name.strip('-')
                            
                            print(f"\n处理文章: {article_name}")
                            # 调用 process_notion_links.py 处理文章
                            try:
                                subprocess.run(['python', 'process_notion_links.py', 
                                             article_name, '--input', md_path], 
                                             check=True)
                                
                                # 处理完文章后，转换并清理图片
                                convert_images_to_webp(article_name)
                                
                            except subprocess.CalledProcessError as e:
                                print(f"处理文章失败: {str(e)}")
                                continue
        
        except Exception as e:
            print(f"处理 ZIP 文件时出错: {str(e)}")
            continue
    
    # 最后清理所有临时文件
    clean_temp_files(temp_dir, zip_path)
    print("\n全部处理完成！")

if __name__ == "__main__":
    extract_zip_utf8() 