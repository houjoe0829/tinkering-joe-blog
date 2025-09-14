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
- 内容解压到：`temp_notion/[ZIP包名命名的目录]/`
- 通常包含：主 Markdown 文件 + 附件文件夹（图片等）

### 2. 内容创建阶段

#### 2.1 确定文章信息
- 确认主 Markdown 文件
- 确定文章标题
- 确定内容类型（posts 或 thoughts）

#### 2.2 创建目标文件
**博客文章**：
- 位置：`content/posts/[英文文件名].md`
- 命名规范：英文单词，短横线分隔，避免拼音

**随思录**：
- 位置：`content/thoughts/[英文文件名].md`
- 命名规范：同博客文章

### 3. 元数据配置阶段

#### 3.1 Front Matter 结构
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

#### 3.2 元数据规范
- **YAML 敏感性**：使用纯英文引号包裹值
- **标点符号**：统一使用半角标点
- **标签限制**：只能从预定义标签列表中选择
- **参考模板**：以 `@nezha-movie-review.md` 为格式参考

### 4. 内容转换阶段

#### 4.1 正文内容处理
- 复制 Notion Markdown 正文到目标文件
- 移除或转换 Notion 内部链接
- 调整 Callout、Toggle 等 Notion 特有块格式
- 清理不必要的 HTML 标签或样式

#### 4.2 图片 Caption 处理
当 Notion 导出包含图片 Caption 时，使用以下 HTML 格式：
```html
<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>Caption 文案内容</em>
</div>
```

### 5. 图片处理阶段

#### 5.1 图片目录创建
**博客文章**：`static/images/posts/[文章名]/`
**随思录**：`static/images/thoughts/[文章名]/`

#### 5.2 图片处理命令序列

**博客文章处理**：
```bash
# 1. 压缩并转换图片为 WebP 格式
python3 scripts/compress_article_images.py content/posts/article-name.md

# 2. 移动压缩后的图片到正确位置
cp -r static/images_compressed/posts/article-name/* static/images/posts/article-name/

# 3. 更新图片引用（运行两次确保完全更新）
python3 scripts/update_image_refs.py
python3 scripts/update_image_refs.py

# 4. 检查并重命名包含空格的文件名
ls static/images/posts/article-name/ | grep " " || echo "无需重命名"
# 如需重命名：
# cd static/images/posts/article-name
# mv "image 1.webp" "image1.webp"

# 5. 再次更新引用（处理重命名的文件）
python3 scripts/update_image_refs.py

# 6. 清理原始图片文件
python3 scripts/clean_original_images.py --execute

# 7. 清理临时文件
rm -rf static/images_compressed/posts/article-name
```

**随思录处理**：
```bash
# 1. 压缩并转换图片
python3 scripts/compress_article_images.py content/thoughts/thought-name.md

# 2. 移动压缩后的图片
cp -r static/images_compressed/thoughts/thought-name/* static/images/thoughts/thought-name/

# 3-7. 其余步骤同博客文章，路径替换为 thoughts
python3 scripts/update_image_refs.py
python3 scripts/update_image_refs.py
# ... 其余步骤
rm -rf static/images_compressed/thoughts/thought-name
```

#### 5.3 图片处理注意事项
- **禁止手动操作**：不要手动重命名图片或修改 Markdown 引用
- **路径规范**：使用完整文件路径作为脚本参数
- **格式统一**：最终所有图片统一为 WebP 格式
- **引用格式**：`/images/posts/article-name/image-name.webp`

### 6. 质量检查阶段

#### 6.1 内容验证
- 确认所有图片正确显示
- 检查文章格式规范（列表、引用、代码块）
- 验证图片描述准确性
- 确认元数据准确性，特别是标签合规性

#### 6.2 交叉引用检查
```bash
# 搜索相关关键词
grep -r "关键词" content/posts/
# 或使用项目搜索脚本
python3 scripts/grep_search.py "关键词"
```

检查要点：
- 其他文章中的相关引用
- 修正指向 Notion 平台的旧链接
- 更新为正确的博客内部链接格式：`/posts/article-name`

### 7. 清理阶段

#### 7.1 临时文件清理
```bash
# 清理 Notion 解压目录
rm -rf temp_notion/[ZIP包名命名的目录]

# 清理图片压缩临时目录
rm -rf static/images_compressed/posts/article-name
rm -rf static/images_compressed/thoughts/thought-name

# 清理原始 ZIP 文件
rm -f temp_files/[Notion导出文件名].zip
```

#### 7.2 最终自检清单
- [ ] 文章标签全部来自预定义列表
- [ ] 所有临时文件和目录已清理
- [ ] 图片引用检查通过
- [ ] 文章格式符合规范

## 常见问题处理

### 脚本执行问题
- **路径错误**：必须使用完整文件路径，如 `content/posts/article-name.md`
- **引用更新不完全**：需要多次运行 `update_image_refs.py`
- **WebP 文件不存在警告**：移动图片前运行更新脚本的正常现象

### 文件名问题
- **包含空格**：Notion 导出的图片可能包含空格，需手动重命名
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
1. `extract_zip_utf8.py` - 处理文件名编码问题
2. `compress_article_images.py` - 图片压缩和格式转换
3. `update_image_refs.py` - 自动更新 Markdown 中的图片引用
4. `clean_original_images.py` - 清理已转换的原始图片

### 图片处理参数
- **WebP 质量**：85%
- **最大尺寸**：保持原比例，适当压缩
- **格式转换**：统一转换为 WebP 格式

### 自动化程度
- 文件扫描：自动识别唯一 ZIP 文件
- 图片处理：全自动压缩、转换、引用更新
- 清理操作：脚本化批量清理临时文件