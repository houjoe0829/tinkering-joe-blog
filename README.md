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
├── docs/               # 项目文档
│   └── draft/          # 需求文档和设计草稿
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

## 日常手动更新博客要注意的点

您只需要关注以下几个步骤即可轻松更新您的博客：

1. **撰写文章**:
    * 博客文章使用 Markdown 格式编写，请将 Markdown 文件放在 `content/posts/` 目录下。
    * **文件名命名规范**：
        * **使用英文**：文件名请使用英文单词，避免使用拼音。
        * **使用短横线分隔**： 单词之间使用短横线 `-` 分隔，例如 `my-second-post.md` 或 `how-to-insert-image.md`。
    * 例如，如果您要写一篇名为 `my-second-post.md` 的文章，就将其放在 `content/posts/` 文件夹中。

2. **插入图片**:
    * 如果您需要在文章中插入图片，请将图片文件放在 `static/images/` 目录下。
    * 然后在 Markdown 文件中使用 Markdown 语法引用图片，例如 `![图片描述](/images/your-image.jpg)`。

3. **提交更新**:
    * 完成文章撰写和图片添加后，将 `content/posts/` 和 `static/images/` 目录下的更改提交到 GitHub 仓库。
    * Cloudflare Pages 会自动检测到 GitHub 仓库的更新，并重新构建和部署您的博客。

## 如何添加"天空之眼"图片

### 添加新的全景图片
1. 准备图片
把原始全景图片放到 temp_files 目录下，建议保留原始文件名（如无人机拍摄的文件通常自带日期和编号）。
2. 提供信息
图片标题（必填）
图片描述（必填）
拍摄地点（可选）
经纬度坐标（可选，如果图片自带GPS信息可自动读取）
3. 自动或手动处理
系统或您自己将自动完成以下操作：

（1）读取照片信息
用 exiftool 工具读取图片的拍摄时间和GPS坐标（如有）。
示例命令：exiftool -DateTimeOriginal -GPSLatitude -GPSLongitude -c "%.6f" 图片路径
（2）图片处理
用 ImageMagick 生成两种图片文件：
优化后的WebP全景图（6000x3000，85%质量）：
magick 原始图片路径 -resize 6000x3000 -quality 85 static/images/sky-eye/optimized/文件名.webp
缩略图（800x400，85%质量）：
magick 原始图片路径 -resize 800x400 -quality 85 static/images/sky-eye/文件名-thumb.jpg
（3）文件管理
在 content/sky-eye/ 下创建 Markdown 文件，文件名用英文短横线风格。
Markdown 文件内容示例（需填入实际信息）：

---
title: "图片标题"
date: YYYY-MM-DDThh:mm:ss+08:00
description: "图片描述"
thumbnail: "/images/sky-eye/文件名-thumb.jpg"
panorama_image: "/images/sky-eye/optimized/文件名.webp"
location: "拍摄地点"
coordinates: "纬度,经度"
draft: false
---
（4）清理
删除 temp_files 下的原始图片，节省空间。
示例命令：rm temp_files/原始图片文件名

### 在文章中引用天空之眼全景图片

您可以在博客文章中引用天空之眼的全景图片，并实现嵌入式显示。这样用户可以直接在文章中查看全景图片的缩略图，并通过点击进入详情页。

使用方法：

```markdown
{{</* sky-eye-embed id="dongji-miaozi-lake-island" title="东极岛的庙子湖全景图片" */>}}
```

参数说明：
- `id`：天空之眼全景图片的文件名（不包含扩展名）
- `title`：可选，显示的标题，如果不提供则使用原始标题

嵌入后的效果是一个带有"查看360°全景图片"提示的缩略图，点击后进入天空之眼详情页。

## 新增内容类型的处理（例如：文章、随思录、天空之眼）

当博客需要引入新的内容类型时，为了确保其在网站的各个位置都能正确且美观地展示，您需要检查和调整以下相关的模板文件和配置。核心是考虑新内容在不同展示场景下的呈现效果：

**1. 内容定义与结构：**

*   **内容原型 (`archetypes/你的新类型.md`)**: 定义新类型内容的默认元数据。
*   **内容目录 (`content/你的新类型/`)**: 为新类型内容创建专属存放目录。

**2. 主要展示场景与对应模板：**

