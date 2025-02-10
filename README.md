# 我的个人博客 -  《Joe 的折腾日记》  (基于 Hugo + Cloudflare Pages)

这个博客使用 Hugo 静态网站生成器构建，并托管在 Cloudflare Pages 上。

## 当前博客构建方式

*   **Hugo**: 负责将 Markdown 内容转换为静态网页。
*   **Cloudflare Pages**:  提供网站托管、CDN 加速和自动部署。
*   **GitHub**:  用于存储博客源代码和版本管理。

## 博客样式定制

博客使用了 PaperMod 主题，并进行了一些自定义样式调整。所有的自定义样式都在 `assets/css/extended/custom.css` 文件中。

### 标题样式规范

为了保持整个博客的视觉一致性，我们采用了以下标题大小规范：

1. **文章标题**: 24px（与首页博客列表标题大小保持一致）
2. **文章内容标题**:
   - h1: 24px（与文章标题相同）
   - h2: 22px（比 h1 小 2px）
   - h3: 20px（比 h2 小 2px）
   - h4: 18px（比 h3 小 2px）
   - h5: 16px（比 h4 小 2px）
   - h6: 14px（比 h5 小 2px）

这种递减的设计确保了标题层级的清晰视觉区分。

### 样式修改经验

1. **样式优先级**:
   - 在 `custom.css` 中修改样式时，如果发现样式不生效，可能是选择器优先级不够。
   - 使用更具体的选择器（如 `.post-header .post-title`）或添加 `!important` 来提高优先级。

2. **响应式设计**:
   - 使用 `@media` 查询来适配移动端显示。
   - 移动端（<768px）通常需要调整字体大小和间距。

3. **统一性原则**:
   - 保持相同类型元素的样式一致，如所有页面的标题大小。
   - 使用变量和规律性的数值（如标题大小每级减小 2px）来维护样式的统一性。

## 日常更新博客

您只需要关注以下几个步骤即可轻松更新您的博客：

1.  **撰写文章**:
    *   博客文章使用 Markdown 格式编写，请将 Markdown 文件放在 `content/posts/` 目录下。
    *   **文件名命名规范**：
        *   **使用英文**：文件名请使用英文单词，避免使用拼音。
        *   **使用短横线分隔**： 单词之间使用短横线 `-` 分隔，例如 `my-second-post.md` 或 `how-to-insert-image.md`。
    *   例如，如果您要写一篇名为 `my-second-post.md` 的文章，就将其放在 `content/posts/` 文件夹中。

2.  **插入图片**:
    *   如果您需要在文章中插入图片，请将图片文件放在 `static/images/` 目录下。
    *   然后在 Markdown 文件中使用 Markdown 语法引用图片，例如 `![图片描述](/images/your-image.jpg)`。

3.  **提交更新**:
    *   完成文章撰写和图片添加后，将 `content/posts/` 和 `static/images/` 目录下的更改提交到 GitHub 仓库。
    *   Cloudflare Pages 会自动检测到 GitHub 仓库的更新，并重新构建和部署您的博客。

## 本地构建和调试

在您提交更新之前，您可以在本地电脑上预览博客效果，确保一切正常：

