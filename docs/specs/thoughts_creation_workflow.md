# Thoughts (随想) 创建工作流程规范

## 概述

Thought (随想) 是博客中一种更简短、随性的内容形式，通常没有正式的标题。本文档详细规定了创建和管理 Thoughts 内容的标准流程。

## 内容特点

- **简短随性**：比正式博文更加简洁和随意
- **无正式标题**：通常不需要设置标题，或标题可以留空
- **快速记录**：适合记录灵感、想法、感悟等
- **灵活形式**：可以包含文字、图片等多种形式

## 创建方法

### 方法一：直接创建 Markdown 文件

适用于快速记录文字内容的场景。

#### 1. 创建 Markdown 文件

- **存放位置**：`content/thoughts/` 目录下
- **文件名规范**：
  - 使用英文单词，避免使用拼音
  - 单词之间使用短横线 `-` 分隔
  - 建议使用简短描述性名称
  - 示例：`my-random-thought.md`、`weekend-reflection.md`

#### 2. 配置 Front Matter

在文件开头添加必要的元数据：

```yaml
---
author: "Joe"
date: "2024-03-15"  # 使用实际日期，格式：YYYY-MM-DD
description: "这里填写对这个 Thought 的简短描述" 
draft: false
tags: ["生活感悟"] # 从预定义标签列表选择
title: "" # Thought 通常没有标题，可以留空
---
```

**重要说明**：
- `title` 字段可以留空或不设置
- `tags` 必须从预定义标签列表中选择（详见「标签规范」章节）
- 获取当前日期：在终端运行 `date +%Y-%m-%d`
- 所有字符串值必须用英文双引号包裹

#### 3. 添加正文内容

在 Front Matter 下方直接添加 Thought 内容。

**图片 Caption 处理**：
如果内容中包含图片说明文字，使用以下 HTML 格式：

```html
<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>Caption 文案内容</em>
</div>
```

#### 4. 处理图片（如有需要）

如果 Thought 包含图片，按以下步骤处理：

**4.1 准备图片目录**
```bash
# 创建对应的图片目录
mkdir -p static/images/thoughts/thought-file-name/
# 将原始图片放入此目录
```

**4.2 图片处理流程**
假设 Thought 文件名为 `thought-file-name.md`：

```bash
# 1. 压缩并转换图片为 WebP 格式
python3 scripts/compress_article_images.py thoughts/thought-file-name

# 2. 更新文章中的图片引用为 WebP 格式
python3 scripts/update_image_refs.py

# 3. 将压缩后的图片移动到正确位置
cp -r static/images_compressed/thoughts/thought-file-name/* static/images/thoughts/thought-file-name/

# 4. 清理原始图片文件
python3 scripts/clean_original_images.py --execute

# 5. 清理临时文件
rm -rf static/images_compressed/thoughts/thought-file-name
```

**注意事项**：
- `compress_article_images.py` 的参数是图片存放的相对路径
- 确保所有脚本具有执行权限
- 图片会自动转换为 WebP 格式以优化性能

### 方法二：从 Notion 导出处理

如果从 Notion 导出 Thought 内容为 ZIP 文件，处理流程与普通博文类似，但需要注意 Thought 的特殊性。

**详细处理流程请参考**：
📋 [`notion_zip_processing_workflow.md`](notion_zip_processing_workflow.md)

该文档包含针对 thoughts 类型内容的完整处理流程，包括：
- ZIP 文件解压和内容转换
- Thought 特有的元数据配置
- 图片处理和优化
- 质量检查和验证

## 标签规范

Thoughts 的标签必须从以下预定义列表中选择，不允许创建新标签：

| 标签名称 | 描述 |
|---------|------|
| `书影音的精神角落` | 看书、看影视剧的记录 |
| `我有个想法！` | 生活或工作上的灵光乍现 |
| `江浙沪包游` | 江浙沪地区的旅行记录 |
| `提升幸福感的好物` | 包括软件和硬件提升幸福感的内容 |
| `折腾软硬件` | 软件和数码硬件相关的折腾 |
| `游戏也是场冒险` | 游戏体验记录 |
| `小城故事` | 老家的故事 |
| `阅读笔记` | 书籍以外的阅读笔记 |
| `现实是个开放世界` | 所有地方的旅行日记（包括江浙沪地区） |
| `工作感悟` | 工作相关的总结 |
| `生活感悟` | 生活相关的感悟 |
| `4+2 骑行中` | 骑行相关的内容 |
| `AI 相关` | 与 AI 相关的内容 |
| `Vibe Coding` | 与 AI 编程相关的感悟 |

## 质量检查

创建 Thought 后，建议运行以下检查：

```bash
# 检查标签是否符合规范
python3 scripts/check_tags.py

# 检查图片引用是否有效
python3 scripts/check_image_refs.py

# 检查中英文排版规范
python3 scripts/check_spacing.py
```

## 最佳实践

1. **内容长度**：建议控制在 500 字以内，保持简洁
2. **发布频率**：可以较为随意，不需要固定节奏
3. **标签选择**：优先选择「生活感悟」、「我有个想法！」等适合随想的标签
4. **图片使用**：如有图片，确保与内容相关且经过优化处理
5. **及时记录**：有想法时及时记录，不要过度修饰

## 常见问题

**Q: Thought 一定要留空标题吗？**
A: 不是必须的。如果有合适的标题可以填写，但通常 Thought 更适合无标题的形式。

**Q: 可以在 Thought 中使用代码块吗？**
A: 可以，但建议保持简洁，避免过于复杂的技术内容。

**Q: Thought 和正式博文的主要区别是什么？**
A: Thought 更随性、简短，通常无正式标题，适合快速记录想法；博文更正式、结构化，有明确主题。

**Q: 如何决定内容应该写成 Thought 还是博文？**
A: 如果内容简短（<500字）、随性、无需详细结构，适合 Thought；如果需要详细阐述、有完整逻辑结构，适合博文。