*   **首页 - 第一个条目 (`layouts/index.html`)**: 如果首页第一个条目有特殊样式，需确保新类型能正确应用。
*   **首页 - 非第一个条目 (`layouts/index.html` 及相关的局部模板如 `partials/entry.html` 或 `partials/post_card.html`)**: 确保新类型在标准列表项中正确显示。
*   **内容类型专属列表页 (`layouts/你的新类型/list.html`)**: 例如 `/thoughts/` 或 `/sky-eye/` 页面的列表展示。
*   **内容类型专属单页 (`layouts/你的新类型/single.html`)**: 单个内容详情页的展示，例如 `/thoughts/my-first-thought/`。
*   **搜索结果页 (`layouts/_default/search.html` 或相关局部模板)**: 确保新类型内容在搜索结果中能被正确显示，并更新统计信息（如果适用）。
*   **标签/分类列表页 (`layouts/taxonomy/terms.html` 或 `layouts/_default/terms.html` 及相关局部模板)**: 当通过标签或分类浏览时，新类型内容应能正确列出和展示。
*   **相关内容/反向链接 (通常在 `single.html` 或其局部模板中)**: 如果有此功能，确保新类型被正确处理。

**3. 其他相关配置与调整：**

*   **导航菜单 (通常在 `hugo.yaml` 或 `layouts/partials/header.html` 中)**: 如果需要，在主导航中添加入口。
*   **RSS 订阅 (`layouts/_default/rss.xml` 或类型专属 RSS)**: 如果希望新内容加入 RSS。
*   **自定义样式 (`assets/css/extended/custom.css`)**: 如果新类型需要独特的视觉样式。
*   **README.md (本文档)**: 记录新内容类型的特殊创建或管理流程。

通过检查以上各个方面，可以帮助您在添加新内容类型时，更系统地完成所有必要的修改。


## 博客样式定制

### 主题管理说明

博客使用了 PaperMod 主题。从 2025-02-20 起，主题代码已经从 git submodule 转换为普通文件，以简化管理和定制，构建属于自己的极简风格。

### 样式定制说明

博客使用了 PaperMod 主题，并进行了一些自定义样式调整。所有的自定义样式都在 `assets/css/extended/custom.css` 文件中。

### 标题样式规范

为了保持整个博客的视觉一致性，我们采用了以下标题大小规范：

1. **文章标题**: 24px（与首页博客列表标题大小保持一致）
2. **文章内容标题**:
   * h1: 24px（与文章标题相同）
   * h2: 22px（比 h1 小 2px）
   * h3: 20px（比 h2 小 2px）
   * h4: 18px（比 h3 小 2px）
   * h5: 16px（比 h4 小 2px）
   * h6: 14px（比 h5 小 2px）

这种递减的设计确保了标题层级的清晰视觉区分。

### 样式修改经验

1. **样式优先级**:
   * 在 `custom.css` 中修改样式时，如果发现样式不生效，可能是选择器优先级不够。
   * 使用更具体的选择器（如 `.post-header .post-title`）或添加 `!important` 来提高优先级。

2. **响应式设计**:
   * 使用 `@media` 查询来适配移动端显示。
   * 移动端（<768px）通常需要调整字体大小和间距。

3. **统一性原则**:
   * 保持相同类型元素的样式一致，如所有页面的标题大小。
   * 使用变量和规律性的数值（如标题大小每级减小 2px）来维护样式的统一性。

## 日常手动更新博客要注意的点

您只需要关注以下几个步骤即可轻松更新您的博客：

1. **撰写文章**:
    * 博客文章使用 Markdown 格式编写，请将 Markdown 文件放在 `content/posts/` 目录下。
    * **文件名命名规范**：
        * **使用英文**：文件名请使用英文单词，避免使用拼音。
        * **使用短横线分隔**： 单词之间使用短横线 `-` 分隔，例如 `my-second-post.md` 或 `how-to-insert-image.md`。
    * 例如，如果您要写一篇名为 `my-second-post.md` 的文章，就将其放在 `content/posts/` 文件夹中。

2. **插入图片**:
    * 如果您需要在文章中插入图片，请将图片文件放在 `static/images/` 目录下。
    * 然后在 Markdown 文件中使用 Markdown 语法引用图片，例如 `![图片描述](/images/your-image.jpg)`。

3. **提交更新**:
    * 完成文章撰写和图片添加后，将 `content/posts/` 和 `static/images/` 目录下的更改提交到 GitHub 仓库。
    * Cloudflare Pages 会自动检测到 GitHub 仓库的更新，并重新构建和部署您的博客。

