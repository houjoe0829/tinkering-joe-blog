import os
import zipfile
import shutil
from pathlib import Path

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
    # 设置输入输出路径
    zip_path = 'Notionfiles/a664cadd-0803-446f-9ecb-29ef5e62d09e_Export-ade6ddf2-97a8-40e4-bb29-220605dcae20.zip'
    extract_dir = 'temp_notion'
    
    # 执行解压
    extract_zip_with_utf8(zip_path, extract_dir)
    print('解压完成！') 