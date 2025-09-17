# 博客内容嵌入规范

## 概述

为了提供更好的阅读体验和视觉一致性，博客支持多种内容嵌入方式，包括链接样式、视频嵌入等。每种方式都有其特定的适用场景和使用方法，本文档详细说明了内容嵌入的规范、实现和最佳实践。

## 内容嵌入类型

### 链接样式类型

### 1. Bookmark 样式链接

#### 定义与特点
Bookmark 样式链接是一种视觉突出的卡片式链接展示方式，适用于需要重点推荐或引用的外部资源。

#### 技术实现
使用 Hugo 的自定义 `link` shortcode 实现，支持三个参数：
- 第一个参数：链接 URL（必需）
- 第二个参数：链接标题（必需）
- 第三个参数：摘要内容（可选，从 2025-05-26 起支持）

#### 使用语法
```markdown
{{< link "URL" "链接标题" "可选的摘要内容" >}}
```

#### 基本示例
```markdown
{{< link "https://example.com" "示例网站" >}}
```

#### 带摘要示例
```markdown
{{< link "https://endler.dev/2025/reinvent-the-wheel/" "Reinvent the Wheel" "One of the most harmful pieces of advice is to not reinvent the wheel." >}}
```

#### 渲染效果
Bookmark 样式链接会渲染出一个美观的卡片，包含：
- **链接标题**：醒目的标题文字
- **摘要内容**：如果提供第三个参数，会显示简短描述
- **完整 URL**：显示完整的链接地址
- **视觉指示器**：链接图标（非外部链接图标）
- **卡片样式**：带有边框和阴影的卡片式设计

#### 适用场景
1. **文章主要推荐的外部资源**：
   - 重要的参考文献
   - 推荐的工具或服务
   - 深度阅读材料

2. **需要特别强调的参考资料**：
   - 官方文档链接
   - 权威资料来源
   - 重要的技术规范

3. **独立成段的重要链接**：
   - 单独一段介绍的外部资源
   - 需要详细说明的链接
   - 文章结尾的推荐阅读

#### 使用最佳实践
1. **控制使用频率**：每篇文章建议不超过 3-5 个 Bookmark 链接
2. **提供有意义的摘要**：充分利用第三个参数提供有价值的描述
3. **确保链接有效性**：定期检查 Bookmark 链接的可访问性
4. **标题简洁明确**：使用清晰、简洁的标题描述链接内容

#### 2. 普通链接

#### 定义与特点
普通链接使用标准的 Markdown 语法，适用于行内引用和列表中的链接，保持文档的简洁性。

#### 使用语法
```markdown
[链接文本](链接URL)
```

#### 内部链接示例
```markdown
[我的另一篇文章](/posts/article-name)
[关于页面](/about)
[搜索功能](/search)
```

#### 外部链接示例
```markdown
[Hugo 官方文档](https://gohugo.io/documentation/)
[GitHub 仓库](https://github.com/username/repository)
[参考资料](https://example.com/reference)
```

#### 适用场景
1. **文章间的内部引用**：
   - 引用博客内的其他文章
   - 链接到特定的页面或章节
   - 交叉引用相关内容

2. **列表项中的链接**：
   - 参考资料列表
   - 相关链接集合
   - 工具和资源清单

3. **段落内的行内链接**：
   - 文章中提到的外部资源
   - 概念解释的参考链接
   - 补充说明的材料

4. **参考资料列表中的链接**：
   - 文章末尾的参考文献
   - 延伸阅读材料
   - 数据来源链接

#### 使用最佳实践
1. **链接文本有意义**：使用描述性的链接文本，避免"点击这里"
2. **内外链区分**：内部链接使用相对路径，外部链接使用完整 URL
3. **适度使用**：避免在同一段落中过多的链接
4. **定期维护**：检查链接的有效性，特别是外部链接

### 视频嵌入

#### 定义与特点
视频嵌入功能允许在博客文章中直接嵌入本地视频文件，提供原生的视频播放体验。支持响应式设计，在不同设备上都能良好显示。

#### 技术实现
使用 Hugo 的自定义 `video` shortcode 实现，基于 HTML5 `<video>` 标签，支持多个可选参数：
- `src`：视频文件路径（必需）
- `poster`：视频海报图片路径（可选）
- `width`：视频宽度（可选，默认 100%）
- `autoplay`：自动播放（可选，默认 false）
- `muted`：静音播放（可选，默认 false）
- `loop`：循环播放（可选，默认 false）

#### 使用语法
```markdown
{{< video src="/images/posts/article-name/demo.mp4" >}}
```

#### 基本示例
```markdown
{{< video src="/images/thoughts/ai-pomodoro-timer-with-radio/demo.mp4" >}}
```

#### 带海报图片示例
```markdown
{{< video src="/images/posts/tutorial/demo.mp4" poster="/images/posts/tutorial/poster.webp" >}}
```

#### 自定义参数示例
```markdown
{{< video src="/images/posts/demo/video.mp4" width="80%" muted="true" >}}
```

