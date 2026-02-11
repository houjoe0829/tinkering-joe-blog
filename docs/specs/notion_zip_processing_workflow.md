# Notion ZIP 文件处理工作流程 v2

## 概述

本文档定义了从 Notion 导出的 ZIP 压缩包转换为博客文章的标准化处理流程。该流程涵盖了环境检查、文件解压、内容转换、图片处理、格式规范化和清理等完整环节,确保 Notion 内容能够无缝集成到 Hugo 博客系统中。

## 适用范围

- 博客文章（posts）：放置在 `content/posts/` 目录
- 随思录（thoughts）：放置在 `content/thoughts/` 目录
- 支持包含图片附件的 Notion 导出内容

## 前置条件

### 环境要求

#### Python 环境检查
```bash
# 检查 Python 版本
python3 --version  # 需要 3.6+

# 检查虚拟环境配置（如果使用）
which python3
```

#### 必需的 Python 依赖
```bash
# 在项目虚拟环境中安装所有依赖
pip3 install Pillow piexif colorama pangu

# 或使用 requirements.txt（如果项目有）
pip3 install -r requirements.txt
```

**依赖说明**：
- `Pillow`：图片处理和格式转换
- `piexif`：EXIF 数据处理
- `colorama`：终端彩色输出（用于检查脚本）
- `pangu`：中文排版规范检查

#### 其他工具
- ImageMagick（可选,部分图片处理场景）
- 项目根目录下的处理脚本

### 文件准备
- Notion ZIP 文件已放置在 `temp_files/` 目录下
- 确保 ZIP 文件是唯一的待处理文件

---

## 标准处理流程

### 阶段 0：环境检查 ✅

**目的**：确保所有依赖已安装,避免执行过程中报错

```bash
# 1. 检查虚拟环境
which python3

# 2. 测试导入关键依赖
python3 -c "import PIL; import piexif; import colorama; import pangu; print('所有依赖已安装')"

# 如果报错,安装缺失的依赖
pip3 install Pillow piexif colorama pangu
```

---

### 阶段 1：文件解压

#### 1.1 自动扫描和解压
```bash
# AI 助手会自动扫描 temp_files 目录,找出唯一的 ZIP 文件
python3 scripts/extract_zip_utf8.py temp_files/[ZIP文件名].zip
```

#### 1.2 解压结果
- 内容解压到：`temp_notion/` 目录（Markdown 文件和图片平铺在根目录）
- 通常包含：主 Markdown 文件 + 图片文件

---

### 阶段 2：图片迁移（在创建文章之前）

> **重要**：必须先将图片复制到目标目录,再创建文章文件。这是因为图片压缩脚本需要从 `static/images/` 目录读取原始图片。

#### 2.1 创建图片目录并复制图片
```bash
# 博客文章
mkdir -p static/images/posts/[article-name]
cp temp_notion/*.png temp_notion/*.jpg temp_notion/*.jpeg static/images/posts/[article-name]/ 2>/dev/null

# 随思录
mkdir -p static/images/thoughts/[thought-name]
cp temp_notion/*.png temp_notion/*.jpg temp_notion/*.jpeg static/images/thoughts/[thought-name]/ 2>/dev/null
```

---

### 阶段 3：内容创建

#### 3.1 确定文章信息
- 确认主 Markdown 文件（在 `temp_notion/` 中）
- 确定文章标题
- 确定内容类型（posts 或 thoughts）
- 确定英文文件名

#### 3.2 创建目标文件
**博客文章**：
- 位置：`content/posts/[英文文件名].md`
- 命名规范：英文单词,短横线分隔,避免拼音

**随思录**：
- 位置：`content/thoughts/[英文文件名].md`
- 命名规范：同博客文章

#### 3.3 图片引用格式
在创建文章时,可以直接使用相对路径引用图片（如 `![alt](filename.png)`）,`update_image_refs.py` 脚本会自动将其转换为正确的绝对路径格式。

---

