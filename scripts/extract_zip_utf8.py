import os
import zipfile
import shutil
from pathlib import Path
import re
import jieba
import pypinyin
from datetime import datetime
import yaml

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
        "新昌": "xinchang",
        "一日": "one-day",
        "游": "trip",
        "碳水": "carbs",
        "美食": "food",
        "下岩贝": "xiayanbei",
        "村": "village",
        "回顾": "recap",
        "总结": "recap",
        "月": "month",
        "以前": "before",
        "超过": "over",
        "公里": "kilometers",
        "华南": "south-china",
        "自驾": "road-trip",
        "写一写感受": "review",
        "感受": "review",
        "朝鲜": "north-korea",
        "四日": "four-days",
        "行纪录": "journey",
        "行": "journey",
        "纪录": "record",
        "回忆": "recap",
        "玩具": "toys",
        "游记": "journey",
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
        "心得": "insights"
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
    # 移除空字符串和特殊字符
    english_words = [word for word in english_words if word and word not in ["s", "S"]]
    
    # 4. 组合成文件名
    filename = '-'.join(english_words).lower()
    
    # 5. 清理多余的短横线
    filename = re.sub(r'-+', '-', filename)  # 将多个连续的短横线替换为单个
    filename = filename.strip('-')  # 移除首尾的短横线
    
    return filename

def parse_notion_datetime(datetime_str):
    """解析 Notion 导出的日期时间字符串
    
    Args:
        datetime_str: Notion 格式的日期时间字符串，如 "November 13, 2024 8:17 PM"
    
    Returns:
        格式化的日期时间字符串，如 "2024-11-13T20:17:00+08:00"
    """
    try:
        # 解析 Notion 的日期时间格式
        dt = datetime.strptime(datetime_str, "%B %d, %Y %I:%M %p")
        # 返回格式化的字符串，添加北京时区
        return dt.strftime("%Y-%m-%dT%H:%M:00+08:00")
    except ValueError as e:
        print(f"警告：无法解析日期时间字符串 '{datetime_str}': {e}")
        return datetime.now().strftime("%Y-%m-%dT%H:%M:00+08:00")

def generate_frontmatter(title, description="", tags=None, created_time=None):
    """生成符合规范的 Front Matter
    
    Args:
        title: 文章标题
        description: 文章描述
        tags: 标签列表
        created_time: 文章创建时间
    
    Returns:
        格式化的 Front Matter 字符串
    """
    if tags is None:
        tags = []
    
    # 如果没有提供创建时间，使用当前时间
    if created_time is None:
        created_time = datetime.now().strftime("%Y-%m-%dT%H:%M:00+08:00")
    
    # 按照规范的顺序创建 frontmatter
    frontmatter = {
        "author": "Joe",
        "date": created_time,
        "description": description,
        "draft": False,
        "tags": tags,
        "title": title
    }
    
    # 使用 yaml 模块生成格式化的 Front Matter
    # default_style='\"' 确保字符串使用双引号
    # sort_keys=False 保持字段顺序
    return "---\n" + yaml.dump(frontmatter, 
                              allow_unicode=True,
                              default_flow_style=False,
                              sort_keys=False,
                              default_style='\"') + "---\n\n"

def extract_notion_metadata(content):
    """从 Notion 导出的内容中提取元数据
    
    Args:
        content: 原始文章内容
    
    Returns:
        (创建时间, 标签列表, 描述)的元组
    """
    created_time = None
    tags = []
    description = ""
    
    # 分割内容为行
    lines = content.split('\n')
    
    # 定义正则表达式
    created_pattern = re.compile(r'^Created(?:\stime)?:\s+(.+)$')
    tags_pattern = re.compile(r'^Tags:\s+(.+)$')
    
    # 提取第一段作为描述（跳过标题和元数据）
    content_started = False
    desc_lines = []
    
    for line in lines:
        line = line.strip()
        
        # 跳过空行
        if not line:
            continue
            
        # 检查创建时间
        created_match = created_pattern.match(line)
        if created_match:
            created_time = parse_notion_datetime(created_match.group(1))
            continue
            
        # 检查标签
        tags_match = tags_pattern.match(line)
        if tags_match:
            # 解析标签字符串
            tags_str = tags_match.group(1)
            # 移除可能的 Notion 链接格式
            tags_str = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', tags_str)
            # 分割标签
            tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
            continue
            
        # 提取描述（第一个非元数据、非标题的段落）
        if not content_started:
            if line.startswith('#'):  # 跳过标题
                continue
            if any(pattern.match(line) for pattern in [created_pattern, tags_pattern]):
                continue
            content_started = True
        
        if content_started and len(desc_lines) < 1:  # 只取第一段
            desc_lines.append(line)
    
    # 组合描述
    description = ' '.join(desc_lines) if desc_lines else ""
    
    return created_time, tags, description

