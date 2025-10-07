#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检查博客文章标签的脚本
功能：
1. 检查所有博文的标签是否都在预定义的标签列表中
2. 统计每个标签的使用次数
3. 检查是否有未使用的预定义标签
4. 输出详细的检查报告
"""

import os
import re
import yaml
from collections import Counter, defaultdict
from typing import Set, List, Dict, Tuple

# 预定义的标签列表
VALID_TAGS = {
    "书影音的精神角落",  # 看书、看影视剧的记录
    "我有个想法！",      # 生活或工作上的灵感
    "江浙沪包游",       # 江浙沪地区的旅行记录
    "提升幸福感的好物",  # 包括软件和硬件提升幸福感的内容
    "折腾软硬件",       # 软件和数码硬件相关的折腾
    "游戏也是场冒险",    # 游戏体验记录
    "小城故事",         # 老家的故事
    "阅读笔记",         # 书籍或文章阅读的笔记
    "现实是个开放世界",  # 所有地方的旅行日记（包括江浙沪地区）
    "工作感悟",         # 工作相关的总结
    "生活感悟",         # 生活相关的感悟
    "4+2 骑行中",       # 骑行相关的内容
    "AI 相关",          # 与 AI 相关的内容
    "Vibe Coding",     # 与 AI 编程相关的感悟
    "博客功能更新",     # 博客功能的更新记录
}

class TagChecker:
    def __init__(self, posts_dir: str):
        self.posts_dir = posts_dir
        self.tag_usage = Counter()  # 统计每个标签的使用次数
        self.invalid_tags = defaultdict(set)  # 记录每个文件中的无效标签
        self.files_without_tags = []  # 记录没有标签的文件
        self.files_with_empty_tags = []  # 记录标签为空的文件

    def extract_front_matter(self, content: str) -> dict:
        """从文件内容中提取 front matter"""
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(pattern, content, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except yaml.YAMLError:
                return {}
        return {}

    def check_file(self, file_path: str) -> None:
        """检查单个文件的标签"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            front_matter = self.extract_front_matter(content)
            if not front_matter:
                self.files_without_tags.append(file_path)
                return

            tags = front_matter.get('tags', [])
            if not tags:
                self.files_with_empty_tags.append(file_path)
                return

            # 检查每个标签
            for tag in tags:
                if tag in VALID_TAGS:
                    self.tag_usage[tag] += 1
                else:
                    self.invalid_tags[file_path].add(tag)

        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {str(e)}")

    def check_all_files(self) -> None:
        """检查所有博文文件"""
        for file_name in os.listdir(self.posts_dir):
            if file_name.endswith('.md'):
                file_path = os.path.join(self.posts_dir, file_name)
                self.check_file(file_path)

    def generate_report(self) -> str:
        """生成检查报告"""
        report = []
        report.append("# 博客标签检查报告\n")

        # 1. 标签使用统计
        report.append("## 标签使用统计")
        for tag in sorted(VALID_TAGS):
            count = self.tag_usage[tag]
            report.append(f"- {tag}: {count} 次")
        report.append("")

        # 2. 未使用的标签
        unused_tags = VALID_TAGS - set(self.tag_usage.keys())
        if unused_tags:
            report.append("## 未使用的标签")
            for tag in sorted(unused_tags):
                report.append(f"- {tag}")
            report.append("")

        # 3. 无效标签
        if self.invalid_tags:
            report.append("## 包含无效标签的文件")
            for file_path, tags in sorted(self.invalid_tags.items()):
                file_name = os.path.basename(file_path)
                report.append(f"- {file_name}")
                for tag in sorted(tags):
                    report.append(f"  - {tag}")
            report.append("")

        # 4. 没有标签的文件
        if self.files_without_tags:
            report.append("## 缺少 Front Matter 的文件")
            for file_path in sorted(self.files_without_tags):
                report.append(f"- {os.path.basename(file_path)}")
            report.append("")

        # 5. 标签为空的文件
        if self.files_with_empty_tags:
            report.append("## 标签为空的文件")
            for file_path in sorted(self.files_with_empty_tags):
                report.append(f"- {os.path.basename(file_path)}")
            report.append("")

        return "\n".join(report)

def main():
    # 设置博文目录路径（包括 posts 和 thoughts）
    content_dirs = ["content/posts", "content/thoughts"]
    
    # 创建检查器实例
    checker = TagChecker(content_dirs[0])
    
    # 检查所有内容目录
    for content_dir in content_dirs:
        checker.posts_dir = content_dir
        checker.check_all_files()
    
    # 生成并打印报告
    report = checker.generate_report()
    print(report)

    # 如果有任何问题，返回非零状态码
    has_issues = bool(
        checker.invalid_tags or 
        checker.files_without_tags or 
        checker.files_with_empty_tags
    )
    exit(1 if has_issues else 0)

if __name__ == "__main__":
    main() 