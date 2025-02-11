import os
import zipfile
import shutil
from pathlib import Path
import subprocess
import glob
from datetime import datetime
import re
import jieba
import pypinyin

def convert_to_english_name(chinese_title):
    """将中文标题转换为规范的英文文件名
    
    Args:
        chinese_title: 中文标题
    
    Returns:
        符合规范的英文文件名：
        1. 使用英文单词
        2. 单词之间用短横线连接
        3. 全部小写
        4. 避免特殊字符
    """
    # 预定义的中文词语映射表
    word_mapping = {
        "朝鲜": "north-korea",
        "四日": "four-days",
        "行纪录": "journey",
        "行": "journey",
        "纪录": "record",
        "回忆": "recap",
        "玩具": "toys",
        "游记": "journey",
        "总结": "summary",
        "日记": "diary",
        "体验": "experience",
        "评测": "review",
        "教程": "tutorial",
        "指南": "guide",
        "旅行": "travel",
        "游记": "travel-notes",
        "记录": "record",
        "探索": "explore",
        "观察": "observation",
        "思考": "thoughts",
        "分享": "sharing",
        "生活": "life",
        "工作": "work",
        "学习": "study",
        "随笔": "essay",
        "札记": "notes",
        "小记": "notes",
        "笔记": "notes",
        "感想": "thoughts",
        "心得": "insights",
        # 可以继续添加更多映射
    }
    
    # 1. 分词
    words = jieba.cut(chinese_title)
    
    # 2. 转换每个词
    english_words = []
    for word in words:
        # 检查是否在映射表中
        if word in word_mapping:
            english_words.append(word_mapping[word])
        else:
            # 如果不在映射表中，转换为拼音
            pinyin = pypinyin.lazy_pinyin(word)
            english_words.extend(pinyin)
    
    # 3. 处理英文单词
    # 移除所有非字母数字的字符
    english_words = [re.sub(r'[^a-zA-Z0-9]', '', word) for word in english_words]
    # 移除空字符串
    english_words = [word for word in english_words if word]
    
    # 4. 组合成文件名
    filename = '-'.join(english_words).lower()
    
    # 5. 清理多余的短横线
    filename = re.sub(r'-+', '-', filename)  # 将多个连续的短横线替换为单个
    filename = filename.strip('-')  # 移除首尾的短横线
    
    return filename

def extract_zip_utf8(zip_path="Notionfiles"):
    """解压并处理 Notion 导出的 ZIP 文件
    
    Args:
        zip_path: ZIP 文件所在目录
    """
    # 创建临时目录
    temp_dir = "temp_notion"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # 查找 ZIP 文件
    zip_files = [f for f in os.listdir(zip_path) if f.endswith('.zip')]
    if not zip_files:
        print("未找到 ZIP 文件")
        return
    
    for zip_file in zip_files:
        full_path = os.path.join(zip_path, zip_file)
        print(f"正在解压文件: {full_path}")
        
        try:
            with zipfile.ZipFile(full_path, 'r') as zip_ref:
                # 解压所有文件
                for file_info in zip_ref.filelist:
                    try:
                        # 使用 CP437 编码处理文件名
                        file_name = file_info.filename.encode('cp437').decode('utf-8')
                    except:
                        # 如果转换失败，尝试直接使用原始文件名
                        file_name = file_info.filename
                    
                    # 创建目标路径
                    target_path = os.path.join(temp_dir, file_name)
                    
                    # 确保目标目录存在
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    
                    # 解压文件
                    try:
                        source = zip_ref.open(file_info)
                        target = open(target_path, "wb")
                        with source, target:
                            shutil.copyfileobj(source, target)
                        print(f"成功提取: {file_name}")
                    except Exception as e:
                        print(f"提取文件失败: {file_name}")
                        print(f"错误信息: {str(e)}")
                        continue
                
                # 处理所有 Markdown 文件
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        if file.endswith('.md'):
                            md_path = os.path.join(root, file)
                            
                            # 读取文件内容以获取标题
                            try:
                                with open(md_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    # 查找标题（# 开头的第一行）
                                    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                                    if title_match:
                                        title = title_match.group(1)
                                    else:
                                        # 如果找不到标题，使用文件名
                                        title = os.path.splitext(file)[0]
                            except Exception as e:
                                print(f"读取文件失败: {str(e)}")
                                title = os.path.splitext(file)[0]
                            
                            # 生成规范的英文文件名
                            article_name = convert_to_english_name(title)
                            
                            print(f"\n处理文章: {title} -> {article_name}")
                            # 调用 process_notion_links.py 处理文章
                            try:
                                subprocess.run(['python', 'process_notion_links.py', 
                                             article_name, '--input', md_path], 
                                             check=True)
                            except subprocess.CalledProcessError as e:
                                print(f"处理文章失败: {str(e)}")
                                continue
        
        except Exception as e:
            print(f"处理 ZIP 文件时出错: {str(e)}")
            continue
    
    print("\n解压和基础处理完成！")

if __name__ == "__main__":
    extract_zip_utf8() 