#### 渲染效果
视频 shortcode 会渲染出一个美观的视频播放器，包含：
- **响应式布局**：自适应不同屏幕尺寸
- **原生控制器**：标准的播放/暂停、进度条、音量控制
- **优雅样式**：圆角边框和阴影效果
- **悬停效果**：轻微的缩放动画
- **兼容性回退**：不支持的浏览器显示下载链接

#### 文件组织
视频文件应放置在对应的图片目录中：

**Posts（博文）**：
```
static/images/posts/article-name/
├── image1.webp
├── screenshot.webp
└── demo.mp4
```

**Thoughts（想法）**：
```
static/images/thoughts/thought-name/
├── photo.webp
└── clip.mp4
```

#### 适用场景
1. **功能演示**：
   - 软件操作演示
   - 产品功能展示
   - 工具使用教程

2. **过程记录**：
   - 制作过程展示
   - 实验步骤记录
   - 操作流程说明

3. **效果展示**：
   - 动画效果演示
   - 交互效果展示
   - 最终成果展示

#### 文件要求和建议
1. **文件大小**：建议控制在 5MB 以内，确保加载速度
2. **文件格式**：推荐使用 MP4 格式，兼容性最好
3. **视频质量**：建议使用 H.264 编码，质量与文件大小平衡
4. **分辨率**：根据内容需要选择，通常 1080p 或 720p 即可
5. **时长控制**：建议控制在 2 分钟以内，保持观看体验

#### 使用最佳实践
1. **文件优化**：压缩视频文件，平衡质量与大小
2. **海报图片**：为重要视频提供吸引人的海报图片
3. **描述性文字**：在视频前后添加必要的文字说明
4. **适度使用**：每篇文章建议不超过 2-3 个视频
5. **移动端考虑**：确保视频在移动设备上播放流畅

## 内容嵌入选择指南

### 选择 Bookmark 样式的情况
- ✅ 文章的核心参考资料
- ✅ 需要详细介绍的外部工具
- ✅ 重要的官方文档或规范
- ✅ 独立段落介绍的资源
- ✅ 希望读者重点关注的链接

### 选择普通链接的情况
- ✅ 文章间的内部引用
- ✅ 列表中的多个链接
- ✅ 段落中的行内引用
- ✅ 简单的外部链接
- ✅ 参考资料列表

### 选择视频嵌入的情况
- ✅ 需要动态演示的功能或过程
- ✅ 软件操作或工具使用教程
- ✅ 产品效果或交互展示
- ✅ 制作过程或实验记录
- ✅ 静态图片无法充分表达的内容

### 避免的使用方式
- ❌ 在同一篇文章中过多使用 Bookmark 样式
- ❌ 对不重要的链接使用 Bookmark 样式
- ❌ 在列表中使用 Bookmark 样式
- ❌ 链接文本过于简单（如"链接"、"点击"）
- ❌ 使用过大的视频文件影响加载速度
- ❌ 在一篇文章中嵌入过多视频

## 技术实现细节

### Bookmark 链接的 Shortcode 实现
Bookmark 链接通过 Hugo 的 shortcode 系统实现，相关文件位置：
- **Shortcode 文件**：`layouts/shortcodes/link.html`
- **样式文件**：`assets/css/extended/custom.css`（包含 `.bookmark-link` 相关样式）

### 视频 Shortcode 的实现
视频嵌入通过 Hugo 的 shortcode 系统实现，相关文件位置：
- **Shortcode 文件**：`layouts/shortcodes/video.html`
- **技术基础**：HTML5 `<video>` 标签
- **样式特性**：内联 CSS 样式，响应式设计

### 样式定制

#### Bookmark 链接样式
Bookmark 链接的视觉样式可以通过 CSS 进行定制：
```css
.bookmark-link {
  /* 卡片样式 */
  border: 1px solid #e1e5e9;
  border-radius: 8px;
  padding: 16px;
  margin: 16px 0;
  
  /* 悬停效果 */
  transition: box-shadow 0.2s ease;
}

.bookmark-link:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
```

#### 视频播放器样式
视频播放器的样式通过内联 CSS 实现，主要特性：
```css
.video-container {
  text-align: center;
  margin: 2rem 0;
}

.video-container video {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transition: transform 0.2s ease;
}

.video-container video:hover {
  transform: scale(1.02);
}
```

### 响应式设计

#### Bookmark 链接响应式
Bookmark 链接支持响应式设计，在不同屏幕尺寸下都能良好显示：
```css
@media (max-width: 768px) {
  .bookmark-link {
    padding: 12px;
    margin: 12px 0;
  }
}
```

#### 视频播放器响应式
视频播放器自动适应不同屏幕尺寸：
```css
@media (max-width: 768px) {
  .video-container {
    margin: 1rem 0;
  }
  
  .video-container video {
    border-radius: 6px;
  }
}
```

## 可访问性考虑

