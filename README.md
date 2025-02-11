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
   title: '标题（如果标题中包含引号，外层使用单引号）'  # 例如：'扑克牌"干瞪眼"的规则'
   date: YYYY-MM-DD  # 使用 Notion 文章的原始创建日期
   draft: false
   description: "文章描述，建议 100 字以内"
   tags: ["标签1", "标签2"]
   author: "Joe"
   ---
   ```
   - **Front Matter 中引号使用规范**：
     * 如果字符串中包含双引号，外层必须使用单引号，例如：`title: '包含"引号"的标题'`
     * 如果字符串中包含单引号，外层使用双引号，例如：`title: "包含'引号'的标题"`
     * 如果字符串中既有单引号又有双引号，使用单引号包裹，内部的单引号需要转义，例如：`title: '包含''单引号''和"双引号"的标题'`
     * 如果字符串不包含任何引号，可以不加引号（但建议始终加上引号保持一致性）

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

7. **标签管理规则**：
   - 使用已有的标签，避免创建过多相似的标签
   - 标签使用中文，便于读者理解
   - 每篇文章建议使用 3-5 个标签
   - 标签应该反映文章的主要主题和分类

## 图片压缩指南

为了优化网站加载速度和存储空间，我们需要定期对图片进行压缩处理和 WebP 转换。以下是具体的压缩方法：

### 压缩工具和参数
- 使用项目根目录下的 `compress_images.py` 脚本进行图片压缩和 WebP 转换
- 脚本会自动处理 `static/images/` 目录下的所有图片
- 压缩后的图片保存在 `static/images_compressed/` 目录
- 压缩参数：
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
   python compress_images.py
   ```

3. **确认压缩效果**：
   ```bash
   # 比较原始目录和压缩后目录的大小
   du -sh static/images static/images_compressed
   ```

4. **更新图片引用**：
   ```bash
   # 更新 Markdown 文件中的图片引用为 WebP 格式
   python update_image_refs.py
   ```

5. **替换原图**：
   ```bash
   # 将压缩后的图片替换原始图片
   cp -r static/images_compressed/* static/images/
   
   # 删除临时的压缩目录
   rm -rf static/images_compressed
   ```

6. **清理临时文件**：
   ```bash
   # 清理 macOS 系统生成的临时文件
   find . -name ".DS_Store" -delete
   ```

### 注意事项
- 建议每月定期对新增图片进行批量压缩
- 压缩前建议先备份原始图片
- 如果压缩后的图片质量不理想，可以在脚本中调整 quality 参数
- 对于某些特殊图片（如透明背景的 PNG），脚本会自动使用无损 WebP 压缩
- 替换原图前，请确保已经检查过压缩后图片的质量

### WebP 格式说明
1. **优势**：
   - 比 JPEG 格式小 25-35%，比 PNG 格式小 25-80%
   - 支持有损和无损压缩
   - 支持透明度（像 PNG）
   - 支持动画（像 GIF）
   - 浏览器兼容性好（现代浏览器都支持）

2. **压缩策略**：
   - JPG/JPEG 图片：使用有损压缩，质量设置为 85%
   - PNG 图片：使用无损压缩，保证清晰度
   - 其他格式：自动选择合适的压缩方式

3. **文件命名**：
   - 压缩后的文件将自动更改扩展名为 .webp
   - 原始文件名保持不变，仅改变扩展名
   - 例如：`image.jpg` -> `image.webp`

4. **兼容性处理**：
   - 现代浏览器（Chrome、Firefox、Safari、Edge）都支持 WebP
   - 移动端（iOS 14+ 和 Android）也都支持 WebP
   - 如果需要兼容更老的浏览器，建议保留原始图片作为备份

### 工作流程建议
1. **新增图片时**：
   - 将原始图片放入 `static/images/` 对应目录
   - 运行压缩脚本进行处理
   - 使用 `update_image_refs.py` 更新引用
   - 确认效果后替换原图

2. **批量处理时**：
   - 每月底对所有新增图片进行批量处理
   - 检查压缩效果和图片质量
   - 更新所有相关文章的引用
   - 记录压缩前后的空间节省情况

3. **特殊情况处理**：
   - 如果某些图片需要保持原格式，可以手动跳过
   - 对于重要的展示图片，可以适当提高压缩质量
   - 如果发现某些图片显示异常，可以选择保留原格式

### 图片处理规则

为了确保图片处理的一致性和避免误操作，请严格按照以下步骤处理图片：

1. **创建文章专属图片目录**：
   ```bash
   # 使用文章的英文名创建目录
   article_name="your-article-name"  # 例如：cycling-adventure
   mkdir -p "static/images/posts/$article_name"
   ```

2. **复制并重命名图片**：
   ```bash
   # 进入临时目录
   cd temp_notion/your-notion-folder
   
   # 重命名并复制图片（避免空格，使用连字符）
   counter=1
   for img in *.*; do
     if [[ "$img" =~ \.(jpg|jpeg|png|PNG|JPG|JPEG)$ ]]; then
       ext="${img##*.}"
       new_name="image-$counter.$ext"
       cp "$img" "../../static/images/posts/$article_name/$new_name"
       echo "Copied $img to $new_name"
       counter=$((counter + 1))
     fi
   done
   cd ../../
   ```

3. **压缩当前文章的图片**：
   ```bash
   # 重要：只压缩当前文章的图片目录
   python compress_images.py \
     "static/images/posts/$article_name" \
     "static/images_compressed/posts/$article_name"
   ```