### 阶段 4：元数据配置

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
- **YAML 语法**：使用纯英文引号包裹值
- **Front Matter 标点**：**必须使用半角标点**（冒号、逗号等）
- **标签限制**：只能从预定义标签列表中选择
- **参考模板**：以 `@weekly-plan-is-for-changes.md` 为格式参考

---

### 阶段 5：内容转换

#### 5.1 正文内容处理
- 复制 Notion Markdown 正文到目标文件
- **删除 Notion 元数据注释**（如 `<!-- Created: YYYY-MM-DD -->`）
- **删除正文开头的一级标题**（`# 文章标题`），因为 Front Matter 中已有 `title` 字段
- 移除或转换 Notion 内部链接（转换为博客内部链接格式 `/posts/article-name`）
- 调整 Callout、Toggle 等 Notion 特有块格式
- 清理不必要的 HTML 标签或样式

**重要**：Hugo 会自动从 Front Matter 的 `title` 字段生成页面标题,正文不需要重复的一级标题。

#### 5.2 图片 Caption 处理
当 Notion 导出包含图片 Caption 时,使用以下 HTML 格式：
```html
<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>Caption 文案内容</em>
</div>
```

#### 5.3 图片尺寸调整
如需调整图片显示尺寸（如 50% 宽度并居中）,使用以下格式：
```html
<img src="/images/posts/article-name/image.webp" alt="描述" style="width: 50%; display: block; margin: 0 auto;" />
```

---

### 阶段 6：图片处理

#### 6.1 图片处理命令序列

**博客文章处理**：
```bash
# 1. 压缩并转换图片为 WebP 格式（图片必须已在 static/images/posts/article-name/ 中）
python3 scripts/compress_article_images.py content/posts/article-name.md

# 2. 移动压缩后的图片到正确位置（覆盖原始图片目录）
cp -r static/images_compressed/posts/article-name/* static/images/posts/article-name/

# 3. 更新图片引用（自动将相对路径转为绝对路径,并更新扩展名为 .webp）
python3 scripts/update_image_refs.py

# 4. 清理原始图片文件（删除 jpg/png,只保留 webp）
python3 scripts/clean_original_images.py --execute

# 5. 清理临时目录
rm -rf static/images_compressed/posts/article-name
```

**随思录处理**：
```bash
# 步骤相同,路径替换为 thoughts
python3 scripts/compress_article_images.py content/thoughts/thought-name.md
cp -r static/images_compressed/thoughts/thought-name/* static/images/thoughts/thought-name/
python3 scripts/update_image_refs.py
python3 scripts/clean_original_images.py --execute
rm -rf static/images_compressed/thoughts/thought-name
```

#### 6.2 图片处理注意事项
- **先迁移图片**：必须先将图片复制到 `static/images/` 目录,再运行压缩脚本
- **路径规范**：使用完整文件路径作为脚本参数
- **格式统一**：最终所有图片统一为 WebP 格式
- **引用格式**：脚本会自动转换为 `/images/posts/article-name/image-name.webp`

---

### 阶段 7：中文标点符号修正 ⭐

> **新增阶段**：确保中文文本使用全角标点,同时保护 Front Matter 和技术内容

#### 7.1 使用 check-chinese-punctuation skill

**推荐方式**：通过 AI 助手调用 skill
```
使用 /check-chinese-punctuation skill 处理文章
```

或者在对话中直接说明：
```
请使用 check-chinese-punctuation skill 修正 content/posts/article-name.md 的标点符号
```

**Skill 特性**：
- ✅ 自动保护数字中的半角逗号（如 `40,000`）
- ✅ 自动跳过代码块、URL、技术参数
- ✅ **自动保护 Front Matter**（避免修改 YAML 格式）
- ✅ 提供详细的处理报告
- ✅ 支持批量处理

#### 7.2 验证处理结果

**Skill 会自动处理并报告**：
- 修正了多少处标点符号
- 保护了哪些内容（数字、URL、代码块等）
- Front Matter 是否安全（未被修改）

