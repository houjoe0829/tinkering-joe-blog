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

def generate_frontmatter(title, description="", tags=None):
    """生成符合规范的 Front Matter
    
    Args:
        title: 文章标题
        description: 文章描述
        tags: 标签列表
    
    Returns:
        格式化的 Front Matter 字符串
    """
    if tags is None:
        tags = []
    
    # 按照规范的顺序创建 frontmatter
    frontmatter = {
        "author": "Joe",
        "date": datetime.now().strftime("%Y-%m-%d"),
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
    # 首先清理 Notion 元数据
    content = clean_notion_metadata(content)
    
    lines = content.split('\n')
    
    # 移除开头的标题（# 开头的行）
    if lines and lines[0].strip().startswith('# '):
        lines = lines[1:]
    
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
    
    # 确保段落之间有正确的空行
    content = '\n'.join(processed_lines).strip()
    return content + '\n'

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

def extract_zip_utf8(zip_path="draftfiles"):
    """解压 Notion 导出的 ZIP 文件并进行基础处理
    
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
                            
                            # 读取文件内容
                            try:
                                with open(md_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    
                                    # 提取标题
                                    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                                    if title_match:
                                        title = title_match.group(1)
                                    else:
                                        title = os.path.splitext(file)[0]
                                    
                                    # 提取描述（第一段非空文本）
                                    description = ""
                                    for line in content.split('\n'):
                                        line = line.strip()
                                        if line and not line.startswith('#'):
                                            description = line
                                            break
                                    
                                    # 生成英文文件名
                                    article_name = convert_to_english_name(title)
                                    
                                    # 处理文章内容（移除重复标题和处理链接）
                                    processed_content = process_content(content, article_name)
                                    
                                    # 处理图片链接
                                    processed_content = process_image_links(processed_content, article_name)
                                    
                                    # 生成 Front Matter
                                    front_matter = generate_frontmatter(
                                        title=title,
                                        description=description,
                                        tags=[]  # 这里可以添加标签提取逻辑
                                    )
                                    
                                    # 组合最终内容
                                    final_content = front_matter + processed_content
                                    
                                    # 保存处理后的文件
                                    output_path = f"temp_notion/{article_name}.md"
                                    with open(output_path, 'w', encoding='utf-8') as f:
                                        f.write(final_content)
                                    
                                    print(f"\n处理文章: {title} -> {article_name}")
                                    
                            except Exception as e:
                                print(f"处理文件失败: {str(e)}")
                                continue
        
        except Exception as e:
            print(f"处理 ZIP 文件时出错: {str(e)}")
            continue
    
    print("\n解压和基础处理完成！")
    print("\n后续步骤：")
    print("1. 为文章创建图片目录")
    print("2. 手动处理图片（复制、重命名、压缩）")
    print("3. 添加文章元数据")
    print("4. 清理临时文件")

if __name__ == "__main__":
    extract_zip_utf8() 