## 依据导出的 Notion ZIP 压缩包来更新博文的规则

这些 Markdown 和附件通常是从 Notion 导出的 ZIP 压缩包，建议将 ZIP 文件先放在 `temp_files` 目录下。

请按照以下关键步骤来帮助更新至当前的 Blog 格式：

1.  **定位并解压 Notion ZIP 包**：
    *   当用户指示处理 Notion ZIP 文件时，AI 助手将假定 `temp_files` 目录下已存在**唯一一个**待处理的 Notion ZIP 压缩包。
    *   AI 助手会自动扫描 `temp_files` 目录，找出该 ZIP 文件。
    *   然后使用 `scripts/extract_zip_utf8.py` 脚本来解压 ZIP 文件。这个脚本会处理文件名中的特殊字符，并将内容解压到 `temp_notion/以ZIP包名命名的目录/`。
        ```bash
        # AI 会自动替换 "你的Notion导出.zip" 为实际扫描到的文件名
        python3 scripts/extract_zip_utf8.py temp_files/你的Notion导出.zip
        ```
    *   AI 助手会浏览解压后的文件，通常包含一个主 Markdown 文件和存放附件（图片等）的文件夹。

2.  **确定文章标题和主 Markdown 文件**：
    *   AI 助手会根据解压后的文件名或内容，和您一起确认主 Markdown 文件及其文章标题。

3.  **创建 Markdown 文件**：
    *   在 `content/posts/` 目录下，AI 会创建一个以文章标题命名的 Markdown 文件（文件名要求是英文单词，用短横线分隔，不要使用拼音）。

4.  **添加 Frontmatter**：
    *   AI 会在新文件的开头添加必要的 Frontmatter 元数据，包括：
        *   `title`：文章标题（来自 Notion 或您提供）
        *   `date`：发布日期为今天，请使用指令 `$ date +%Y-%m-%d` 获取当前日期，不要使用 AI 数据库的日期
        *   `draft`：是否为草稿，默认 `false`
        *   `description`：文章简短描述（可从 Notion 内容提取或您提供）
        *   `tags`：只能从预定义标签列表中选择合适的标签（参考"博客元数据格式规范"章节中的标签列表）
        *   `author`：作者信息 (默认为 "Joe")
    *   每次生成新的博客文件时，请参考 `@nezha-movie-review.md` 文件的格式和元数据进行修正。
    *   YAML 对特殊字符非常敏感，特别是在 Front Matter 中。
    *   在元数据里，使用纯英文引号包裹 YAML 值。
    *   在元数据里，统一使用半角标点符号。

5.  **添加并调整文章正文**：
    *   AI 会将主 Notion Markdown 文件中的正文内容复制到新创建的博客 Markdown 文件中。
    *   **重要**：AI 会协助检查并修正 Notion 特有的 Markdown 格式，例如：
        *   移除或转换 Notion 内部链接。
        *   调整 Callout、Toggle 等 Notion 特有块的显示，使其符合标准 Markdown 或博客主题支持的格式。
        *   清理不必要的 HTML 标签或样式。

6.  **处理并添加图片**：
    *   在 `static/images/posts/` 目录下，创建与文章同名（英文文件名）的目录。
    *   将 Notion 导出的图片（通常在解压后的附件目录中）直接复制到这个新创建的图片目录中。
    *   **重要：不要手动重命名图片文件，也不要手动修改 Markdown 中的图片引用路径**。
    *   按顺序执行以下命令处理图片：
        ```bash
        # 1. 压缩并转换图片为 WebP 格式
        python3 scripts/compress_article_images.py article-name

        # 2. 更新文章中的图片引用为 WebP 格式
        python3 scripts/update_image_refs.py

        # 3. 将压缩后的图片移动到正确位置
        cp -r static/images_compressed/posts/article-name/* static/images/posts/article-name/

        # 4. 清理原始图片文件
        python3 scripts/clean_original_images.py --execute

        # 5. 清理临时文件
        rm -rf static/images_compressed/posts/article-name
        ```
    *   注意事项：
        * 所有图片最终会统一为 WebP 格式
        * 图片引用路径会自动更新为 `/images/posts/article-name/image-name.webp` 格式
        * 在执行清理前，确保 WebP 图片已经正确生成

