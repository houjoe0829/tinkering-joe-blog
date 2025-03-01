#!/usr/bin/env python3
import os
import re
from pathlib import Path
from urllib.parse import unquote

def find_image_refs(md_file):
    """查找 Markdown 文件中的所有图片引用"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # 匹配 Markdown 图片语法
    markdown_refs = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
    
    # 匹配 HTML 图片标签
    html_refs = re.findall(r'<img\s+[^>]*src="([^"]+)"[^>]*>', content)
    
    # 将 HTML 图片引用转换为与 Markdown 格式相同的元组格式 (alt_text, image_path)
    html_tuples = [(f"HTML图片", ref) for ref in html_refs]
    
    return markdown_refs + html_tuples

def check_image_exists(image_path):
    """检查图片文件是否存在"""
    # 如果是完整 URL，跳过检查
    if image_path.startswith(('http://', 'https://')):
        return True, "外部链接"
    
    # 移除 URL 参数（如果有）
    image_path = image_path.split('?')[0]
    
    # URL 解码路径
    decoded_path = unquote(image_path)
    
    # 构建完整的文件路径（尝试原始路径和解码后的路径）
    full_path = os.path.join('static', image_path.lstrip('/'))
    decoded_full_path = os.path.join('static', decoded_path.lstrip('/'))
    
    # 检查文件是否存在（原始路径或解码后的路径）
    exists = os.path.exists(full_path) or os.path.exists(decoded_full_path)
    return exists, full_path if os.path.exists(full_path) else decoded_full_path

def main():
    # 获取所有 Markdown 文件
    md_files = list(Path('content').rglob('*.md'))
    
    # 用于统计的变量
    total_images = 0
    broken_refs = []
    external_links = []
    
    print("开始检查图片引用...")
    print("-" * 50)
    
    # 检查每个 Markdown 文件
    for md_file in md_files:
        image_refs = find_image_refs(str(md_file))
        if not image_refs:
            continue
            
        print(f"\n检查文件: {md_file}")
        for alt_text, image_path in image_refs:
            total_images += 1
            exists, full_path = check_image_exists(image_path)
            
            if image_path.startswith(('http://', 'https://')):
                external_links.append((str(md_file), image_path))
                print(f"  [外部链接] {image_path}")
            elif not exists:
                broken_refs.append((str(md_file), image_path))
                print(f"  [失败] {image_path} -> {full_path}")
            else:
                print(f"  [成功] {image_path}")
    
    print("\n" + "=" * 50)
    print("检查完成！统计信息：")
    print(f"- 总共检查了 {len(md_files)} 个 Markdown 文件")
    print(f"- 发现 {total_images} 个图片引用")
    print(f"- 其中 {len(external_links)} 个外部链接")
    print(f"- 发现 {len(broken_refs)} 个失效的图片引用")
    
    if broken_refs:
        print("\n失效的图片引用：")
        for md_file, image_path in broken_refs:
            print(f"- 在文件 {md_file} 中: {image_path}")
    
    if external_links:
        print("\n外部图片链接：")
        for md_file, image_path in external_links:
            print(f"- 在文件 {md_file} 中: {image_path}")

if __name__ == '__main__':
    main() 