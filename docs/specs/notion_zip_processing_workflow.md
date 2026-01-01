# Notion ZIP 文件处理工作流程

## 概述

本文档定义了从 Notion 导出的 ZIP 压缩包转换为博客文章的标准化处理流程。该流程涵盖了文件解压、内容转换、图片处理、格式规范化和清理等完整环节，确保 Notion 内容能够无缝集成到 Hugo 博客系统中。

## 适用范围

- 博客文章（posts）：放置在 `content/posts/` 目录
- 随思录（thoughts）：放置在 `content/thoughts/` 目录
- 支持包含图片附件的 Notion 导出内容

## 前置条件

### 环境要求
- Python 3.x 环境
- ImageMagick 工具（图片处理）
- 项目根目录下的处理脚本

### 文件准备
- Notion ZIP 文件已放置在 `temp_files/` 目录下
- 确保 ZIP 文件是唯一的待处理文件

## 标准处理流程

### 1. 文件解压阶段

#### 1.1 自动扫描和解压
```bash
# AI 助手会自动扫描 temp_files 目录，找出唯一的 ZIP 文件
python3 scripts/extract_zip_utf8.py temp_files/[ZIP文件名].zip
```

#### 1.2 解压结果
- 内容解压到：`temp_notion/` 目录（Markdown 文件和图片平铺在根目录）
- 通常包含：主 Markdown 文件 + 图片文件

### 2. 图片迁移阶段（在创建文章之前）

> **重要**：必须先将图片复制到目标目录，再创建文章文件。这是因为图片压缩脚本需要从 `static/images/` 目录读取原始图片。

#### 2.1 创建图片目录并复制图片
```bash
# 博客文章
mkdir -p static/images/posts/[article-name]
cp temp_notion/*.png temp_notion/*.jpg temp_notion/*.jpeg static/images/posts/[article-name]/ 2>/dev/null

# 随思录
mkdir -p static/images/thoughts/[thought-name]
cp temp_notion/*.png temp_notion/*.jpg temp_notion/*.jpeg static/images/thoughts/[thought-name]/ 2>/dev/null
```

### 3. 内容创建阶段

#### 3.1 确定文章信息
- 确认主 Markdown 文件（在 `temp_notion/` 中）
- 确定文章标题
- 确定内容类型（posts 或 thoughts）
- 确定英文文件名

#### 3.2 创建目标文件
**博客文章**：
- 位置：`content/posts/[英文文件名].md`
- 命名规范：英文单词，短横线分隔，避免拼音

**随思录**：
- 位置：`content/thoughts/[英文文件名].md`
- 命名规范：同博客文章

#### 3.3 图片引用格式
在创建文章时，可以直接使用相对路径引用图片（如 `![alt](filename.png)`），`update_image_refs.py` 脚本会自动将其转换为正确的绝对路径格式。

### 4. 元数据配置阶段

#### 4.1 Front Matter 结构
```yaml
---
author: "Joe"
date: YYYY-MM-DD  # 使用 `date +%Y-%m-%d` 获取当前日期
description: "文章简短描述"
draft: false
tags: ["标签1", "标签2"]  # 必须从预定义标签列表选择
title: "文章标题"  # thoughts 类型可以留空 ""
---
```

#### 4.2 元数据规范
- **YAML 敏感性**：使用纯英文引号包裹值
- **标点符号**：统一使用半角标点
- **标签限制**：只能从预定义标签列表中选择
- **参考模板**：以 `@nezha-movie-review.md` 为格式参考

### 5. 内容转换阶段

#### 5.1 正文内容处理
- 复制 Notion Markdown 正文到目标文件
- 移除或转换 Notion 内部链接（转换为博客内部链接格式 `/posts/article-name`）
- 调整 Callout、Toggle 等 Notion 特有块格式
- 清理不必要的 HTML 标签或样式

#### 5.2 图片 Caption 处理
当 Notion 导出包含图片 Caption 时，使用以下 HTML 格式：
```html
<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>Caption 文案内容</em>
</div>
```

#### 5.3 图片尺寸调整
如需调整图片显示尺寸（如 50% 宽度并居中），使用以下格式：
```html
<img src="/images/posts/article-name/image.webp" alt="描述" style="width: 50%; display: block; margin: 0 auto;" />
```

### 6. 图片处理阶段

#### 6.1 图片处理命令序列