7.  **最终检查**：
    *   确认所有图片都能正确显示。
    *   检查文章格式是否规范，特别是列表、引用、代码块等。
    *   确保图片描述准确且有意义。
    *   验证文章元数据的准确性，特别是标签是否符合预定义列表。

8.  **检查交叉引用**：
    *   与处理 Obsidian 文件类似，使用 grep 或项目提供的搜索脚本在所有博客文章中搜索当前文章的相关关键词。
        ```bash
        grep -r "关键词" content/posts/
        # 或者
        python3 scripts/grep_search.py "关键词"
        ```
    *   检查其他文章中是否有引用当前文章的链接。
    *   如果发现引用，确保链接格式正确（应为 `/posts/article-name` 格式），修正任何指向 Notion 平台的旧链接，并更新所有相关文章中的引用。
    *   AI 不会主动新增引用，仅修正已发现的错误或不当引用。

9.  **清理原始图片**：
    *   运行 `clean_original_images.py` 脚本来预览并删除已转换为 WebP 且已备份的原始图片（位于 `static/images/posts/article-name/` 目录下，非 WebP 格式的图片）。
        ```bash
        # 预览要删除的原始图片文件
        python3 scripts/clean_original_images.py
        # 确认无误后删除原始图片文件
        python3 scripts/clean_original_images.py --execute
        ```
    *   注意：此脚本主要针对全局图片清理，对于单篇文章，确保只清理对应文章目录下的原始图片。通常 `compress_article_images.py` 和 `update_image_refs.py` 处理后，原始图片（如 .jpg, .png）仍在 `static/images/posts/article-name/`，这些是需要被 `clean_original_images.py` 清理的。

10. **清理所有临时文件**：
    *   清理 Notion 解压的临时目录：`rm -rf temp_notion/以ZIP包名命名的目录` (请替换为实际目录名)
    *   清理图片压缩过程中生成的临时目录：`rm -rf static/images_compressed/posts/article-name`
    *   清理 `temp_files` 目录中已处理的 Notion ZIP 文件：`rm -f temp_files/你的Notion导出.zip` (请替换为实际文件名)

11. **最后，运行自检清单**：
    *   首先，再次确认文章的标签是否都出自预定义的标签列表。
    *   其次，回顾操作记录，确保所有相关的临时文件和目录都已清理干净。

## 依据 Obsidian Markdown 文件来更新博文的规则

这些 Markdown 是从 Obsidian 导出的，包括 Markdown 文件和附件，都放在 `temp_files` 目录下。

请按照以下关键步骤来帮助更新至当前的 Blog 格式：

1. **接收并理解内容**：AI 助手会仔细阅读并理解您提供的文章标题和正文。
2. **创建 Markdown 文件**：在 `content/posts/` 目录下，AI 会创建一个以文章标题命名的 Markdown 文件，要求是英文单词，不要使用拼音。
3. **添加 Frontmatter**：AI 会在新文件的开头添加必要的 Frontmatter 元数据，包括：
   * `title`：文章标题
   * `date`：发布日期为今天，请使用指令 `$ date +%Y-%m-%d` 获取当前日期，不要使用 AI 数据库的日期
   * `draft`：是否为草稿，默认不是草稿
   * `description`：文章简短描述
   * `tags`：只能从预定义标签列表中选择合适的标签（参考"博客元数据格式规范"章节中的标签列表）
   * `author`：作者信息
   每次生成新的博客文件时，请参考 `@nezha-movie-review.md` 文件的格式和元数据进行修正。
   - YAML 对特殊字符非常敏感，特别是在 Front Matter 中
   - 在元数据里，使用纯英文引号包裹 YAML 值
   - 在元数据里，统一使用半角标点符号
4. **添加文章正文**：AI 会将您提供的文章正文内容复制到 Markdown 文件中。
5. **添加图片**：
   - 在 `static/images/posts/` 目录下，创建与文章同名的目录
   - 将原始图片复制到该目录
   - 根据图片内容给予有意义的文件名
   - 使用 `compress_article_images.py` 脚本处理单篇文章的图片：

        ```bash
        python3 scripts/compress_article_images.py article-name
        ```
   - 将压缩后的图片从 `static/images_compressed/posts/article-name/` 复制到 `static/images/posts/article-name/`
   - 运行 `update_image_refs.py` 更新文章中的图片引用为 WebP 格式
   - 注意：这里不要使用 `compress_images.py`，它是用于全站图片批量处理的

   ③ **最终检查**：
      * 确认所有图片都能正确显示
      * 检查文章格式是否规范
      * 确保图片描述准确且有意义
      * 验证文章元数据的准确性

   注意：虽然手动处理会花费更多时间，但能确保更好的质量控制和准确性。对于图片压缩和格式转换，可以使用图形界面工具（如 ImageOptim）来处理。

