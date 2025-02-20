# Joe 的折腾日记

这个博客使用 Hugo 静态网站生成器构建，并托管在 Cloudflare Pages 上。

## 当前博客构建方式

* **Hugo**: 负责将 Markdown 内容转换为静态网页。
* **Cloudflare Pages**:  提供网站托管、CDN 加速和自动部署。
* **GitHub**:  用于存储博客源代码和版本管理。

## 评论系统

### 使用 GitHub Discussions

* **评论数据存储**:  评论数据直接存储在 GitHub 仓库的 Discussions 功能中。
* **前端组件**:  使用开源组件 [Giscus](https://giscus.app/) 在博客页面中嵌入评论功能。
* **用户认证**:  用户需要拥有 GitHub 账号才能评论。
* **优点**:
  * **零维护成本**:  无需服务器和数据库，完全依赖 GitHub 平台。
  * **与 GitHub 集成**:  天然与代码仓库集成，方便管理和审核。
  * **Markdown 支持**:  评论支持 Markdown 格式。
* **缺点**:
  * **仓库需公开**:  博客仓库必须设置为 Public 才能公开评论。
  * **依赖 GitHub**:  评论功能依赖 GitHub 服务的稳定性。
  * **用户门槛**:  需要用户注册 GitHub 账号。
* **适用场景**:  静态博客，对维护成本敏感，希望利用 GitHub 账号体系。

**更详细的配置步骤和说明，请参考 [Giscus 官方网站](https://giscus.app/)。**

---

## 项目目录结构

```
discovery-log/
├── archetypes/          # Hugo 文章模板
├── assets/              # 自定义样式和资源文件
│   └── css/
│       └── extended/
│           └── custom.css
├── content/             # 博客文章内容
│   └── posts/          # 所有博客文章
├── data/               # Hugo 数据文件
├── i18n/               # 国际化文件
├── layouts/            # 自定义布局模板
├── public/             # Hugo 生成的静态网站文件
├── resources/          # Hugo 缓存资源
├── scripts/            # 工具脚本目录
│   ├── extract_zip_utf8.py           # Notion ZIP 文件处理
│   ├── compress_article_images.py     # 单篇文章图片压缩
│   ├── compress_images.py            # 全局图片压缩
│   ├── clean_original_images.py      # 清理原始图片
│   └── update_image_refs.py          # 更新图片引用
├── static/             # 静态资源文件
│   └── images/        # 图片资源
│       └── posts/     # 文章图片
├── themes/             # Hugo 主题
├── draftfiles/        # Notion 导出的 ZIP 文件
├── hugo.yaml           # Hugo 配置文件
└── README.md          # 项目说明文档
```

## 博客样式定制

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

## 本地构建和调试

在您提交更新之前，您可以在本地电脑上预览博客效果，确保一切正常：

1. **安装 Hugo**:  请确保您已经在本机安装了 Hugo (具体安装步骤请参考 [Hugo 官方文档](https://gohugo.io/getting-started/installing/))。

2. **本地预览**:
    * 打开命令行终端，进入您的博客项目根目录。
    * 运行命令 `hugo server -D`。
    * Hugo 将会在本地启动一个开发服务器，您可以通过浏览器访问 `http://localhost:1313/` 来预览您的博客。
    * `-D` 参数表示同时构建 `draft` (草稿) 状态的文章，方便您预览尚未正式发布的文章。

3. **停止预览**:
    * 在命令行终端中按下 `Ctrl + C` 即可停止本地 Hugo 开发服务器。

## AI 助手依据 Markdown 文件手动更新博客的说明

在这种场景下，我只通过 Markdown 文章提供标题和正文。

AI 将执行以下关键步骤来帮助您更新博客：

1. **接收并理解内容**：AI 助手会仔细阅读并理解您提供的文章标题和正文。
2. **创建 Markdown 文件**：在 `content/posts/` 目录下，AI 会创建一个以文章标题命名的 Markdown 文件。
3. **添加 Frontmatter**：AI 会在新文件的开头添加必要的 Frontmatter 元数据，包括：
   * `title`：文章标题
   * `date`：发布日期
   * `draft`：是否为草稿
   * `description`：文章简短描述
   * `tags`：从预定义标签列表中选择合适的标签（参考"博客元数据格式规范"章节中的标签列表）
   * `author`：作者信息
   每次生成新的博客文件时，请参考 `@nezha-movie-review.md` 文件的格式和元数据进行修正。
   - YAML 对特殊字符非常敏感，特别是在 Front Matter 中
   - 在元数据里，使用纯英文引号包裹 YAML 值
   - 在元数据里，统一使用半角标点符号
4. **添加文章正文**：AI 会将您提供的文章正文内容复制到 Markdown 文件中。

## 使用 AI 助手来处理 Notion Zip 文件

主要是将 Notion 导出的 Zip 文件转换为当前的 Blog 格式。

为了保持博客内容的一致性和质量，请严格遵守以下处理步骤，不要遗漏：

1. **Notion Zip 准备**：
   * 将 Notion 导出的 Zip 文件放入项目根目录的 `draftfiles` 目录中

2. **解压缩处理**：

   ```bash
   python3 scripts/extract_zip_utf8.py
   ```

   * 脚本会将 ZIP 文件解压到 `temp_notion` 目录
   * 自动处理文件名编码问题

3. **手动内容处理**：
   * 检查并手动修正文章的英文名，确保符合以下规范：
     * 使用纯英文单词，不使用拼音
     * 单词之间用短横线（-）连接
     * 所有字母小写
     * 文件名应该清晰表达文章主题
     * 如果是特定时间的文章，建议加入年份
     * 示例：
       * ✅ `chinese-new-year-2024-recap.md`
       * ✅ `my-first-coding-experience.md`
       * ❌ `joe-recap-guo-nian.md`（不要使用拼音）
       * ❌ `My-First-Post.md`（不要使用大写）
       * ❌ `post1.md`（不够具体）
   * 创建并完善 Front Matter 元数据：
     * 确保所有必需字段都已填写
     * 标签必须从预定义列表中选择（参考"博客元数据格式规范"章节中的标签列表）
     * 不要创建新的标签
   * 检查并修复文章格式

4. **处理文章和图片**：
   建议采用手动方式处理文章和图片，以确保更高的质量和准确性：

   ① **文章处理**：
      * 仔细阅读原文，理解内容和时间线
      * 创建新的 Markdown 文件，使用规范的英文名，如：`content/posts/taizhou-travel-notes.md`
      * 保留文章内容里的原始链接，不要修改
      * 手动编写 Front Matter，确保：
        * 标题、描述准确，使用原文标题，不要生成新的标题
        * 日期使用 Notion zip 实际数据的日期
        * 标签分类合理
        * 作者信息正确

   ② **图片处理**：
      * 在 `static/images/posts/` 下创建与文章同名的目录
      * 将原始图片复制到该目录
      * 根据图片内容给予有意义的文件名
      * 使用 `compress_article_images.py` 脚本处理单篇文章的图片：

        ```bash
        python3 scripts/compress_article_images.py article-name
        ```

      * 将压缩后的图片从 `static/images_compressed/posts/article-name/` 复制到 `static/images/posts/article-name/`
      * 运行 `update_image_refs.py` 更新文章中的图片引用为 WebP 格式
      * 注意：这里不要使用 `compress_images.py`，它是用于全站图片批量处理的

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

6. 清理临时文件
   ① **清理原始图片，不要忘了**：

     ```bash
     # 预览要删除的原始图片文件
     python3 scripts/clean_original_images.py
     
     # 确认无误后删除原始图片文件
     python3 scripts/clean_original_images.py --execute
     ```

   * 这一步会删除已经转换为 WebP 格式的原始图片文件
   * 注意：网站图标文件（如 android-chrome-*.png、apple-touch-icon.png 等）会自动保护，不会被删除

   ② **清理其他临时文件**：

   ```bash
   # 清理 Notion 处理的临时文件
   rm -rf temp_notion
   rm -f draftfiles/*.zip
   ```

注意事项：
* 每个步骤完成后请仔细检查，确保无误后再进行下一步
* 如果发现问题，可以随时回退到之前的步骤
* 保留原始 ZIP 文件，直到所有步骤都确认无误

## 全局图片压缩指南

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
   python scripts/compress_images.py
   ```

   这会在项目根目录创建 `static_compressed` 目录，存放压缩后的文件。

3. **复制压缩后的文件**：

   ```bash
   cp -r static_compressed/* static/
   ```

   这一步会将压缩后的文件复制回原目录，同时保留原始文件作为备份。

4. **更新图片引用**：

   ```bash
   python scripts/update_image_refs.py
   ```

   这一步会自动将所有 Markdown 文件中的图片引用更新为 WebP 格式。
   例如：`![示例图片](/images/example.jpg)` 会被更新为 `![示例图片](/images/example.webp)`

5. **预览要删除的原始文件**：

   ```bash
   python scripts/clean_original_images.py
   ```

   这一步会显示哪些原始文件将被删除，以及可以节省的空间大小。

6. **确认无误后删除原始文件**：

   ```bash
   python scripts/clean_original_images.py --execute
   ```

   这一步会删除已经转换为 WebP 格式的原始图片文件，但会保留网站图标相关文件。

7. **清理临时文件**：

   ```bash
   # 清理 Notion 处理的临时文件
   rm -rf temp_notion
   rm -f draftfiles/*.zip
   
   # 清理图片压缩的临时目录
   rm -rf static_compressed
   rm -rf static/images_compressed
   ```

### 注意事项

1. **安全性考虑**：
   * 压缩脚本会在单独的目录中生成压缩后的文件，不会直接修改原始文件
   * 清理脚本默认为预览模式，让您可以在删除前确认更改
   * 网站必需的图标文件（favicon 等）会自动保护，不会被转换或删除
   * 更新图片引用时会自动备份原始 Markdown 文件

2. **文件格式**：
   * 支持的输入格式：JPG、JPEG、PNG、GIF、WebP
   * 所有图片（除了网站图标）都会被转换为 WebP 格式
   * PNG 文件会使用无损压缩转换为 WebP
   * JPG 文件会使用有损压缩（质量 85%）转换为 WebP

3. **性能优化**：
   * WebP 格式通常可以减少 30-70% 的文件大小
   * 图片会被限制在 1920x1920 的最大尺寸内
   * 所有图片都会被移除元数据，进一步减小文件大小

4. **兼容性**：
   * 现代浏览器都支持 WebP 格式
   * 网站图标保持原格式以确保最大兼容性

## 图片引用检查指南

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

### 最佳实践

1. **定期检查**：
   * 每次添加新文章后运行检查
   * 在进行图片相关的批量操作后运行检查
   * 定期（如每月）进行一次完整检查

2. **失效链接处理**：
   * 对于失效的图片引用，确认图片文件是否存在
   * 检查文件名大小写是否正确
   * 验证文件路径是否正确
   * 确保图片格式与引用一致（如 .webp）

3. **外部链接管理**：
   * 尽量避免使用外部图片链接
   * 如果必须使用外部链接，确保链接的可靠性
   * 考虑将重要的外部图片下载到本地

4. **文件名规范**：
   * 使用规范的文件命名（避免空格和特殊字符）
   * 保持文件扩展名的一致性（优先使用 .webp）
   * 使用有意义的文件名，便于管理和识别

5. **目录结构**：
   * 保持图片目录结构清晰
   * 每篇文章的图片放在独立的目录中
   * 目录名与文章文件名保持一致

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

## 博客元数据格式规范

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

#### 格式要求说明

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

## 许可证说明

本仓库采用双重许可证模式：

1. **博客内容**：所有博客文章内容（包括文字、图片等）采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可证。
2. **代码部分**：所有代码文件采用 [MIT](https://opensource.org/licenses/MIT) 许可证。

详细的许可说明请查看 [LICENSE.md](LICENSE.md) 文件。
