import os
import zipfile
import shutil
from pathlib import Path

def extract_zip(zip_path, extract_dir):
    """
    解压 ZIP 文件，并正确处理中文文件名
    
    参数:
        zip_path: ZIP 文件路径
        extract_dir: 解压目标目录
    """
    # 确保目标目录存在
    os.makedirs(extract_dir, exist_ok=True)
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # 获取所有文件列表
            file_list = zip_ref.namelist()
            
            # 解压所有文件
            for file in file_list:
                try:
                    # 使用 cp437 编码处理文件名
                    filename = file.encode('cp437').decode('utf-8')
                    
                    # 构建目标路径
                    target_path = os.path.join(extract_dir, filename)
                    
                    # 确保目标目录存在
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    
                    # 解压文件
                    source = zip_ref.open(file)
                    target = open(target_path, "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
                        
                    print(f'已解压: {filename}')
                    
                except Exception as e:
                    print(f'解压文件时出错: {file}')
                    print(f'错误信息: {str(e)}')
                    continue
            
            print(f'\n成功解压 ZIP 文件到: {extract_dir}')
            
    except Exception as e:
        print(f'打开 ZIP 文件时出错: {zip_path}')
        print(f'错误信息: {str(e)}')

if __name__ == '__main__':
    # 获取所有 ZIP 文件
    zip_files = [f for f in os.listdir('.') if f.endswith('.zip')]
    
    # 按文件大小排序
    zip_files.sort(key=lambda x: os.path.getsize(x))
    
    # 解压所有 ZIP 文件
    for zip_file in zip_files:
        print(f'\n开始处理: {zip_file}')
        extract_dir = os.path.join('extracted_new', os.path.splitext(zip_file)[0])
        extract_zip(zip_file, extract_dir) 