5. **检查交叉引用**：
   * 使用 grep 或其他搜索工具在所有博客文章中搜索当前文章的相关关键词
   * 检查其他文章中是否有引用当前文章的链接
   * 如果发现引用：
     * 确保链接格式正确（应该是 `/posts/article-name` 格式）
     * 修正任何指向 Notion 或其他外部平台的旧链接
     * 更新所有相关文章中的引用
   * 但是，不要自己新增引用，只修正错误
   * 建议使用以下命令进行搜索：
     ```bash
     # 使用 grep 搜索关键词
     grep -r "关键词" content/posts/
     
     # 或者使用项目提供的搜索脚本
     python3 scripts/grep_search.py "关键词"
     ```

6. 清理原始图片，不要忘了

     ```bash
     # 预览要删除的原始图片文件
     python3 scripts/clean_original_images.py
     
     # 确认无误后删除原始图片文件
     python3 scripts/clean_original_images.py --execute
     ```

   * 这一步会删除已经转换为 WebP 格式的原始图片文件
   * 注意：网站图标文件（如 android-chrome-*.png、apple-touch-icon.png 等）会自动保护，不会被删除

7. **清理所有临时文件**：
   * 清理临时解压目录：`rm -rf temp_notion/*`
   * 清理临时压缩图片：`rm -rf static/images_compressed/posts/article-name`
   * 清理已处理的草稿 zip 文件：`rm -f temp_files/*.zip`

8. 最后，运行自检清单
   首先，一定要先读一下预定义的标签列表，看看标签是否出自列表
   其次，看看操作记录是否清理了所有的临时文件

## 手动增加 Thought (随想) 的方法

Thought (随想) 是一种更简短、随性的内容形式，通常没有正式的标题。您可以通过以下两种方式添加 Thought：

### 1. 直接粘贴内容

如果您想快速记录一些文字，可以直接创建一个 Markdown 文件：

1.  **创建 Markdown 文件**：
    *   在 `content/thoughts/` 目录下创建一个新的 `.md` 文件。 
    *   **文件名命名规范**：建议使用简短描述，确保英文且用短横线分隔，例如 `my-random-thought.md`。

2.  **添加 Frontmatter (元数据)**：
    *   在文件开头添加必要的 Frontmatter。由于 Thought 没有正式标题，`title` 字段需要去掉。
    *   **重要**：`tags` 必须从本文档 "Blog 元数据格式规范" 章节中预定义的标签列表选择。
    *   获取当前日期给 `date` 字段，可以在终端运行 `$ date +%Y-%m-%d`。
    *   示例：
        ```yaml
        ---
        author: "Joe"
        date: "2024-03-15"  # 使用实际日期
        description: "这里填写对这个 Thought 的简短描述" 
        draft: false
        tags: ["生活感悟"] # 从预定义列表选择
        title: "" # Thought 通常没有标题，可以留空
        ---
        ```
        *   请参照 "Blog 元数据格式规范" 确保其他元数据（如 `author`, `description`, `draft`）的正确性，并使用英文引号包裹字符串类型的值。

3.  **添加内容**：
    *   在 Frontmatter下方粘贴或撰写您的 Thought 内容。

4.  **处理图片 (如果需要)**：
    *   如果 Thought 中包含图片，首先在 `static/images/thoughts/` 目录下，创建与 Thought Markdown 文件名对应的目录（例如，如果 Markdown 文件是 `my-random-thought.md`，则图片目录为 `static/images/thoughts/my-random-thought/`）。将原始图片放入此目录。
    *   然后按照以下步骤处理图片 (假设 Thought 的文件名为 `thought-file-name.md`，对应图片目录 `thought-file-name`)：
        ```bash
        # 1. 压缩并转换图片为 WebP 格式 (将 thought-file-name 替换为实际的文件名，不含扩展名)
        python3 scripts/compress_article_images.py thoughts/thought-file-name

        # 2. 更新文章中的图片引用为 WebP 格式 (此脚本会扫描并更新所有引用)
        python3 scripts/update_image_refs.py

        # 3. 将压缩后的图片移动到正确位置
        # 注意：compress_article_images.py 会将图片输出到 static/images_compressed/thoughts/thought-file-name/
        cp -r static/images_compressed/thoughts/thought-file-name/* static/images/thoughts/thought-file-name/

        # 4. 清理原始图片文件 (此脚本会全局扫描并清理可被 WebP 替代的原始图)
        python3 scripts/clean_original_images.py --execute

        # 5. 清理本次压缩产生的临时文件
        rm -rf static/images_compressed/thoughts/thought-file-name
        ```
    *   **注意**：执行 `compress_article_images.py` 时，参数 `thoughts/thought-file-name` 指的是图片存放的相对路径和目录名。请确保这些脚本存在且具有执行权限。