def clean_notion_metadata(content):
    """清理 Notion 导出的元数据
    
    Args:
        content: 原始文章内容
    
    Returns:
        清理后的文章内容
    """
    # 分割内容为行
    lines = content.split('\n')
    
    # 跳过 Front Matter
    content_start = 0
    if lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                content_start = i + 1
                break
    
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
    for line in lines[content_start:]:
        # 检查是否匹配任何需要跳过的模式
        should_skip = any(pattern.match(line.strip()) for pattern in skip_patterns)
        if not should_skip:
            cleaned_lines.append(line)
    
    # 重新组合内容
    if content_start > 0:
        # 保留原始的 Front Matter
        cleaned_content = '\n'.join(lines[:content_start] + cleaned_lines)
    else:
        cleaned_content = '\n'.join(cleaned_lines)
    
    # 移除多余的空行
    cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)
    
    return cleaned_content.strip() + '\n'

def process_content(content, article_name):
    """处理文章内容，移除重复标题和处理链接
    
    Args:
        content: 原始文章内容
        article_name: 文章英文名称
    
    Returns:
        处理后的文章内容
    """
    # 首先提取元数据
    created_time, tags, description = extract_notion_metadata(content)
    
    # 清理 Notion 元数据
    content = clean_notion_metadata(content)
    
    lines = content.split('\n')
    
    # 移除开头的标题（# 开头的行）
    if lines and lines[0].strip().startswith('# '):
        title = lines[0].strip('#').strip()
        lines = lines[1:]
    else:
        title = article_name.replace('-', ' ').title()
    
    # 处理 Notion 链接
    processed_lines = []
    for line in lines:
        # 1. 替换 Notion 链接为内部链接
        line = re.sub(
            r'\[([^\]]+)\]\(https://www\.notion\.so/[^)]+\)',
            lambda m: f'[{m.group(1)}](/posts/{convert_to_english_name(m.group(1))})',
            line
        )
        
        # 2. 移除 Notion 页面 ID
        line = re.sub(r'\?pvs=\d+', '', line)
        
        processed_lines.append(line)
    
    # 生成新的 Front Matter
    front_matter = generate_frontmatter(
        title=title,
        description=description,
        tags=tags,
        created_time=created_time
    )
    
    # 组合最终内容
    content = front_matter + '\n'.join(processed_lines)
    
    # 确保段落之间有正确的空行
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip() + '\n'

def process_image_links(content, article_name):
    """处理文章中的图片链接为统一格式
    
    Args:
        content: 文章内容
        article_name: 文章英文名称
    
    Returns:
        处理后的文章内容
    """
    # 替换图片链接
    # 1. 替换完整的 Notion 图片路径
    content = re.sub(
        r'!\[(.*?)\]\((.*?)(?:Untitled.*?\.png|.*?\.(png|jpg|jpeg|gif))\)',
        lambda m: f'![{m.group(1)}](/images/posts/{article_name}/image-{abs(hash(m.group(2)))%100}.webp)',
        content
    )
    
    # 2. 替换相对路径的图片链接
    content = re.sub(
        r'!\[(.*?)\]\((?!http|/)(.*?)(?:Untitled.*?\.png|.*?\.(png|jpg|jpeg|gif))\)',
        lambda m: f'![{m.group(1)}](/images/posts/{article_name}/image-{abs(hash(m.group(2)))%100}.webp)',
        content
    )
    
    return content

def main():
    """主函数，处理 Notion 导出的 ZIP 文件"""
    # 创建临时目录
    temp_dir = Path('temp_notion')
    temp_dir.mkdir(exist_ok=True)
    
    # 查找 draftfiles 目录中的 ZIP 文件
    zip_files = list(Path('draftfiles').glob('*.zip'))
    
    for zip_path in zip_files:
        print(f"正在解压文件: {zip_path}")
        
        # 解压 ZIP 文件
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # 获取所有 Markdown 文件
            markdown_files = [f for f in zip_ref.namelist() if f.endswith('.md')]
            
            for md_file in markdown_files:
                # 解码文件名（处理中文）
                try:
                    # 尝试使用 UTF-8 解码
                    decoded_name = md_file.encode('cp437').decode('utf-8')
                except UnicodeEncodeError:
                    # 如果失败，假设文件名已经是 UTF-8
                    decoded_name = md_file
                except Exception as e:
                    print(f"警告：无法解码文件名 '{md_file}': {e}")
                    continue
                
                print(f"                            成功提取: {decoded_name}")
                
                # 读取文件内容
                try:
                    content = zip_ref.read(md_file).decode('utf-8')
                except UnicodeDecodeError:
                    try:
                        content = zip_ref.read(md_file).decode('gbk')
                    except UnicodeDecodeError:
                        print(f"错误：无法解码文件内容 '{decoded_name}'")
                        continue
                
                # 获取文章标题（移除扩展名和可能的 Notion ID）
                article_title = re.sub(r'\s+[a-f0-9]{32}$', '', 
                                     Path(decoded_name).stem)
                
                # 转换为英文文件名
                article_name = convert_to_english_name(article_title)
                print(f"\n处理文章: {article_title} -> {article_name}")
                
                # 处理文章内容
                content = process_content(content, article_name)
                content = process_image_links(content, article_name)
                
                # 保存处理后的文件
                output_path = temp_dir / f"{article_name}.md"
                output_path.write_text(content, encoding='utf-8')
    
    print("\n解压和基础处理完成！")
    print("\n后续步骤：")
    print("1. 为文章创建图片目录")
    print("2. 手动处理图片（复制、重命名、压缩）")
    print("3. 添加文章元数据")
    print("4. 清理临时文件")

if __name__ == '__main__':
    main() 