4. **更新压缩后的图片**：
   ```bash
   # 只压缩更新当前文章的图片
   cp "static/images_compressed/posts/$article_name/"*.webp \
     "static/images/posts/$article_name/"
   ```

5. **清理临时文件**：
   ```bash
   # 只删除当前文章的临时压缩目录
   rm -rf "static/images_compressed/posts/$article_name"
   ```

### 注意事项

1. **严格遵循目录结构**：
   - 每篇文章的图片必须放在其专属目录：`static/images/posts/article-name/`
   - 不要在根目录或其他文章目录中处理图片

2. **图片压缩原则**：
   - 每次只处理一篇文章的图片
   - 使用文章专属的输入输出目录
   - 不要使用项目根目录作为压缩目标

3. **避免常见错误**：
   - ❌ 不要直接压缩 `static/images` 目录
   - ❌ 不要在一次操作中处理多篇文章的图片
   - ❌ 不要使用通用的临时目录

4. **最佳实践**：
   - ✅ 始终使用文章的英文名作为目录名
   - ✅ 在处理新文章前清理之前的临时文件
   - ✅ 压缩完成后立即验证图片质量

5. **文件命名规范**：
   - 图片文件名格式：`image-1.webp`, `image-2.webp` 等
   - 不使用原始文件名，避免中文和特殊字符
   - 统一使用小写字母和数字

6. **质量控制**：
   - 压缩后的图片大小不应超过原图
   - WebP 格式的质量参数统一设置为 85%
   - 压缩后要检查图片是否正常显示

通过严格遵循这些规则，可以确保：
- 每篇文章的图片都被正确处理
- 避免误操作影响其他文章的图片
- 保持项目的整洁和一致性

---

**提示**:

*   每次修改博客内容后，都建议先在本地预览，确保没有问题后再提交到 GitHub。
*   如果您想要了解更多关于 Hugo 和 Cloudflare Pages 的使用方法，可以查阅它们的官方文档。

### 从 Notion 导出文章的处理流程

为了保持博客内容的一致性和质量，从 Notion 导出的文章需要经过以下处理步骤：

1. **Notion 导出准备**：
   - 在 Notion 中选择要导出的单个页面
   - 选择导出格式为 "Markdown & CSV"
   - 确保勾选 "Include content" 和 "Include files & media"
   - 下载得到一个 ZIP 文件，将其放入 `Notionfiles` 目录

2. **自动处理流程**：
   ```bash
   # 执行自动处理脚本
   python extract_zip_utf8.py
   ```
   脚本会自动完成以下工作：
   - 解压 ZIP 文件到 `temp_notion` 目录
   - 自动处理文件名编码问题
   - 从文章标题生成规范的英文文件名
   - 调用 `process_notion_links.py` 处理文章内容和图片

3. **文章处理（由 process_notion_links.py 完成）**：
   - 提取并规范化文章元数据（标题、标签、创建时间等）
   - 生成符合规范的 Front Matter
   - 清理 Notion 特有的元数据和格式
   - 处理文章中的图片：
     * 下载网络图片到本地
     * 处理本地图片引用
     * 统一图片命名和存储位置
     * 转换为 WebP 格式并优化
   - 更新文章中的图片引用路径
   - 生成最终的博客文章文件

4. **本地预览确认**：
   ```bash
   # 启动 Hugo 预览
   hugo server -D
   ```
   - 检查文章在列表和详情页的显示效果
   - 确认所有图片能正常加载
   - 检查文章格式和样式是否正确

5. **提交更新**：
   - 确认一切正常后，提交更新到 Git 仓库
   - 等待 Cloudflare Pages 自动部署完成
   - 在线检查文章的最终效果

6. **清理临时文件**：
   ```bash
   # 清理临时文件和目录
   rm -rf temp_notion Notionfiles/*.zip
   ```

### 技术实现说明

整个自动化处理流程由两个主要脚本完成：

1. **extract_zip_utf8.py**：
   - 负责解压 Notion 导出的 ZIP 文件
   - 处理文件名编码问题
   - 生成规范的文章英文名
   - 协调整体处理流程

2. **process_notion_links.py**：
   - 处理文章内容和元数据
   - 提取 Notion 导出的元数据（标题、标签、创建时间等）
   - 清理 Notion 特有的格式和冗余内容
   - 处理图片：
     * 支持本地图片和网络图片
     * 并发下载和处理
     * 自动转换为 WebP 格式
     * 统一命名和组织

### 注意事项

1. **文件命名规范**：
   - 文章英文名自动从标题生成
   - 使用小写字母、数字和短横线
   - 避免特殊字符和空格

2. **图片处理**：
   - 所有图片统一存放在 `static/images/posts/{article-name}/` 目录
   - 自动转换为 WebP 格式以优化加载速度
   - 使用统一的命名格式：`image-1.webp`, `image-2.webp` 等

3. **元数据处理**：
   - 使用 Notion 页面的创建时间作为文章发布时间
   - 自动提取标签信息
   - 自动生成文章描述（从正文提取）

4. **内容清理**：
   - 自动移除 Notion 特有的元数据
   - 清理重复的标题
   - 规范化空行和格式

5. **质量控制**：
   - 每次处理完成后必须进行本地预览
   - 检查图片加载和显示效果
   - 确认文章格式和样式正确

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