#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
博客内容字数统计脚本

功能：
1. 解析 Markdown 文件内容
2. 清理文本（排除 Markdown 语法、链接 URL、Front matter 等）
3. 分别统计中文字符数和英文单词数
4. 将字数信息写入文章的 Front matter

使用方法：
python scripts/word_count.py [--file FILE] [--update] [--dry-run]
"""

import os
import re
import sys
import argparse
import frontmatter
from pathlib import Path
from typing import Dict, Tuple, List
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WordCounter:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.content_dirs = ['content/posts', 'content/thoughts']
        
    def clean_markdown_content(self, content: str) -> str:
        """
        清理 Markdown 内容，移除语法标记但保留实际文本内容
        
        Args:
            content: 原始 Markdown 内容
            
        Returns:
            清理后的纯文本内容
        """
        # 移除 Front matter（已经在 frontmatter 库中处理）
        
        # 保留代码块内容，但移除代码块标记
        # 匹配 ```language 和 ``` 包围的代码块
        content = re.sub(r'```[\w]*\n(.*?)\n```', r'\1', content, flags=re.DOTALL)
        # 匹配行内代码 `code`
        content = re.sub(r'`([^`]+)`', r'\1', content)
        
        # 处理链接：保留链接文本，移除 URL
        # [文本](URL) -> 文本
        content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
        # [文本][ref] -> 文本
        content = re.sub(r'\[([^\]]+)\]\[[^\]]*\]', r'\1', content)
        # 移除链接引用定义行
        content = re.sub(r'^\s*\[[^\]]+\]:\s*.*$', '', content, flags=re.MULTILINE)
        
        # 处理图片：保留 Alt 文本
        # ![alt](url) -> alt
        content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', content)
        
        # 移除 Markdown 语法标记
        # 标题标记
        content = re.sub(r'^#{1,6}\s+', '', content, flags=re.MULTILINE)
        # 粗体和斜体
        content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)  # **粗体**
        content = re.sub(r'\*([^*]+)\*', r'\1', content)      # *斜体*
        content = re.sub(r'__([^_]+)__', r'\1', content)      # __粗体__
        content = re.sub(r'_([^_]+)_', r'\1', content)        # _斜体_
        # 删除线
        content = re.sub(r'~~([^~]+)~~', r'\1', content)
        
        # 移除引用标记
        content = re.sub(r'^>\s*', '', content, flags=re.MULTILINE)
        
        # 移除列表标记
        content = re.sub(r'^\s*[-*+]\s+', '', content, flags=re.MULTILINE)  # 无序列表
        content = re.sub(r'^\s*\d+\.\s+', '', content, flags=re.MULTILINE)  # 有序列表
        
        # 移除水平分割线
        content = re.sub(r'^[-*_]{3,}$', '', content, flags=re.MULTILINE)
        
        # 移除 HTML 标签
        content = re.sub(r'<[^>]+>', '', content)
        
        # 移除 Hugo shortcodes
        content = re.sub(r'\{\{<[^>]*>\}\}', '', content)
        content = re.sub(r'\{\{%[^%]*%\}\}', '', content)
        
        # 移除多余的空白字符，但保留换行
        content = re.sub(r'[ \t]+', ' ', content)  # 多个空格/制表符合并为一个空格
        content = re.sub(r'\n\s*\n', '\n\n', content)  # 多个连续换行合并为两个换行
        
        return content.strip()
    
    def count_words(self, content: str) -> Tuple[int, int]:
        """
        统计中文字符数和英文单词数
        
        Args:
            content: 清理后的文本内容
            
        Returns:
            (中文字符数, 英文单词数)
        """
        # 统计中文字符（包括中文标点符号）
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', content))
        
        # 移除中文字符后统计英文单词
        content_without_chinese = re.sub(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', ' ', content)
        # 按空格分割并过滤空字符串
        english_words = len([word for word in re.split(r'\s+', content_without_chinese) if word.strip()])
        
        return chinese_chars, english_words
    
    def process_file(self, file_path: Path) -> Dict:
        """
        处理单个 Markdown 文件
        
        Args:
            file_path: 文件路径
            
        Returns:
            包含统计信息的字典
        """
        try:
            # 读取文件
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            # 清理内容
            cleaned_content = self.clean_markdown_content(post.content)
            
            # 统计字数
            chinese_chars, english_words = self.count_words(cleaned_content)
            
            # 计算总字数（中文字符 + 英文单词）
            total_words = chinese_chars + english_words
            
            result = {
                'file': str(file_path),
                'chinese_chars': chinese_chars,
                'english_words': english_words,
                'total_words': total_words,
                'date': post.metadata.get('date'),
                'title': post.metadata.get('title', ''),
                'section': self.get_section_from_path(file_path)
            }
            
            logger.info(f"处理文件: {file_path.name} - 中文: {chinese_chars}, 英文: {english_words}, 总计: {total_words}")
            
            return result
            
        except Exception as e:
            logger.error(f"处理文件 {file_path} 时出错: {e}")
            return None
    
    def get_section_from_path(self, file_path: Path) -> str:
        """从文件路径获取内容类型"""
        path_parts = file_path.parts
        if 'posts' in path_parts:
            return 'posts'
        elif 'thoughts' in path_parts:
            return 'thoughts'
        else:
            return 'unknown'
    
    def update_frontmatter(self, file_path: Path, word_count_data: Dict) -> bool:
        """
        更新文件的 Front matter，添加字数统计信息
        
        Args:
            file_path: 文件路径
            word_count_data: 字数统计数据
            
        Returns:
            是否成功更新
        """
        try:
            # 读取文件
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            # 更新字数信息
            post.metadata['word_count'] = {
                'chinese_chars': word_count_data['chinese_chars'],
                'english_words': word_count_data['english_words'],
                'total_words': word_count_data['total_words']
            }
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                frontmatter.dump(post, f, default_flow_style=False, allow_unicode=True)
            
            logger.info(f"已更新 {file_path.name} 的字数统计信息")
            return True
            
        except Exception as e:
            logger.error(f"更新文件 {file_path} 的 Front matter 时出错: {e}")
            return False
    
    def get_all_markdown_files(self) -> List[Path]:
        """获取所有需要处理的 Markdown 文件"""
        files = []
        for content_dir in self.content_dirs:
            dir_path = self.project_root / content_dir
            if dir_path.exists():
                files.extend(dir_path.glob('*.md'))
        return files
    
    def process_all_files(self, update_frontmatter: bool = False, dry_run: bool = False) -> List[Dict]:
        """
        处理所有 Markdown 文件
        
        Args:
            update_frontmatter: 是否更新 Front matter
            dry_run: 是否为试运行（不实际修改文件）
            
        Returns:
            所有文件的统计结果列表
        """
        files = self.get_all_markdown_files()
        results = []
        
        logger.info(f"找到 {len(files)} 个 Markdown 文件")
        
        for file_path in files:
            result = self.process_file(file_path)
            if result:
                results.append(result)
                
                # 更新 Front matter
                if update_frontmatter and not dry_run:
                    self.update_frontmatter(file_path, result)
                elif update_frontmatter and dry_run:
                    logger.info(f"[试运行] 将更新 {file_path.name} 的字数统计信息")
        
        return results
    
    def generate_summary(self, results: List[Dict]) -> Dict:
        """生成统计摘要"""
        if not results:
            return {}
        
        # 按类型分组统计
        posts_stats = [r for r in results if r['section'] == 'posts']
        thoughts_stats = [r for r in results if r['section'] == 'thoughts']
        
        # 计算总计
        total_chinese = sum(r['chinese_chars'] for r in results)
        total_english = sum(r['english_words'] for r in results)
        total_words = sum(r['total_words'] for r in results)
        
        # 计算各类型统计
        posts_chinese = sum(r['chinese_chars'] for r in posts_stats)
        posts_english = sum(r['english_words'] for r in posts_stats)
        posts_total = sum(r['total_words'] for r in posts_stats)
        
        thoughts_chinese = sum(r['chinese_chars'] for r in thoughts_stats)
        thoughts_english = sum(r['english_words'] for r in thoughts_stats)
        thoughts_total = sum(r['total_words'] for r in thoughts_stats)
        
        # 按年份统计（今年）
        from datetime import datetime
        current_year = datetime.now().year
        this_year_results = []
        
        for r in results:
            if r['date']:
                try:
                    # 处理不同的日期格式
                    date_str = str(r['date'])
                    if 'T' in date_str:
                        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                    else:
                        date_obj = datetime.strptime(date_str[:10], '%Y-%m-%d')
                    
                    if date_obj.year == current_year:
                        this_year_results.append(r)
                except Exception as e:
                    logger.warning(f"解析日期失败: {r['date']} - {e}")
        
        this_year_chinese = sum(r['chinese_chars'] for r in this_year_results)
        this_year_english = sum(r['english_words'] for r in this_year_results)
        this_year_total = sum(r['total_words'] for r in this_year_results)
        
        this_year_posts = [r for r in this_year_results if r['section'] == 'posts']
        this_year_thoughts = [r for r in this_year_results if r['section'] == 'thoughts']
        
        summary = {
            'total': {
                'files': len(results),
                'chinese_chars': total_chinese,
                'english_words': total_english,
                'total_words': total_words,
                'posts_count': len(posts_stats),
                'thoughts_count': len(thoughts_stats)
            },
            'posts': {
                'count': len(posts_stats),
                'chinese_chars': posts_chinese,
                'english_words': posts_english,
                'total_words': posts_total
            },
            'thoughts': {
                'count': len(thoughts_stats),
                'chinese_chars': thoughts_chinese,
                'english_words': thoughts_english,
                'total_words': thoughts_total
            },
            'this_year': {
                'files': len(this_year_results),
                'chinese_chars': this_year_chinese,
                'english_words': this_year_english,
                'total_words': this_year_total,
                'posts_count': len(this_year_posts),
                'thoughts_count': len(this_year_thoughts)
            }
        }
        
        return summary

def main():
    parser = argparse.ArgumentParser(description='博客内容字数统计工具')
    parser.add_argument('--file', type=str, help='处理单个文件')
    parser.add_argument('--update', action='store_true', help='更新文件的 Front matter')
    parser.add_argument('--dry-run', action='store_true', help='试运行，不实际修改文件')
    
    args = parser.parse_args()
    
    counter = WordCounter()
    
    if args.file:
        # 处理单个文件
        file_path = Path(args.file)
        if not file_path.exists():
            logger.error(f"文件不存在: {file_path}")
            sys.exit(1)
        
        result = counter.process_file(file_path)
        if result:
            print(f"\n文件: {result['file']}")
            print(f"中文字符: {result['chinese_chars']}")
            print(f"英文单词: {result['english_words']}")
            print(f"总字数: {result['total_words']}")
            
            if args.update and not args.dry_run:
                counter.update_frontmatter(file_path, result)
            elif args.update and args.dry_run:
                print("[试运行] 将更新文件的字数统计信息")
    else:
        # 处理所有文件
        results = counter.process_all_files(args.update, args.dry_run)
        summary = counter.generate_summary(results)
        
        if summary:
            print("\n=== 字数统计摘要 ===")
            print(f"总计: {summary['total']['total_words']:,} 字 (中文: {summary['total']['chinese_chars']:,}, 英文: {summary['total']['english_words']:,})")
            print(f"博文: {summary['posts']['count']} 篇, {summary['posts']['total_words']:,} 字")
            print(f"随思录: {summary['thoughts']['count']} 条, {summary['thoughts']['total_words']:,} 字")
            print(f"今年: {summary['this_year']['total_words']:,} 字 (博文: {summary['this_year']['posts_count']} 篇, 随思录: {summary['this_year']['thoughts_count']} 条)")
            print(f"今年约 {summary['this_year']['total_words'] / 10000:.1f} 万字")

if __name__ == '__main__':
    main() 