**手动检查 Front Matter**（推荐）：
```yaml
# ✅ 正确：Front Matter 必须使用半角标点
description: "这是一篇文章"
title: "文章标题"

# ❌ 错误：全角冒号会导致 YAML 解析失败
description： "这是一篇文章"
title： "文章标题"
```

**如果发现问题**：
- 请向 AI 助手报告："Front Matter 被错误修改了"
- AI 助手会自动修正

#### 7.3 验证标点修正结果

```bash
# 检查中文行是否还有半角逗号
grep -n "[一-龥].*," content/posts/article-name.md

# 应该返回空（或只有 Front Matter、代码块、URL 等技术内容）
```

---

### 阶段 8：质量检查

#### 8.1 内容验证
- 确认所有图片正确显示
- 检查文章格式规范（列表、引用、代码块）
- 验证图片 alt 文本是否有意义（避免使用文件名作为 alt）
- 确认元数据准确性,特别是标签合规性
- **验证 Front Matter 使用半角标点**

#### 8.2 自动化检查脚本

```bash
# 检查标签合规性
python3 scripts/check_tags.py

# 检查图片引用有效性
python3 scripts/check_image_refs.py

# 检查中文排版规范
python3 scripts/check_spacing.py
```

#### 8.3 交叉引用检查
```bash
# 搜索相关关键词,查找需要更新的 Notion 链接
grep -r "notion.so" content/posts/
```

检查要点：
- 其他文章中的相关引用
- 修正指向 Notion 平台的旧链接
- 更新为正确的博客内部链接格式：`/posts/article-name`

---

### 阶段 9：清理

#### 9.1 临时文件清理
```bash
# 清理 Notion 解压目录
rm -rf temp_notion/*

# 清理图片压缩临时目录
rm -rf static/images_compressed/posts/article-name
rm -rf static/images_compressed/thoughts/thought-name

# 清理原始 ZIP 文件
rm -f temp_files/[Notion导出文件名].zip
```

#### 9.2 最终自检清单
- [ ] 文章标签全部来自预定义列表
- [ ] 所有临时文件和目录已清理
- [ ] 图片引用检查通过（全部为 .webp 格式的绝对路径）
- [ ] 图片 alt 文本有意义
- [ ] Notion 内部链接已转换为博客链接
- [ ] 文章格式符合规范
- [ ] **Front Matter 使用半角标点**
- [ ] **正文中文使用全角标点**
- [ ] **正文开头没有重复的一级标题**

---

## 常见问题处理

### 环境问题

#### 虚拟环境配置错误
**症状**：
```
/path/to/.venv/bin/pip3: line 2: /wrong/path/python: No such file or directory
```

**解决方法**：
```bash
# 删除旧的虚拟环境
rm -rf .venv

# 重新创建虚拟环境
python3 -m venv .venv

# 激活并安装依赖
source .venv/bin/activate
pip3 install Pillow piexif colorama pangu
```

#### Python 依赖缺失
**症状**：
```
ModuleNotFoundError: No module named 'PIL'
```

**解决方法**：
```bash
# 检查当前使用的 Python
which python3

# 在正确的环境中安装依赖
pip3 install Pillow piexif colorama pangu
```

### 脚本执行问题

#### 图片目录不存在
**问题**：运行 `compress_article_images.py` 时报错图片不存在

**原因**：没有先将图片复制到 `static/images/` 目录

**解决**：参考阶段 2,先复制图片再运行压缩脚本

#### 路径错误
**问题**：脚本无法找到文件

**原因**：使用了相对路径而非完整文件路径

**解决**：使用完整路径,如 `content/posts/article-name.md`

#### WebP 文件不存在警告
**问题**：`update_image_refs.py` 警告 WebP 文件不存在

**原因**：未运行压缩脚本或未移动压缩后的图片

**解决**：确保完整执行阶段 6 的所有步骤

### 标点符号问题

#### Front Matter 被错误修改
**症状**：
```yaml
description： "文章描述"  # 全角冒号
```

**解决**：
向 AI 助手说明："Front Matter 的标点被错误修改了,请修正"

