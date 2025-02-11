import os
import zipfile
import shutil
from pathlib import Path
import glob

def extract_zip_with_utf8(zip_path, extract_dir):
    # 确保目标目录存在
    os.makedirs(extract_dir, exist_ok=True)
    
    # 使用 UTF-8 编码打开 ZIP 文件
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # 遍历 ZIP 文件中的所有文件
        for file_info in zip_ref.filelist:
            try:
                # 尝试直接使用 UTF-8 解码
                file_name = file_info.filename
                # 构建目标路径
                target_path = os.path.join(extract_dir, file_name)
                # 确保目标目录存在
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                # 提取文件
                if file_info.filename.endswith('/'):
                    os.makedirs(target_path, exist_ok=True)
                else:
                    # 提取文件内容
                    with zip_ref.open(file_info) as source, open(target_path, 'wb') as target:
                        shutil.copyfileobj(source, target)
                print(f"成功提取: {file_name}")
            except Exception as e:
                print(f"提取文件时出错: {str(e)}")

if __name__ == '__main__':
    # 查找 Notionfiles 目录下的第一个 ZIP 文件
    zip_files = glob.glob('Notionfiles/*.zip')
    if not zip_files:
        print('错误：在 Notionfiles 目录下没有找到 ZIP 文件')
        exit(1)
    
    # 设置输入输出路径
    zip_path = zip_files[0]
    extract_dir = 'temp_notion'
    
    # 如果目标目录已存在，先删除它
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    
    print(f'正在解压文件: {zip_path}')
    # 执行解压
    extract_zip_with_utf8(zip_path, extract_dir)
    print('解压完成！') 