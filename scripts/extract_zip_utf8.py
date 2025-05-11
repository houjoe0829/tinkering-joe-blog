import os
import zipfile
import shutil
from pathlib import Path
import re
from datetime import datetime
import sys

def extract_notion_metadata(content):
    """从 Notion 导出的内容中提取创建时间
    
    Args:
        content: 原始文章内容
    
    Returns:
        创建时间字符串 (YYYY-MM-DD)，如果无法解析则返回 None
    """
    # 查找 Created: 行
    created_pattern = r'Created: ([A-Za-z]+ \d{1,2}, \d{4})'
    match = re.search(created_pattern, content)
    
    if match:
        try:
            # 将 Notion 的日期格式转换为 datetime 对象
            date_str = match.group(1)
            date_obj = datetime.strptime(date_str, '%B %d, %Y')
            # 转换为 YYYY-MM-DD 格式
            return date_obj.strftime('%Y-%m-%d')
        except ValueError as e:
            print(f"警告：无法解析创建时间 '{date_str}': {e}")
            return None
    
    return None

def clean_notion_metadata(content):
    """清理 Notion 导出的元数据，只保留标题、正文和图片引用
    
    Args:
        content: 原始文章内容
    
    Returns:
        清理后的文章内容
    """
    # 分割内容为行
    lines = content.split('\n')
    
    # 清理 Notion 特有的元数据行
    cleaned_lines = []
    skip_patterns = [
        r'^Created:.*$',
        r'^Created time:.*$',
        r'^Updated:.*$',
        r'^Last edited:.*$',
        r'^Last edited time:.*$',
        r'^Tags:.*$',
        r'^Author:.*$'
    ]
    
    # 编译正则表达式
    skip_patterns = [re.compile(pattern) for pattern in skip_patterns]
    
    # 处理正文内容
    for line in lines:
        line = line.rstrip()  # 只移除行尾空白，保留行首空白
        
        # 如果是空行，保留它
        if not line:
            cleaned_lines.append(line)
            continue
            
        # 如果是图片引用行，确保完整保留，包括所有空白和路径
        if '![' in line and '](' in line and ')' in line:
            cleaned_lines.append(line)
            continue
            
        # 检查是否匹配任何需要跳过的模式
        should_skip = any(pattern.match(line.strip()) for pattern in skip_patterns)
        if not should_skip:
            cleaned_lines.append(line)
    
    # 移除多余的空行，但保留必要的段落分隔
    content = '\n'.join(cleaned_lines)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip() + '\n'

def decode_filename(name):
    """尝试多种编码方式解码文件名
    
    Args:
        name: 原始文件名
    
    Returns:
        解码后的文件名
    """
    encodings = ['utf-8', 'cp437', 'gbk', 'gb18030']
    
    # 如果已经是 UTF-8，直接返回
    try:
        name.encode('utf-8').decode('utf-8')
        return name
    except UnicodeEncodeError:
        pass
    
    # 尝试不同的编码
    for enc in encodings:
        try:
            if enc == 'cp437':
                # ZIP 文件特殊处理
                decoded = name.encode('cp437').decode('utf-8')
            else:
                # 其他编码直接尝试
                decoded = name.encode('cp437').decode(enc)
            return decoded
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
    
    # 如果所有尝试都失败，返回原始名称并打印警告
    print(f"警告：无法正确解码文件名 '{name}'，将使用原始名称")
    return name

def main():
    """主函数，处理 Notion 导出的 ZIP 文件
    只提取标题、正文、创建日期和图片
    """
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("用法: python3 extract_zip_utf8.py <zip文件路径>")
        sys.exit(1)
    
    zip_path = Path(sys.argv[1])
    if not zip_path.exists():
        print(f"错误：找不到文件 {zip_path}")
        sys.exit(1)
    
    # 创建临时目录
    temp_dir = Path('temp_notion')
    temp_dir.mkdir(exist_ok=True)
    
    print(f"正在解压文件: {zip_path}")
    
    # 解压 ZIP 文件
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # 获取所有 Markdown 文件和图片文件
        markdown_files = [f for f in zip_ref.namelist() if f.endswith('.md')]
        image_files = [f for f in zip_ref.namelist() if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]
        
        # 处理 Markdown 文件
        for md_file in markdown_files:
            # 解码文件名（处理中文）
            decoded_name = decode_filename(md_file)
            print(f"正在处理文章: {decoded_name}")
            
            # 读取文件内容
            try:
                content = zip_ref.read(md_file).decode('utf-8')
            except UnicodeDecodeError:
                try:
                    content = zip_ref.read(md_file).decode('gbk')
                except UnicodeDecodeError:
                    try:
                        content = zip_ref.read(md_file).decode('gb18030')
                    except UnicodeDecodeError:
                        print(f"错误：无法解码文件内容 '{decoded_name}'")
                        continue
            
            # 提取创建时间
            created_time = extract_notion_metadata(content)
            if not created_time:
                print(f"警告：无法从文件中提取创建时间，将使用当前时间")
                created_time = datetime.now().strftime('%Y-%m-%d')
            
            # 清理 Notion 元数据，只保留标题和正文
            content = clean_notion_metadata(content)
            
            # 保存处理后的文件
            output_path = temp_dir / Path(decoded_name).name
            # 确保父目录存在
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(content, encoding='utf-8')
            
            # 在文件开头添加创建时间的注释
            with open(output_path, 'r+', encoding='utf-8') as f:
                content = f.read()
                f.seek(0)
                f.write(f"<!-- Created: {created_time} -->\n\n{content}")
        
        # 提取所有图片文件到扁平结构
        for img_file in image_files:
            try:
                # 解码文件名
                decoded_name = decode_filename(img_file)
                # 只使用文件名部分，不保留路径
                target_path = temp_dir / Path(decoded_name).name
                
                # 提取图片文件
                with zip_ref.open(img_file) as source, open(target_path, 'wb') as target:
                    shutil.copyfileobj(source, target)
                print(f"已提取图片: {decoded_name}")
            except Exception as e:
                print(f"警告：提取图片失败 '{img_file}': {e}")
    
    print("\n解压和基础处理完成！")
    print("\n后续步骤：")
    print("1. 手动修改文件名，确保符合规范")
    print("2. 手动处理图片（复制、重命名、压缩）")
    print("3. 手动添加文章元数据（标签等）")
    print("4. 清理临时文件")

if __name__ == '__main__':
    main() 