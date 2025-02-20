import os
import re
import requests
from pathlib import Path
import sys

def download_image(url, save_path):
    try:
        # 清理 URL，移除可能的后缀
        url = url.split(']')[0]
        response = requests.get(url)
        response.raise_for_status()
        
        # 确保目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # 保存图片
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {save_path}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def process_markdown_file(file_path):
    # 读取 Markdown 文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取文章名称（不包含扩展名）
    article_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # 创建图片保存目录
    image_dir = f"static/images/posts/{article_name}"
    os.makedirs(image_dir, exist_ok=True)
    
    # 查找所有知乎图片链接（包括各种可能的格式）
    zhihu_links = []
    pattern = r'https://pic[0-9]\.zhimg\.com/[a-zA-Z0-9_]+_b\.[a-zA-Z]+'
    zhihu_links = re.findall(pattern, content)
    
    # 去重
    zhihu_links = list(set(zhihu_links))
    print(f"找到 {len(zhihu_links)} 个知乎图片链接")
    
    # 下载每个图片并更新链接
    successful_downloads = 0
    for i, url in enumerate(zhihu_links):
        print(f"\n处理第 {i+1}/{len(zhihu_links)} 个链接: {url}")
        # 构建保存路径
        save_path = os.path.join(image_dir, f"zhihu-image-{i+1}.jpg")
        if download_image(url, save_path):
            successful_downloads += 1
            # 更新 Markdown 中的图片链接
            # 找到包含此 URL 的整个图片引用
            old_pattern = f'!\\[.*?\\]\\({url}.*?\\)'
            new_link = f'![图片](/images/posts/{article_name}/zhihu-image-{i+1}.jpg)'
            content = re.sub(old_pattern, new_link, content)
    
    # 处理本地图片引用
    content = re.sub(
        r'!\[.*?\]\(%E6%9C%9D%E9%B2%9C%E5%9B%9B%E6%97%A5%E8%A1%8C%E7%BA%AA%E5%BD%95%205cf659918b1044b68cf256dbd42079b7/.*?\)',
        f'![图片](/images/posts/{article_name}/local-image.jpg)',
        content
    )
    
    # 移除 image-0.webp 的引用
    content = re.sub(r'!\[.*?\]\(/images/posts/[^)]+/image-0\.webp\)', '', content)
    
    # 保存更新后的 Markdown 文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n处理完成！")
    print(f"- 找到图片链接：{len(zhihu_links)} 个")
    print(f"- 成功下载：{successful_downloads} 个")
    print(f"- 保存目录：{image_dir}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python download_zhihu_images.py <markdown_file>")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    if not os.path.exists(markdown_file):
        print(f"File not found: {markdown_file}")
        sys.exit(1)
    
    process_markdown_file(markdown_file)

if __name__ == "__main__":
    main() 