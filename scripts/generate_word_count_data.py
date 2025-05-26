#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成字数统计数据文件供 Hugo 使用

功能：
1. 运行字数统计脚本
2. 生成 Hugo 数据文件（JSON 格式）
3. 格式化数字显示（万字单位）

使用方法：
python scripts/generate_word_count_data.py
"""

import json
import sys
from pathlib import Path
from word_count import WordCounter
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def format_word_count(count: int) -> str:
    """
    格式化字数显示
    
    Args:
        count: 字数
        
    Returns:
        格式化后的字符串（万字单位）
    """
    if count >= 10000:
        return f"{count / 10000:.1f}"
    else:
        return f"{count / 10000:.2f}"

def generate_hugo_data():
    """生成 Hugo 数据文件"""
    try:
        # 初始化字数统计器
        counter = WordCounter()
        
        # 处理所有文件
        logger.info("开始处理所有文件...")
        results = counter.process_all_files()
        
        # 生成统计摘要
        summary = counter.generate_summary(results)
        
        if not summary:
            logger.error("无法生成统计摘要")
            return False
        
        # 格式化数据
        hugo_data = {
            "total": {
                "word_count_formatted": format_word_count(summary['total']['total_words']),
                "word_count_raw": summary['total']['total_words'],
                "chinese_chars": summary['total']['chinese_chars'],
                "english_words": summary['total']['english_words'],
                "posts_count": summary['total']['posts_count'],
                "thoughts_count": summary['total']['thoughts_count']
            },
            "this_year": {
                "word_count_formatted": format_word_count(summary['this_year']['total_words']),
                "word_count_raw": summary['this_year']['total_words'],
                "chinese_chars": summary['this_year']['chinese_chars'],
                "english_words": summary['this_year']['english_words'],
                "posts_count": summary['this_year']['posts_count'],
                "thoughts_count": summary['this_year']['thoughts_count']
            },
            "posts": {
                "count": summary['posts']['count'],
                "word_count_formatted": format_word_count(summary['posts']['total_words']),
                "word_count_raw": summary['posts']['total_words'],
                "chinese_chars": summary['posts']['chinese_chars'],
                "english_words": summary['posts']['english_words']
            },
            "thoughts": {
                "count": summary['thoughts']['count'],
                "word_count_formatted": format_word_count(summary['thoughts']['total_words']),
                "word_count_raw": summary['thoughts']['total_words'],
                "chinese_chars": summary['thoughts']['chinese_chars'],
                "english_words": summary['thoughts']['english_words']
            },
            "generated_at": summary.get('generated_at', ''),
            "last_updated": "2025-05-26"  # 可以动态生成
        }
        
        # 确保 data 目录存在
        data_dir = Path(__file__).parent.parent / 'data'
        data_dir.mkdir(exist_ok=True)
        
        # 写入数据文件
        data_file = data_dir / 'word_count.json'
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(hugo_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"数据文件已生成: {data_file}")
        
        # 打印摘要
        print("\n=== 字数统计数据已生成 ===")
        print(f"总计: {hugo_data['total']['word_count_formatted']} 万字")
        print(f"今年: {hugo_data['this_year']['word_count_formatted']} 万字")
        print(f"数据文件: {data_file}")
        
        return True
        
    except Exception as e:
        logger.error(f"生成数据文件时出错: {e}")
        return False

def main():
    """主函数"""
    success = generate_hugo_data()
    if not success:
        sys.exit(1)

if __name__ == '__main__':
    main() 