**博客文章处理**：
```bash
# 1. 压缩并转换图片为 WebP 格式（图片必须已在 static/images/posts/article-name/ 中）
python3 scripts/compress_article_images.py content/posts/article-name.md

# 2. 移动压缩后的图片到正确位置（覆盖原始图片目录）
cp -r static/images_compressed/posts/article-name/* static/images/posts/article-name/

# 3. 更新图片引用（自动将相对路径转为绝对路径，并更新扩展名为 .webp）
python3 scripts/update_image_refs.py

# 4. 清理原始图片文件（删除 jpg/png，只保留 webp）
python3 scripts/clean_original_images.py --execute

# 5. 清理临时目录
rm -rf static/images_compressed/posts/article-name
```

**随思录处理**：
```bash
# 步骤相同，路径替换为 thoughts
python3 scripts/compress_article_images.py content/thoughts/thought-name.md
cp -r static/images_compressed/thoughts/thought-name/* static/images/thoughts/thought-name/
python3 scripts/update_image_refs.py
python3 scripts/clean_original_images.py --execute
rm -rf static/images_compressed/thoughts/thought-name
```

#### 6.2 图片处理注意事项
- **先迁移图片**：必须先将图片复制到 `static/images/` 目录，再运行压缩脚本
- **路径规范**：使用完整文件路径作为脚本参数
- **格式统一**：最终所有图片统一为 WebP 格式
- **引用格式**：脚本会自动转换为 `/images/posts/article-name/image-name.webp`

### 7. 质量检查阶段

#### 7.1 内容验证
- 确认所有图片正确显示
- 检查文章格式规范（列表、引用、代码块）
- 验证图片 alt 文本是否有意义（避免使用文件名作为 alt）
- 确认元数据准确性，特别是标签合规性

#### 7.2 交叉引用检查
```bash
# 搜索相关关键词，查找需要更新的 Notion 链接
grep -r "notion.so" content/posts/
```

检查要点：
- 其他文章中的相关引用
- 修正指向 Notion 平台的旧链接
- 更新为正确的博客内部链接格式：`/posts/article-name`

### 8. 清理阶段

#### 8.1 临时文件清理
```bash
# 清理 Notion 解压目录
rm -rf temp_notion/*

# 清理图片压缩临时目录
rm -rf static/images_compressed/posts/article-name
rm -rf static/images_compressed/thoughts/thought-name

# 清理原始 ZIP 文件
rm -f temp_files/[Notion导出文件名].zip
```

#### 8.2 最终自检清单
- [ ] 文章标签全部来自预定义列表
- [ ] 所有临时文件和目录已清理
- [ ] 图片引用检查通过（全部为 .webp 格式的绝对路径）
- [ ] 图片 alt 文本有意义
- [ ] Notion 内部链接已转换为博客链接
- [ ] 文章格式符合规范

## 常见问题处理

### 脚本执行问题
- **图片目录不存在**：必须先创建图片目录并复制图片，再运行压缩脚本
- **路径错误**：必须使用完整文件路径，如 `content/posts/article-name.md`
- **WebP 文件不存在警告**：确保已运行压缩脚本并移动了压缩后的图片

### 文件名问题
- **包含空格**：`extract_zip_utf8.py` 会自动处理文件名中的空格
- **特殊字符**：避免使用特殊字符，使用英文和短横线

### 验证工具
```bash
# 检查图片引用有效性
python3 scripts/check_image_refs.py

# 检查标签合规性
python3 scripts/check_tags.py

# 检查排版规范
python3 scripts/check_spacing.py
```

## 技术实现细节

### 脚本依赖关系
1. `extract_zip_utf8.py` - 处理文件名编码问题，自动去除空格
2. `compress_article_images.py` - 图片压缩和格式转换（需要图片已在 static/images/ 目录）
3. `update_image_refs.py` - 自动更新 Markdown 中的图片引用（相对路径 → 绝对路径，扩展名 → .webp）
4. `clean_original_images.py` - 清理已转换的原始图片

### 图片处理参数
- **WebP 质量**：85%（JPG）/ 100% 无损（PNG）
- **最大尺寸**：1920x1920，保持原比例
- **格式转换**：统一转换为 WebP 格式

### update_image_refs.py 功能说明
该脚本会自动处理两种情况：
1. **相对路径**：`![alt](filename.png)` → `![alt](/images/posts/article-name/filename.webp)`
2. **绝对路径**：`![alt](/images/posts/article-name/filename.png)` → `![alt](/images/posts/article-name/filename.webp)`

脚本会检查 WebP 文件是否存在，只有存在时才会更新引用。