### 2. 通过 Notion 导出的 ZIP 文件

如果您从 Notion 导出 Thought 内容为 ZIP 文件，可以参考以下步骤，这与处理普通博文的 Notion ZIP 文件类似，但针对 Thought 的特性有所调整：

1.  **接收并解压 Notion ZIP 包**：
    *   将 Notion ZIP 文件放在 `temp_files` 目录下。
    *   使用 `scripts/extract_zip_utf8.py` 脚本解压：
        ```bash
        python3 scripts/extract_zip_utf8.py temp_files/你的Notion导出.zip
        ```
    *   内容会解压到 `temp_notion/以ZIP包名命名的目录/`。

2.  **确定主 Markdown 文件**：
    *   在解压后的文件中找到主 Markdown 文件。

3.  **创建 Markdown 文件**：
    *   在 `content/thoughts/` 目录下创建一个 Markdown 文件。 （如果 `content/thoughts/` 目录不存在，请先创建它。）
    *   **文件名命名规范**：使用英文单词和短横线，例如根据内容命名，如 `a-quick-reflection.md` 或 `notion-thought.md`。将其记为 `thought-file-name.md`。

4.  **添加 Frontmatter**：
    *   在新文件开头添加元数据：
        *   `date`：发布日期（例如，可在终端运行 `$ date +%Y-%m-%d` 获取当天日期后填入）
        *   `draft`: `false` (除非确实是草稿)
        *   `description`：Thought 的简短描述。
        *   `tags`：**必须**从 "Blog 元数据格式规范" 中预定义的标签列表选择。
        *   `author`: "Joe"
    *   示例：
        ```yaml
        ---
        author: "Joe"
        date: "2024-03-15"
        description: "从 Notion 导入的随想"
        draft: false
        tags: ["生活感悟"]
        title: ""
        ---
        ```

5.  **添加并调整文章正文**：
    *   将 Notion Markdown 文件中的正文内容复制到新创建的 Thought Markdown 文件 (`content/thoughts/thought-file-name.md`) 中。
    *   修正 Notion 特有的 Markdown 格式（如内部链接、Callout 等），使其符合标准 Markdown。

6.  **处理并添加图片**：
    *   在 `static/images/thoughts/` 目录下，创建与 Thought Markdown 文件名对应的目录（即 `thought-file-name`）。
    *   将 Notion 导出的图片（通常在解压后的附件目录中）直接复制到这个新创建的图片目录中 (`static/images/thoughts/thought-file-name/`)。
    *   **重要：不要手动重命名图片文件，也不要手动修改 Markdown 中的图片引用路径**，脚本会自动处理。
    *   按顺序执行以下命令处理图片 (将 `thought-file-name` 替换为实际的文件名，不含扩展名)：
        ```bash
        # 1. 压缩并转换图片为 WebP 格式
        python3 scripts/compress_article_images.py thoughts/thought-file-name

        # 2. 更新 Thought 中的图片引用为 WebP 格式 (全局更新)
        python3 scripts/update_image_refs.py

        # 3. 将压缩后的图片移动到正确位置
        cp -r static/images_compressed/thoughts/thought-file-name/* static/images/thoughts/thought-file-name/

        # 4. 清理原始图片文件 (全局清理)
        python3 scripts/clean_original_images.py --execute

        # 5. 清理本次压缩产生的临时文件
        rm -rf static/images_compressed/thoughts/thought-file-name
        ```

7.  **最终检查**：
    *   确认所有图片都能正确显示。
    *   检查文章格式是否规范，特别是列表、引用、代码块等。
    *   确保图片描述准确且有意义。
    *   验证文章元数据的准确性，特别是标签是否符合预定义列表。

