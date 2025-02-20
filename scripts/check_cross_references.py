#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from collections import defaultdict
import sys

def get_all_posts():
    """获取所有博客文章的文件名（不含扩展名）"""
    posts_dir = "content/posts"
    posts = []
    for file in os.listdir(posts_dir):
        if file.endswith(".md"):
            posts.append(os.path.splitext(file)[0])
    return posts

def find_references(file_path, all_posts):
    """在单个文件中查找所有引用"""
    references = []
    notion_references = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 查找内部链接引用 /posts/xxx
    internal_refs = re.finditer(r'\[([^\]]+)\]\(/posts/([^)]+)\)', content)
    for ref in internal_refs:
        link_text = ref.group(1)
        link_target = ref.group(2)
        references.append({
            'type': 'internal',
            'text': link_text,
            'target': link_target
        })
    
    # 查找 Notion 链接
    notion_refs = re.finditer(r'\[([^\]]+)\]\(https://(?:www\.)?notion\.so/[^)]+\)', content)
    for ref in notion_refs:
        link_text = ref.group(1)
        link_target = ref.group(0)
        notion_references.append({
            'type': 'notion',
            'text': link_text,
            'target': link_target
        })
    
    return references, notion_references

def check_references():
    """检查所有博客文章的引用"""
    posts = get_all_posts()
    posts_dir = "content/posts"
    
    # 存储所有引用信息
    all_references = defaultdict(list)
    all_notion_refs = defaultdict(list)
    broken_links = defaultdict(list)
    
    # 遍历所有文章
    for post in posts:
        file_path = os.path.join(posts_dir, f"{post}.md")
        refs, notion_refs = find_references(file_path, posts)
        
        # 检查内部链接
        for ref in refs:
            all_references[post].append(ref)
            # 检查链接目标是否存在
            if ref['target'] not in posts:
                broken_links[post].append(ref)
        
        # 记录 Notion 链接
        for ref in notion_refs:
            all_notion_refs[post].append(ref)
    
    # 打印报告
    print("\n=== 博客交叉引用检查报告 ===\n")
    
    # 1. 打印内部链接统计
    print("1. 内部链接统计：")
    for post, refs in all_references.items():
        if refs:
            print(f"\n文章 '{post}.md' 包含 {len(refs)} 个内部链接：")
            for ref in refs:
                print(f"  - [{ref['text']}] -> /posts/{ref['target']}")
    
    # 2. 打印损坏的链接
    if broken_links:
        print("\n2. 发现损坏的链接：")
        for post, refs in broken_links.items():
            print(f"\n文章 '{post}.md' 中的损坏链接：")
            for ref in refs:
                print(f"  - [{ref['text']}] -> /posts/{ref['target']} (目标不存在)")
    else:
        print("\n2. 未发现损坏的链接！")
    
    # 3. 打印 Notion 链接
    if all_notion_refs:
        print("\n3. 发现 Notion 链接（建议替换为内部链接）：")
        for post, refs in all_notion_refs.items():
            print(f"\n文章 '{post}.md' 中的 Notion 链接：")
            for ref in refs:
                print(f"  - [{ref['text']}] -> {ref['target']}")
    else:
        print("\n3. 未发现 Notion 链接！")

if __name__ == "__main__":
    check_references() 