1.  **安装 Hugo**:  请确保您已经在本机安装了 Hugo (具体安装步骤请参考 [Hugo 官方文档](https://gohugo.io/getting-started/installing/))。

2.  **本地预览**:
    *   打开命令行终端，进入您的博客项目根目录。
    *   运行命令 `hugo server -D`。
    *   Hugo 将会在本地启动一个开发服务器，您可以通过浏览器访问 `http://localhost:1313/` 来预览您的博客。
    *   `-D` 参数表示同时构建 `draft` (草稿) 状态的文章，方便您预览尚未正式发布的文章。

3.  **停止预览**:
    *   在命令行终端中按下 `Ctrl + C` 即可停止本地 Hugo 开发服务器。

## AI 助手更新博客的关键步骤

当您提供博客文章内容给 AI 助手时，AI 将执行以下关键步骤来帮助您更新博客：

1. **接收并理解内容**：AI 助手会仔细阅读并理解您提供的文章标题和正文。
2. **创建 Markdown 文件**：在 `content/posts/` 目录下，AI 会创建一个以文章标题命名的 Markdown 文件。
3. **添加 Frontmatter**：AI 会在新文件的开头添加必要的 Frontmatter 元数据，包括 `title`, `date`, `draft`, `description`, `tags`, `author` 等字段，并根据文章内容进行合理设置。每次生成新的博客文件时，请参考 `@nezha-movie-review.md` 文件的格式和元数据进行修正。
4. **添加文章正文**：AI 会将您提供的文章正文内容复制到 Markdown 文件中。

### 使用 AI 助手更新博客的注意事项

1. **文件命名规则**：
   - 文件名必须使用英文，不能使用中文或拼音
   - 单词之间使用短横线（-）连接
   - 避免在文件名中使用空格、特殊字符或换行符
   - 示例：`my-first-blog-post.md`

2. **日期设置规则**：
   - 文章的日期格式必须是 `YYYY-MM-DD`（例如：`2025-02-03`）
   - 保持原始数据中的日期不变，不要随意修改年份
   - 如果是从其他平台迁移的文章，应保留原文的创建日期
   - 对于新文章，使用实际的发布日期（当前日期是 2025-02-10）
   - 日期可以是过去的日期，也可以是未来的日期（未来日期的文章会在到期日自动发布）
   - 建议将重要或置顶文章的日期设置为未来日期

3. **Front Matter 规范**：
   ```yaml
   ---
   title: "文章标题"
   date: 2025-02-10
   draft: false
   description: "文章描述，建议 100 字以内"
   tags: ["标签1", "标签2"]
   author: "Joe"
   ---
   ```

4. **本地预览和部署步骤**：
   - 每次更新后运行 `hugo --cleanDestinationDir` 清理缓存
   - 使用 `hugo server -D` 启动本地预览
   - 确认文章在博客列表和首页都正常显示
   - 检查文章内容、格式和样式是否正确
   - 确认无误后提交到 GitHub，等待自动部署

5. **常见问题处理**：
   - 如果文章没有显示在列表中，检查：
     * 文件名是否包含特殊字符或换行符
     * front matter 格式是否正确
     * 日期设置是否合理
     * draft 状态是否正确
   - 如果样式显示异常，检查：
     * Markdown 语法是否正确
     * 是否误用了特殊字符
     * 图片路径是否正确

6. **图片处理规则**：
   - 图片文件必须放在 `static/images/` 目录下
   - 图片文件名同样使用英文和短横线
   - 在文章中使用相对路径引用图片：`![描述](/images/your-image.jpg)`
   - **图片压缩**：
     * 使用项目根目录下的 `compress_images.py` 脚本进行图片压缩
     * 脚本会自动处理 `static/images/` 目录下的所有图片
     * 压缩后的图片保存在 `static/images_compressed/` 目录
     * 压缩参数：
       - 质量：85%（可在脚本中调整 quality 参数）
       - 最大尺寸：1920x1920（保持原比例）
       - 自动移除图片元数据
     * 使用方法：
       ```bash
       # 安装依赖
       brew install imagemagick
       # 运行压缩脚本
       python compress_images.py
       ```
     * 压缩完成后，可以比较原始目录和压缩后目录的大小：
       ```bash
       du -sh static/images static/images_compressed
       ```
     * 确认压缩效果后，可以将压缩后的图片替换原始图片

7. **标签管理规则**：
   - 使用已有的标签，避免创建过多相似的标签
   - 标签使用中文，便于读者理解
   - 每篇文章建议使用 3-5 个标签
   - 标签应该反映文章的主要主题和分类

---

**提示**:

*   每次修改博客内容后，都建议先在本地预览，确保没有问题后再提交到 GitHub。
*   如果您想要了解更多关于 Hugo 和 Cloudflare Pages 的使用方法，可以查阅它们的官方文档。

### 从 Notion 导出文件的处理流程

1. **准备工作**：
   - 在 Notion 中选择要导出的页面
   - 选择导出格式为 "Markdown & CSV"
   - 确保导出时包含图片

2. **文件处理步骤**：
   - 将导出的 ZIP 文件放在 `Notionfiles` 目录下
   - 运行 `extract_zip.py` 解压所有 ZIP 文件
   - 运行 `process_notion_files.py` 处理解压后的文件
   - 运行 `compress_images.py` 压缩处理后的图片

3. **自动化处理内容**：
   - 提取文章标题、标签、创建日期等信息
   - 生成符合 Hugo 格式的 Front Matter
   - 创建文章专属的图片目录
   - 处理图片文件名和链接
   - 自动清理已处理的源文件

4. **注意事项**：
   - 确保 Python 环境已安装 `pyyaml` 包：`pip3 install pyyaml`
   - 确保已安装 ImageMagick：`brew install imagemagick`
   - 图片会被自动压缩并限制最大尺寸为 1920x1920
   - 处理完成后源文件会被自动删除
   - 如果文章已存在，将会跳过处理

5. **处理后的文件结构**：
   ```
   content/
   └── posts/
       └── article-title.md
   static/
   └── images/
       └── posts/
           └── article-title/
               ├── image-1.jpg
               ├── image-2.png
               └── ...
   ```

### 从 Notion 自动化迁移内容到当前博客

## 自动化迁移技术方案 (开发者参考)

本博客的 Notion 文章自动化迁移功能，由以下技术方案实现，供开发者参考：

**核心编程语言**：**Python**

**主要依赖库**：

*   `zipfile`:  用于解压和处理 Notion 导出的 ZIP 文件。
*   `frontmatter`:  用于解析和操作 Markdown 文件中的 Frontmatter 元数据。
*   `re` (正则表达式):  用于进行文本内容匹配、替换和格式化，例如清理 Notion 特殊语法、转换代码块等。
*   `datetime`:  用于处理日期和时间信息，特别是 Notion 页面的创建时间。
*   `os` 和 `shutil`:  用于文件和目录操作，例如创建目录、移动文件、重命名文件等。

**核心处理流程**：

1.  **ZIP 文件解压**：使用 `zipfile` 库解压用户提供的 ZIP 文件，获取 Notion 导出的 Markdown 文件和图片资源。
2.  **Markdown 文件解析**：
    *   遍历解压后的目录，识别 Markdown 文件。
    *   使用 `frontmatter` 库加载 Markdown 文件，解析 Frontmatter 元数据和正文内容。
3.  **元数据提取与转换**：
    *   从 Markdown 文件名或特定文件中尝试提取文章标题。
    *   **关键步骤**：解析 Notion 导出文件中的元数据信息（例如 CSV 文件或 JSON 文件，如果 Notion 导出包含），尝试获取页面的原始创建时间 `created_time`。
    *   构建符合 Hugo Frontmatter 规范的元数据，包括 `title`, `date` (设置为提取到的创建时间), `draft`, `description`, `tags`, `author` 等字段。
4.  **内容清洗与转换**：
    *   **Notion 语法清理**：使用正则表达式 (`re`) 清理 Notion 特有的 Markdown 语法，例如移除公式块、调整代码块语法等，确保内容与 Hugo 兼容。
    *   **图片路径替换**：
        *   识别 Markdown 内容中的图片引用链接，通常是 Notion 的 S3 链接或本地相对路径。
        *   将图片下载或复制到 Hugo 项目的 `static/images/posts/{文章英文标题}/` 目录下。
        *   将 Markdown 中的图片引用路径更新为 Hugo 博客的相对路径格式，例如 `![图片描述](/images/posts/{文章英文标题}/image.jpg)`。
5.  **Hugo Markdown 文件生成**：
    *   使用 `frontmatter` 库，将清洗转换后的 Markdown 内容和构建的 Frontmatter 元数据重新组合，生成符合 Hugo 格式的 Markdown 文件。
    *   将生成的 Markdown 文件保存到 `content/drafts/` 目录下，等待用户进一步编辑和发布。
6.  **生成迁移报告**：
    *   记录每个文件的处理状态，包括成功处理的文件名、图片数量、提取到的创建时间等信息。
    *   如果处理过程中发生任何错误或异常，记录错误信息，方便问题排查和用户参考。
    *   将迁移报告输出为文本文件或 Markdown 文件，与迁移结果一起提供给用户。

**用户操作透明化**：

整个自动化迁移过程，用户只需提供 Notion 导出的 ZIP 文件，无需手动运行任何脚本或进行复杂配置。AI 助手在后台完成所有技术处理，并将最终结果以 Hugo 博客文件的形式交付给用户，实现真正的 "一键迁移" 体验。

---