8.  **检查交叉引用 (如果适用)**：
    *   Thought 可能较少被其他长文正式引用。如果需要，可使用 `grep -r "关键词" content/` 或 `python3 scripts/grep_search.py "关键词"` 在所有内容中搜索相关关键词，检查并修正链接。

9.  **清理所有临时文件**：
    *   清理 Notion 解压的临时目录：`rm -rf temp_notion/以ZIP包名命名的目录` (请替换为实际目录名)
    *   清理 `temp_files` 目录中已处理的 Notion ZIP 文件：`rm -f temp_files/你的Notion导出.zip` (请替换为实际文件名)

10. **自检清单**：
    *   首先，再次确认文章的标签是否都出自预定义的标签列表。
    *   其次，回顾操作记录，确保所有相关的临时文件和目录都已清理干净。

## 全局图片压缩的方法

为了优化网站加载速度和存储空间，我们需要定期对图片进行压缩处理和 WebP 转换。以下是具体的压缩流程：

### 压缩工具和参数

- 使用项目根目录下的 `compress_images.py` 脚本进行图片压缩和 WebP 转换
* 脚本会自动处理 `static` 目录下的所有图片（包括子目录）
* 网站图标相关文件（favicon、apple-touch-icon、android-chrome）会保持原格式
* 压缩参数：
  * 质量：85%（可在脚本中调整 quality 参数）
  * 最大尺寸：1920x1920（保持原比例）
  * 自动移除图片元数据
  * 自动转换为 WebP 格式（PNG 使用无损压缩，JPG 使用有损压缩）

### 完整压缩流程

1. **安装依赖**：

   ```bash
   brew install imagemagick
   ```

2. **运行压缩脚本**：

   ```bash
   python3 scripts/compress_images.py
   ```

   这会在项目根目录创建 `static_compressed` 目录，存放压缩后的文件。

3. **复制压缩后的文件**：

   ```bash
   cp -r static_compressed/* static/
   ```

   这一步会将压缩后的文件复制回原目录，同时保留原始文件作为备份。

4. **更新图片引用**：

   ```bash
   python3 scripts/update_image_refs.py
   ```

   这一步会自动将所有 Markdown 文件中的图片引用更新为 WebP 格式。
   例如：`![示例图片](/images/example.jpg)` 会被更新为 `![示例图片](/images/example.webp)`

5. **预览要删除的原始文件**：

   ```bash
   python3 scripts/clean_original_images.py
   ```

   这一步会显示哪些原始文件将被删除，以及可以节省的空间大小。

6. **确认无误后删除原始文件**：

   ```bash
   python3 scripts/clean_original_images.py --execute
   ```

   这一步会删除已经转换为 WebP 格式的原始图片文件，但会保留网站图标相关文件。

7. **清理临时文件**：

   ```bash
   # 清理 Notion 处理的临时文件
   rm -rf temp_notion
   rm -f temp_files/*.zip
   
   # 清理图片压缩的临时目录
   rm -rf static_compressed
   rm -rf static/images_compressed
   ```

## 图片引用的自检方法

为了确保博客中的所有图片引用都是有效的，我们提供了一个专门的检查脚本。这个工具可以帮助您：
1. 检测所有 Markdown 文件中的图片引用
2. 验证每个图片文件是否存在
3. 识别外部链接和失效的图片引用

### 运行检查

使用以下命令运行图片引用检查：

```bash
python3 scripts/check_image_refs.py
```

### 检查内容

脚本会检查以下内容：
1. **Markdown 文件**：扫描 `content` 目录下所有的 `.md` 文件
2. **图片引用**：查找所有使用 Markdown 图片语法的引用 `![alt text](/path/to/image)`
3. **文件存在性**：验证每个引用的图片在 `static` 目录中是否存在
4. **URL 编码处理**：自动处理包含空格或特殊字符的文件名
5. **外部链接识别**：区分并标记外部图片链接（以 http:// 或 https:// 开头）

### 检查结果

脚本会输出详细的检查报告，包括：
1. 每个文件的检查结果
2. 成功的图片引用（显示为绿色）
3. 失败的图片引用（显示为红色）
4. 外部链接（单独列出）

### 统计信息

检查完成后会显示统计信息：
- 检查的 Markdown 文件总数
- 发现的图片引用总数
- 外部链接数量
- 失效的图片引用数量

### 常见问题处理