**预防**：
- 使用 `/check-chinese-punctuation` skill（会自动保护 Front Matter）
- 处理完成后手动检查 Front Matter

#### 数字格式被破坏
**症状**：`40,000` 被替换为 `40，000`

**原因**：使用了不当的批量替换方法

**解决**：使用 `/check-chinese-punctuation` skill,它会自动保护数字格式

### 内容格式问题

#### 正文开头有重复标题
**症状**：文章显示两个标题

**原因**：Notion 导出时包含一级标题,未删除

**解决**：参考阶段 5.1,删除正文开头的 `# 标题`

### 文件名问题

#### 包含空格
`extract_zip_utf8.py` 会自动处理文件名中的空格

#### 包含特殊字符
避免使用特殊字符,使用英文和短横线

---

## 技术实现细节

### 脚本和工具依赖关系
1. `extract_zip_utf8.py` - 处理文件名编码问题,自动去除空格
2. `compress_article_images.py` - 图片压缩和格式转换（需要图片已在 static/images/ 目录）
3. `update_image_refs.py` - 自动更新 Markdown 中的图片引用（相对路径 → 绝对路径,扩展名 → .webp）
4. `clean_original_images.py` - 清理已转换的原始图片
5. `/check-chinese-punctuation` skill - 智能修正中文标点符号（保护数字、Front Matter、技术内容）

### 图片处理参数
- **WebP 质量**：85%（JPG）/ 100% 无损（PNG）
- **最大尺寸**：1920x1920,保持原比例
- **格式转换**：统一转换为 WebP 格式

### update_image_refs.py 功能说明
该脚本会自动处理两种情况：
1. **相对路径**：`![alt](filename.png)` → `![alt](/images/posts/article-name/filename.webp)`
2. **绝对路径**：`![alt](/images/posts/article-name/filename.png)` → `![alt](/images/posts/article-name/filename.webp)`

脚本会检查 WebP 文件是否存在,只有存在时才会更新引用。

### check-chinese-punctuation skill 智能特性
- 自动保护数字中的半角逗号（如 `40,000` 不会变成 `40，000`）
- 自动跳过代码块、URL、Front Matter
- 智能识别技术内容（坐标、版本号、域名等）
- 支持单文件和批量处理
- 提供详细的处理报告和验证结果
- 由 AI 助手智能调用,自动处理边界情况

---

## 改进点总结

### 相比 v1 版本的主要改进

1. **新增阶段 0：环境检查**
   - 明确列出所有 Python 依赖
   - 提供依赖检查和安装命令
   - 包含虚拟环境故障排除

2. **新增阶段 7：中文标点符号修正**
   - 使用智能脚本自动处理
   - 保护 Front Matter 和技术内容
   - 提供验证方法

3. **修正阶段 5：内容转换**
   - 明确说明需要删除正文开头的一级标题
   - 更新参考模板文件名

4. **扩展常见问题处理**
   - 新增环境问题章节
   - 新增标点符号问题处理
   - 新增内容格式问题说明

5. **完善自检清单**
   - 增加 Front Matter 标点检查
   - 增加正文标点检查
   - 增加标题重复检查

### 版本对比

| 项目 | v1 版本 | v2 版本 |
|------|---------|---------|
| 环境检查 | ❌ 无 | ✅ 详细说明 |
| 依赖管理 | ⚠️ 简略 | ✅ 完整列表 |
| 标点处理 | ❌ 未提及 | ✅ 独立阶段 |
| 标题处理 | ❌ 错误描述 | ✅ 明确说明 |
| 故障排除 | ⚠️ 基础 | ✅ 详细分类 |
| 自检清单 | ⚠️ 不完整 | ✅ 全面覆盖 |

---

## 使用建议

1. **首次使用**：完整阅读文档,执行阶段 0 检查环境
2. **日常使用**：可跳过阶段 0,直接从阶段 1 开始
3. **遇到问题**：查阅"常见问题处理"章节
4. **脚本失败**：优先检查依赖和环境配置
5. **标点问题**：使用阶段 7 的智能脚本,手动验证 Front Matter