### 语义化标记
- Bookmark 链接使用适当的 HTML 语义化标签
- 提供 `aria-label` 属性用于屏幕阅读器
- 确保链接具有足够的颜色对比度
- 视频使用标准的 HTML5 `<video>` 元素

### 键盘导航
- 所有链接都支持键盘导航（Tab 键）
- 焦点状态有明显的视觉指示
- 支持回车键激活链接
- 视频播放器支持键盘控制（空格键播放/暂停）

### 屏幕阅读器支持
- 链接标题和摘要都能被屏幕阅读器正确读取
- 外部链接有适当的标识
- 提供足够的上下文信息
- 视频提供兼容性回退文本和下载链接

### 视频可访问性
- 提供视频控制器，用户可以控制播放
- 支持键盘操作和屏幕阅读器
- 不自动播放，避免干扰用户体验
- 为重要视频提供文字描述或字幕

## 性能优化

### 加载优化
- Bookmark 链接的样式通过 CSS 预加载
- 图标使用 SVG 格式，减少加载时间
- 避免不必要的外部资源依赖
- 视频使用 `preload="metadata"` 减少初始加载

### 缓存策略
- 链接样式文件参与 Hugo 的资源管道
- 支持浏览器缓存和 CDN 缓存
- 版本控制确保样式更新及时生效
- 视频文件通过 CDN 缓存提升加载速度

### 视频性能优化
- 建议视频文件大小控制在 5MB 以内
- 使用 H.264 编码优化兼容性和压缩率
- 提供海报图片减少首次加载时间
- 不自动播放，由用户主动控制

## 维护和更新

### 定期检查
1. **链接有效性检查**：
   ```bash
   # 可以使用工具检查链接状态
   python3 scripts/check_links.py
   ```

2. **样式一致性检查**：
   - 定期审查 Bookmark 链接的视觉效果
   - 确保在不同浏览器中的兼容性
   - 验证响应式设计的正确性

3. **视频文件检查**：
   - 定期检查视频文件的可访问性
   - 验证视频在不同设备上的播放效果
   - 监控视频文件大小和加载性能

### 更新流程
1. **Shortcode 更新**：
   - 链接：修改 `layouts/shortcodes/link.html`
   - 视频：修改 `layouts/shortcodes/video.html`
2. **样式更新**：修改 `assets/css/extended/custom.css`
3. **测试验证**：在本地环境测试新样式和功能
4. **文档更新**：更新本规范文档

## 示例和参考

### 实际使用示例

#### 链接样式示例
可以参考以下文件中的实际使用案例：
- `content/thoughts/reinventing-the-wheel-reflections.md`
- 其他包含外部链接的博文

#### 视频嵌入示例
可以参考以下文件中的视频使用案例：
- `content/thoughts/ai-pomodoro-timer-with-radio.md`
- 其他包含演示视频的文章

### 样式参考
- **设计灵感**：现代 Web 应用中的卡片式设计
- **颜色方案**：与博客整体主题保持一致
- **交互效果**：简洁的悬停和焦点效果

## 常见问题

### 链接相关问题

#### Q: 什么时候使用 Bookmark 样式？
A: 当链接是文章的重要参考资料，需要读者特别关注时使用。

#### Q: 可以在列表中使用 Bookmark 样式吗？
A: 不推荐。列表中建议使用普通链接保持简洁性。

#### Q: Bookmark 链接支持内部链接吗？
A: 技术上支持，但建议主要用于外部重要资源。

#### Q: 如何修改 Bookmark 链接的样式？
A: 通过修改 `custom.css` 中的相关样式类来定制外观。

#### Q: 摘要参数是必需的吗？
A: 不是必需的，但建议提供以增强用户体验。

### 视频相关问题

#### Q: 视频文件应该放在哪里？
A: 放在对应的 `static/images/` 目录下，与图片文件一起管理。

#### Q: 支持哪些视频格式？
A: 推荐使用 MP4 格式（H.264 编码），兼容性最好。

#### Q: 视频文件大小有限制吗？
A: 建议控制在 5MB 以内，确保良好的加载体验。

#### Q: 如何为视频添加海报图片？
A: 使用 `poster` 参数：`{{< video src="video.mp4" poster="poster.webp" >}}`

#### Q: 视频会自动播放吗？
A: 默认不会自动播放，由用户主动控制，也可通过 `autoplay="true"` 开启。

#### Q: 如何修改视频播放器的样式？
A: 视频样式在 shortcode 中通过内联 CSS 定义，可以修改 `video.html` 文件。

## 相关文档

### 相关规范文档
- **博客样式定制**：[`blog_styling_guide.md`](blog_styling_guide.md)
- **内容类型规范**：[`content_types_overview.md`](content_types_overview.md)

### 技术参考
- **Hugo Shortcodes**：[Hugo Shortcode Documentation](https://gohugo.io/content-management/shortcodes/)
- **HTML5 Video**：[MDN Video Element Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
- **CSS 样式指南**：现代 CSS 最佳实践
- **可访问性标准**：WCAG 2.1 指导原则
- **视频编码指南**：H.264 编码最佳实践
