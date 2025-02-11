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

### 图片处理规则（重要！）

为了避免误操作和保持项目的一致性，图片处理必须严格遵循以下步骤：

#### 1. 目录结构规范
```bash
static/images/posts/
└── article-name/           # 每篇文章必须使用独立目录
    ├── image-1.webp       # 图片必须按顺序编号
    ├── image-2.webp
    └── image-3.webp
```

#### 2. 图片处理工作流（必须按顺序执行）

```bash
# 第一步：为当前文章创建专属图片目录（必须使用文章的英文名）
article_name="2019-toys-and-gadgets-recap"  # 示例：将此处改为当前文章的英文名
mkdir -p "static/images/posts/$article_name"

# 第二步：复制图片到文章专属目录
cd temp_notion/your-notion-folder
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

# 第三步：压缩当前文章的图片
# ⚠️ 注意：使用 compress_article_images.py 而不是 compress_images.py
python compress_article_images.py "$article_name"

# 第四步：更新当前文章的压缩图片
cp -r "static/images_compressed/posts/$article_name/"*.webp \
  "static/images/posts/$article_name/"

# 第五步：清理当前文章的临时文件
rm -rf "static/images_compressed/posts/$article_name"
```

#### 3. 图片压缩脚本说明

项目中有两个不同的图片压缩脚本，用途不同：

1. **compress_article_images.py**：
   - 用途：压缩单篇文章的图片
   - 使用方法：`python compress_article_images.py "article-name"`
   - 示例：`python compress_article_images.py "2019-toys-and-gadgets-recap"`
   - ✅ 这是处理新文章时应该使用的脚本

2. **compress_images.py**：
   - 用途：仅在特殊情况下用于压缩所有图片（如站点迁移）
   - ❌ 禁止在日常文章处理中使用
   - ⚠️ 使用前必须得到管理员确认

#### 4. 严格禁止的操作（❌）

1. **禁止全局压缩**：
   ```bash
   # ❌ 严禁执行以下命令
   python compress_images.py "static/images" "static/images_compressed"
   ```

2. **禁止多文章同时处理**：
   ```bash
   # ❌ 严禁同时处理多个文章的图片
   python compress_images.py "static/images/posts/article1" "static/images/posts/article2"
   ```

3. **禁止使用错误的目录结构**：
   ```bash
   # ❌ 禁止将图片直接放在 posts 目录下
   static/images/posts/image1.webp  # 错误
   
   # ✅ 必须放在文章专属目录下
   static/images/posts/article-name/image-1.webp  # 正确
   ```

#### 4. 图片处理检查清单

每次处理图片前，请检查：

- [ ] 是否已创建文章专属目录？
- [ ] 目录名是否使用文章的英文名？
- [ ] 是否只处理当前文章的图片？
- [ ] 图片是否按顺序编号？
- [ ] 是否清理了之前的临时文件？

#### 5. 常见错误处理

如果发现压缩了错误的目录：
1. 立即停止当前操作
2. 删除所有 `static/images_compressed` 目录
3. 从版本控制恢复原始图片
4. 重新按照正确步骤处理当前文章的图片

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
   - 生成最终的博客文章文件（用原文内容，不要修改）

4. **图片压缩处理**：
   ```bash
   # 假设文章英文名为 your-article-name
   article_name="your-article-name"
   
   # 压缩当前文章的图片
   python compress_images.py \
     "static/images/posts/$article_name" \
     "static/images_compressed/posts/$article_name"
   
   # 更新压缩后的图片
   cp "static/images_compressed/posts/$article_name/"*.webp \
     "static/images/posts/$article_name/"
   ```

5. **本地预览确认**：
   ```bash
   # 启动 Hugo 预览
   hugo server -D
   ```
   - 检查文章在列表和详情页的显示效果
   - 确认所有图片能正常加载
   - 检查文章格式和样式是否正确

6. **提交更新**：
   - 确认一切正常后，提交更新到 Git 仓库
   - 等待 Cloudflare Pages 自动部署完成
   - 在线检查文章的最终效果

7. **清理临时文件**：
   ```bash
   # 清理临时文件和目录
   rm -rf "static/images_compressed/posts/$article_name"  # 清理压缩临时目录
   rm -rf temp_notion  # 清理解压的临时目录
   rm -f Notionfiles/*.zip  # 清理原始 ZIP 文件
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
   - 所有图片统一存放在 `