1. **找不到图片文件**：
   * 检查文件是否已经转换为 WebP 格式
   * 验证文件路径是否正确
   * 确认文件名大小写是否匹配

2. **URL 编码问题**：
   * 检查文件名中的空格是否正确编码
   * 验证特殊字符是否正确处理
   * 考虑重命名文件，避免使用特殊字符

3. **批量修复**：
   * 使用 `update_image_refs.py` 更新图片引用
   * 使用 `compress_images.py` 处理图片格式
   * 使用 `clean_original_images.py` 清理原始图片

通过定期运行图片引用检查，可以及时发现和解决潜在的问题，确保博客内容的完整性和可访问性。

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
     * `书影音的精神角落`：看书、看影视剧的记录
     * `我有个想法！`：生活或工作上的灵感
     * `江浙沪包游`：江浙沪地区的旅行记录
     * `提升幸福感的好物`：包括软件和硬件提升幸福感的内容
     * `折腾软硬件`：软件和数码硬件相关的折腾
     * `游戏也是场冒险`：游戏体验记录
     * `小城故事`：老家的故事
     * `阅读笔记`：书籍或文章阅读的笔记
     * `现实是个开放世界`：所有地方的旅行日记（包括江浙沪地区）
     * `工作感悟`：工作相关的总结
     * `生活感悟`：生活相关的感悟
     * `骑行`：骑行相关的内容
     * `AI`：与 AI 相关的内容
     * `Vibe Coding`：与 AI 编程相关的感悟

4. **字段顺序**：
   * 建议按照 author、date、description、draft、tags、title 的顺序排列
   * 保持所有文章的字段顺序一致

5. **其他注意事项**：
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

为了提供更好的阅读体验，博客支持两种链接样式：

### 1. Bookmark 样式链接

适用于需要突出显示的重要外部链接，使用 `link` shortcode：

```markdown
{{< link "https://example.com" "链接标题" >}}
```

这会渲染出一个美观的 Bookmark 卡片，包含：
- 链接标题
- 完整 URL
- 视觉指示器（外部链接图标）

使用场景：
- 文章主要推荐的外部资源
- 需要特别强调的参考资料
- 独立成段的重要链接

### 2. 普通链接

适用于行内引用或列表中的链接，使用标准 Markdown 语法：

```markdown
[文章标题](/posts/article-name)
[外部链接标题](https://example.com)
```

使用场景：
- 文章间的内部引用
- 列表项中的链接
- 段落内的行内链接
- 参考资料列表中的链接


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

## 许可证说明

本仓库采用双重许可证模式：

1. **博客内容**：所有博客文章内容（包括文字、图片等）采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可证。
2. **代码部分**：所有代码文件采用 [MIT](https://opensource.org/licenses/MIT) 许可证。

详细的许可说明请查看 [LICENSE.md](LICENSE.md) 文件。

## 图片处理的标准流程

为了确保博客图片的一致性和质量，请严格按照以下步骤处理图片：

### 1. 准备工作
- 确保原始图片已经放在正确的目录：`static/images/posts/article-name/`
- **不要手动重命名图片文件**，让脚本来处理格式转换
- **不要手动修改 Markdown 中的图片引用**，让脚本来更新

### 2. 执行图片处理（按顺序执行）
```bash
# 1. 压缩并转换图片为 WebP 格式
python3 scripts/compress_article_images.py article-name

# 2. 更新文章中的图片引用为 WebP 格式
python3 scripts/update_image_refs.py

# 3. 将压缩后的图片移动到正确位置
cp -r static/images_compressed/posts/article-name/* static/images/posts/article-name/

# 4. 清理原始图片文件
python3 scripts/clean_original_images.py --execute

# 5. 清理临时文件
rm -rf static/images_compressed/posts/article-name
```

### 3. 注意事项
- 脚本会自动处理图片压缩和格式转换
- 脚本会保护网站图标等特殊图片文件
- 所有图片最终会统一为 WebP 格式
- 图片引用路径统一为 `/images/posts/article-name/image-name.webp`
- 在执行清理前，确保 WebP 图片已经正确生成

### 4. 图片命名建议
虽然文件名最终会被脚本处理，但建议在准备原始图片时遵循以下命名规范：
- 使用有意义的英文名称
- 使用短横线分隔单词
- 避免使用空格和特殊字符
- 示例：`cycling-route-overview.jpg` 而不是 `image1.jpg`