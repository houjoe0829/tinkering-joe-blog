#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检查和修正博客文章中的中英文排版问题
使用pangu.py自动在中英文之间添加空格

使用方法:
    python3 scripts/check_spacing.py                # 检查所有文章并显示需要修正的内容
    python3 scripts/check_spacing.py --fix          # 检查并自动修正所有文章
    python3 scripts/check_spacing.py --file <file>  # 只检查指定文件
"""

import os
import sys
import glob
import argparse
import re
from pathlib import Path
import colorama
from colorama import Fore, Style

# 尝试导入pangu，如果没有安装则提示安装
try:
    import pangu
except ImportError:
    print(f"{Fore.RED}错误: 未找到pangu模块。请先安装:{Style.RESET_ALL}")
    print("pip install pangu")
    sys.exit(1)

# 初始化colorama
colorama.init()

# 定义文章目录
CONTENT_DIR = "content/posts"

def is_front_matter(line, in_front_matter):
    """判断当前行是否是Front Matter的分隔符"""
    if line.strip() == "---":
        return not in_front_matter
    return in_front_matter

def process_file(file_path, fix=False):
    """处理单个文件，检查并可选地修正中英文排版问题"""
    print(f"处理文件: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分离Front Matter和正文
    lines = content.split('\n')
    front_matter_lines = []
    content_lines = []
    
    in_front_matter = False
    for line in lines:
        if line.strip() == "---" and not in_front_matter:
            in_front_matter = True
            front_matter_lines.append(line)
        elif line.strip() == "---" and in_front_matter:
            in_front_matter = False
            front_matter_lines.append(line)
        elif in_front_matter:
            front_matter_lines.append(line)
        else:
            content_lines.append(line)
    
    # 逐行处理正文部分，保持Front Matter不变
    # 修改：不再整体处理文本，而是逐行处理，保留空行
    spaced_lines = []
    for line in content_lines:
        if line.strip() == "":
            # 保留空行
            spaced_lines.append(line)
        else:
            # 只处理非空行
            spaced_lines.append(pangu.spacing_text(line))
    
    # 将处理后的行重新组合
    spaced_content = '\n'.join(spaced_lines)
    content_text = '\n'.join(content_lines)
    
    # 如果内容有变化，显示差异
    if content_text != spaced_content:
        print(f"{Fore.YELLOW}发现排版问题:{Style.RESET_ALL}")
        
        # 分割为行以显示差异
        original_lines = content_text.split('\n')
        spaced_lines = spaced_content.split('\n')
        
        changes_found = False
        for i, (orig, spaced) in enumerate(zip(original_lines, spaced_lines)):
            if orig != spaced:
                changes_found = True
                line_num = i + len(front_matter_lines) + 1  # +1 因为行号从1开始
                print(f"{Fore.CYAN}第 {line_num} 行:{Style.RESET_ALL}")
                print(f"{Fore.RED}- {orig}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}+ {spaced}{Style.RESET_ALL}")
                print()
        
        if not changes_found:
            print(f"{Fore.YELLOW}内容有变化，但无法显示具体行差异{Style.RESET_ALL}")
        
        # 如果需要修正，写回文件
        if fix:
            new_content = '\n'.join(front_matter_lines + [''] + spaced_lines)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"{Fore.GREEN}已修正文件: {file_path}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}使用 --fix 参数可自动修正这些问题{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}文件排版正常: {file_path}{Style.RESET_ALL}")
    
    return content_text != spaced_content

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='检查和修正博客文章中的中英文排版问题')
    parser.add_argument('--fix', action='store_true', help='自动修正排版问题')
    parser.add_argument('--file', type=str, help='只检查指定文件')
    args = parser.parse_args()
    
    # 确定要处理的文件列表
    if args.file:
        if os.path.exists(args.file):
            files = [args.file]
        else:
            print(f"{Fore.RED}错误: 文件不存在: {args.file}{Style.RESET_ALL}")
            return 1
    else:
        files = glob.glob(os.path.join(CONTENT_DIR, "**/*.md"), recursive=True)
    
    # 处理所有文件
    issues_found = 0
    for file_path in files:
        if process_file(file_path, args.fix):
            issues_found += 1
    
    # 输出统计信息
    print("\n" + "="*50)
    print(f"检查了 {len(files)} 个文件，发现 {issues_found} 个文件有排版问题")
    if issues_found > 0 and not args.fix:
        print(f"{Fore.YELLOW}使用 --fix 参数可自动修正这些问题{Style.RESET_ALL}")
    print("="*50)
    
    return 0 if issues_found == 0 or args.fix else 1

if __name__ == "__main__":
    sys.exit(main()) 