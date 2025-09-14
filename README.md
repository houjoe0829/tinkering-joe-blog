# Joe 的折腾日记

这个博客使用 Hugo 静态网站生成器构建，并托管在 Cloudflare Pages 上。

- 博客官方地址是：[https://houjoe.me/](https://houjoe.me/)
- Cloudflare 的原始地址是：[https://discovery-log.pages.dev/](https://discovery-log.pages.dev/)

## 项目目录结构

```
discovery-log/
├── archetypes/          # Hugo 文章模板
│   └── sky-eye.md      # 天空之眼文章模板
├── assets/              # 自定义样式和资源文件
│   └── css/
│       └── extended/
│           └── custom.css
├── content/             # 博客文章内容
│   ├── posts/          # 普通博客文章
│   └── sky-eye/        # 天空之眼全景照片文章
├── data/               # Hugo 数据文件
├── docs/               # 项目文档管理
│   ├── specs/          # 已固化的需求与技术实现规范
│   └── staging/        # 过渡区：从想法到执行的方案（命名：[状态].主题名.md）
├── i18n/               # 国际化文件
├── layouts/            # 自定义布局模板
│   ├── _default/       # 默认布局
│   ├── partials/       # 页面组件
│   ├── shortcodes/     # 短代码
│   └── sky-eye/        # 天空之眼布局模板
├── public/             # Hugo 生成的静态网站文件
├── resources/          # Hugo 缓存资源
├── scripts/            # 工具脚本目录
│   ├── extract_zip_utf8.py           # Notion ZIP 文件处理
│   ├── compress_article_images.py     # 单篇文章图片压缩
│   ├── compress_images.py            # 全局图片压缩
│   ├── clean_original_images.py      # 清理原始图片
│   └── update_image_refs.py          # 更新图片引用
├── static/             # 静态资源文件
│   ├── conf/           # 配置文件
│   ├── downloads/      # 下载资源
│   ├── images/         # 图片资源
│   │   ├── posts/      # 文章图片
│   │   └── sky-eye/    # 天空之眼图片
│   │       └── optimized/ # 优化后的全景照片
│   └── js/             # JavaScript 文件
├── temp_files/         # 临时文件目录（处理全景照片）
├── themes/             # Hugo 主题
│   └── PaperMod/       # 当前使用的主题
├── workers/            # Cloudflare Workers 脚本
├── .gitignore          # Git 忽略文件
├── hugo.yaml           # Hugo 配置文件
└── README.md          # 项目说明文档
```

## 当前博客构建方式

* **Hugo**: 负责将 Markdown 内容转换为静态网页。
* **Cloudflare Pages**:  提供网站托管、CDN 加速和自动部署。
* **GitHub**:  用于存储博客源代码和版本管理。
* **Giscus**:  提供评论功能，使用 GitHub Discussions 存储评论数据。

---

## 本地构建和调试

在您提交更新之前，您可以在本地电脑上预览博客效果，确保一切正常：

1. **安装 Hugo**:  请确保您已经在本机安装了 Hugo (具体安装步骤请参考 [Hugo 官方文档](https://gohugo.io/getting-started/installing/))。

2. **本地预览**:
    * 运行命令 `hugo server -D`。
    * Hugo 将会在本地启动一个开发服务器，您可以通过浏览器访问 `http://localhost:1313/` 来预览您的博客。

3. **停止预览**:
    * 在命令行终端中按下 `Ctrl + C` 即可停止本地 Hugo 开发服务器。

## 博客内容类型

本博客支持三种不同类型的内容：**博文**（深度文章）、**天空之眼**（360° 全景图片）和**想法**（简短随想）。每种类型都有其独特的特点、用途和管理方式。

**详细的内容类型说明请参考：**
📋 [`docs/specs/content_types_overview.md`](docs/specs/content_types_overview.md)

该文档包含完整的内容类型规范，涵盖：
- 三种内容类型的详细定义和特征
- 适用场景和最佳实践
- 技术规格和处理流程
- 存储位置和命名规范
- 新增内容类型的考虑要素

## 内容交叉引用系统

博客中的三种内容类型（博文、天空之眼、想法）之间可以互相引用和关联，形成丰富的内容网络。系统支持直接引用、标签关联、时间关联等多种关系类型，并提供智能的相关内容推荐。

**详细的交叉引用系统规范请参考：**
📋 [`docs/specs/content_cross_reference_system.md`](docs/specs/content_cross_reference_system.md)

该文档包含完整的交叉引用系统指南，涵盖：
- 四种关系类型和引用方式详解
- 相关内容推荐算法和显示逻辑
- Hugo 模板实现和前端交互增强
- 显示样式规范和性能优化
- 内容策略建议和监控分析

## 博客样式定制

本博客基于 Hugo PaperMod 主题构建，并进行了自定义样式调整以实现极简风格。包含标题规范、表格样式、响应式设计等完整的样式体系。

**详细的样式定制规范请参考：**
📋 [`docs/specs/blog_styling_guide.md`](docs/specs/blog_styling_guide.md)

该文档包含完整的样式定制指南，涵盖：
- 主题管理和自定义样式位置
- 标题和表格的详细样式规范
- 样式开发最佳实践和调试技巧
- 响应式设计和暗色模式适配
- 主题定制扩展和维护方法


## 依据导出的 Notion ZIP 压缩包来更新博文的规则

从 Notion 导出的 ZIP 压缩包需要经过标准化的处理流程才能转换为博客文章。

**详细的处理规则和操作步骤请参考：**
📋 [`docs/specs/notion_zip_processing_workflow.md`](docs/specs/notion_zip_processing_workflow.md)

该文档包含完整的工作流程，涵盖：
- 文件解压和内容转换
- 元数据配置规范
- 图片处理和优化
- 质量检查和验证
- 清理和维护步骤



## 手动增加 Thought (随想) 的方法

Thought (随想) 是一种更简短、随性的内容形式，通常没有正式的标题。您可以通过直接创建 Markdown 文件或从 Notion 导出 ZIP 文件两种方式添加 Thought。

**详细的创建规则和操作步骤请参考：**
📋 [`docs/specs/thoughts_creation_workflow.md`](docs/specs/thoughts_creation_workflow.md)

该文档包含完整的 Thoughts 创建工作流程，涵盖：
- 文件创建和命名规范
- Front Matter 配置要求
- 图片处理和优化流程
- 标签规范和质量检查
- 最佳实践和常见问题

## 全局图片压缩的方法

为了优化网站加载速度和存储空间，博客需要定期对图片进行压缩处理和 WebP 转换。这个过程包括压缩、格式转换、引用更新和清理等多个步骤。

**详细的压缩规则和操作步骤请参考：**
📋 [`docs/specs/global_image_compression_workflow.md`](docs/specs/global_image_compression_workflow.md)

该文档包含完整的全局图片压缩工作流程，涵盖：
- 压缩工具配置和参数设置
- 完整的 6 步压缩流程
- 环境准备和依赖安装
- 自动化脚本和批量处理
- 质量检查和故障排除

## 图片引用的自检方法

博客提供了专门的图片引用验证工具，可以检测所有 Markdown 文件中的图片引用有效性，验证文件存在性，识别外部链接和失效引用，确保内容完整性。

**详细的图片引用验证规范请参考：**
📋 [`docs/specs/image_reference_validation.md`](docs/specs/image_reference_validation.md)

该文档包含完整的图片引用验证指南，涵盖：
- 验证工具使用方法和检查内容详解
- 常见问题和解决方案
- 批量修复工具和自动化集成
- 性能优化和最佳实践
- 团队协作和维护流程

## Blog 元数据格式规范

为了保持博客文章的一致性，所有文章的元数据(Front Matter)必须遵循以下格式规范：

```yaml
---
author: "Joe"                                     # 作者名需要用引号包裹
date: 2024-02-11                                 # 日期格式：YYYY-MM-DD，不需要引号
description: "这里写文章的简短描述"                 # 描述需要用引号包裹
draft: false                                     # 是否为草稿：true/false
tags: ["标签1", "标签2"]                         # 标签格式：数组，每个标签用引号包裹
title: "文章标题"                                # 标题需要用引号包裹
---
```

### 格式要求说明

1. **引号使用规则**：
   * `author`、`description`、`title` 和标签内容必须使用双引号 `"` 包裹
   * `date` 和 `draft` 不需要使用引号

2. **日期格式**：
   * 必须使用 `YYYY-MM-DD` 格式
   * 不要包含时间信息
   * 不要使用引号包裹

3. **标签格式和规范**：
   * 使用数组格式 `["标签1", "标签2"]`
   * 每个标签都要用双引号包裹
   * 标签之间使用逗号和空格分隔
   * 标签必须从以下预定义列表中选择，不允许创建新标签：

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

1. **字段顺序**：
   * 建议按照 author、date、description、draft、tags、title 的顺序排列
   * 保持所有文章的字段顺序一致

2. **其他注意事项**：
   * 确保每个字段后面有一个空格再写值
   * 冒号后面必须有一个空格
   * 不要在字段值末尾添加多余的空格
   * 确保 `---` 分隔符前后都有空行

### 示例

一个标准的文章元数据示例：

```yaml
---
author: "Joe"
date: 2024-02-11
description: "这是一篇关于如何正确设置博客文章元数据的教程"
draft: false
tags: ["折腾软硬件", "我有个想法！"]
title: "博客文章元数据格式指南"
---
```

## YouTube 视频嵌入规范

为了在博客文章中嵌入 YouTube 视频，请使用 Hugo 的内置 shortcode。这种方式可以确保视频在不同设备上都能正确显示，并且保持响应式布局。

### 基本用法

```markdown
{{</* youtube 视频ID */>}}
```

### 示例

```markdown
这是一段视频的相关描述。

{{</* youtube cKONu4-p0ws */>}}

这是视频后的补充说明。
```

## 链接样式规范

博客支持两种不同的链接样式：Bookmark 样式（卡片式重点链接）和普通链接（标准 Markdown 链接）。每种样式都有其特定的适用场景和使用方法。

**详细的链接样式规范请参考：**
📋 [`docs/specs/link_styling_guide.md`](docs/specs/link_styling_guide.md)

该文档包含完整的链接样式指南，涵盖：
- 两种链接样式的详细说明和使用方法
- 适用场景和选择指南
- 技术实现细节和样式定制
- 可访问性考虑和性能优化
- 维护更新和常见问题解答


## 全局标签检查的方法

为了确保博客中的所有标签都符合预定义规范，我们提供了一个专门的检查脚本。这个工具可以帮助您：
1. 检查所有博文的标签是否都在预定义的标签列表中
2. 统计每个标签的使用次数
3. 检查是否有未使用的预定义标签
4. 输出详细的检查报告

### 运行检查

使用以下命令运行标签检查：

```bash
python3 scripts/check_tags.py
```

### 检查内容

脚本会检查以下内容：
1. **标签合规性**：检查每篇文章的标签是否都在预定义列表中
2. **标签使用情况**：统计每个标签的使用次数
3. **未使用标签**：识别预定义列表中未被使用的标签
4. **异常情况**：检测缺少标签或使用了无效标签的文章

### 检查结果

脚本会输出详细的检查报告，包括：
1. 每个标签的使用统计
2. 未使用的标签列表
3. 包含无效标签的文件列表
4. 缺少 Front Matter 的文件列表
5. 标签为空的文件列表


## 自动化排版检查工具

为了确保博客文章符合中英文排版规范，我们提供了一个自动化检查工具。这个工具基于 pangu.py，可以自动检测并修正中英文之间的空格问题。

### 安装依赖

```bash
pip install pangu colorama
```

### 使用方法

1. **检查所有文章并显示需要修正的内容**：

```bash
python3 scripts/check_spacing.py
```

2. **自动修正所有文章的排版问题**：

```bash
python3 scripts/check_spacing.py --fix
```

3. **只检查指定文件**：

```bash
python3 scripts/check_spacing.py --file content/posts/your-article.md
```

4. **检查并修正指定文件**：

```bash
python3 scripts/check_spacing.py --file content/posts/your-article.md --fix
```

### 注意事项

- 该工具会保留 Front Matter 不变，只处理文章正文部分
- 工具会显示具体的修改差异，方便您查看修改内容
- 建议在提交新文章前运行此工具，确保排版规范一致



## 博客内容统计 Dashboard

博客支持自动化的内容统计功能，可以在搜索页面查看创作成果，包括字数统计、内容分类和年度统计。通过 Git Pre-commit Hook 实现完全自动化的数据更新。

**详细的统计功能规范请参考：**
📋 [`docs/specs/content_statistics_dashboard.md`](docs/specs/content_statistics_dashboard.md)

该文档包含完整的内容统计系统指南，涵盖：
- 功能特性和统计规则详解
- Git Pre-commit Hook 自动化机制
- 技术实现架构和数据结构
- 部署配置和使用指南
- 性能优化和扩展定制方法

## 许可证说明

本仓库采用双重许可证模式：

1. **博客内容**：所有博客文章内容（包括文字、图片等）采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可证。
2. **代码部分**：所有代码文件采用 [MIT](https://opensource.org/licenses/MIT) 许可证。

详细的许可说明请查看 [LICENSE.md](LICENSE.md) 文件。