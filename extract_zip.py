import os
import zipfile
import json
import uuid
import re
from pathlib import Path
import tempfile
import shutil
import unicodedata
import logging
import sys
from pypinyin import lazy_pinyin, Style

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('extraction.log', encoding='utf-8')
    ]
)

def to_pinyin(text):
    """将中文文本转换为拼音"""
    # 将文本转换为拼音，保留非中文字符
    pinyin_list = lazy_pinyin(text, style=Style.NORMAL, errors='ignore')
    # 将拼音列表组合成字符串，用连字符连接
    result = '-'.join(pinyin_list)
    # 移除不允许的字符
    result = ''.join(c if c.isalnum() or c in '-_.' else '-' for c in result)
    # 替换连续的连字符
    while '--' in result:
        result = result.replace('--', '-')
    # 确保文件名不以连字符开始或结束
    result = result.strip('-')
    return result or 'unnamed'

def get_safe_filename(original_name):
    """生成安全的文件名"""
    # 分离文件名和扩展名
    base_name, ext = os.path.splitext(original_name)
    
    # 转换为拼音
    safe_base_name = to_pinyin(base_name)
    
    # 如果文件名为空，使用 UUID
    if not safe_base_name:
        safe_base_name = str(uuid.uuid4())
    
    # 组合新的文件名
    return safe_base_name + ext

def safe_extract_file(zip_file, member, target_dir):
    """安全地提取单个文件，使用 UUID 作为文件名"""
    try:
        # 生成唯一的文件名
        unique_name = str(uuid.uuid4())
        
        # 获取原始文件扩展名（如果有）
        _, ext = os.path.splitext(member.filename)
        
        # 组合新的文件名
        safe_name = unique_name + ext
        
        # 创建目标路径
        target_path = Path(target_dir) / safe_name
        
        # 确保父目录存在
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 使用临时文件进行提取
        temp_path = target_path.parent / f"{uuid.uuid4()}.tmp"
        
        try:
            # 提取到临时文件
            with zip_file.open(member) as source, open(temp_path, 'wb') as target:
                shutil.copyfileobj(source, target)
            
            # 重命名为最终文件名
            temp_path.replace(target_path)
            
            # 尝试获取原始文件名
            try:
                original_name = member.filename.encode('cp437').decode('utf-8')
            except UnicodeEncodeError:
                original_name = member.filename
            
            logging.info(f"成功提取文件: {original_name} -> {safe_name}")
            return True, safe_name, original_name
            
        except Exception as e:
            if temp_path.exists():
                temp_path.unlink()
            raise e
            
    except Exception as e:
        logging.error(f"提取文件时出错: {member.filename}")
        logging.error(f"错误信息: {str(e)}")
        return False, None, None

def extract_zip_files(zip_path, target_dir):
    """提取 ZIP 文件的主函数"""
    try:
        # 确保目标目录存在
        Path(target_dir).mkdir(parents=True, exist_ok=True)
        
        # 创建 ZIP 文件对象
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # 获取 ZIP 文件的基本名称（不包含路径和扩展名）
            zip_base_name = Path(zip_path).stem
            
            # 为这个 ZIP 文件创建专门的目标目录
            zip_target_dir = Path(target_dir) / zip_base_name
            zip_target_dir.mkdir(parents=True, exist_ok=True)
            
            # 记录文件名映射
            filename_mapping = {}
            
            # 提取所有文件
            for member in zip_ref.filelist:
                success, safe_name, original_name = safe_extract_file(zip_ref, member, zip_target_dir)
                if success:
                    filename_mapping[safe_name] = original_name
            
            # 保存文件名映射
            mapping_file = zip_target_dir / 'filename_mapping.json'
            with open(mapping_file, 'w', encoding='utf-8') as f:
                json.dump(filename_mapping, f, ensure_ascii=False, indent=2)
            
            logging.info(f"成功解压 ZIP 文件到: {zip_target_dir}")
            
    except Exception as e:
        logging.error(f"处理 ZIP 文件时出错: {zip_path}")
        logging.error(f"错误信息: {str(e)}")

def main():
    """主函数"""
    # 设置工作目录
    current_dir = Path.cwd()
    zip_files = list(current_dir.glob('*.zip'))
    
    if not zip_files:
        logging.warning("当前目录下没有找到 ZIP 文件")
        return
    
    # 创建输出目录
    output_dir = current_dir / 'extracted_new'
    output_dir.mkdir(exist_ok=True)
    
    # 处理每个 ZIP 文件
    for zip_file in zip_files:
        logging.info(f"\n开始处理: {zip_file.name}")
        extract_zip_files(zip_file, output_dir)

if __name__ == '__main__':
    main()