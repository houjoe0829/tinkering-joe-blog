# 博客样式定制规范

## 概述

本博客基于 Hugo PaperMod 主题构建，并进行了自定义样式调整以实现极简风格。本文档详细说明了样式定制的规范、最佳实践和技术实现细节。

## 主题管理

### 主题选择和演进
- **当前主题**：Hugo PaperMod
- **管理方式**：从 2025-02-20 起，主题代码已从 git submodule 转换为普通文件
- **定制目标**：简化管理和定制，构建属于自己的极简风格
- **主题位置**：`themes/PaperMod/`

### 自定义样式位置
- **主要样式文件**：`assets/css/extended/custom.css`
- **作用范围**：所有自定义样式调整都在此文件中
- **优先级**：该文件中的样式会覆盖主题默认样式

## 样式规范详解

### 标题样式规范

为了保持整个博客的视觉一致性，采用了以下标题大小规范：

#### 标题层级设计
1. **文章标题**：24px（与首页博客列表标题大小保持一致）
2. **文章内容标题**：
   - `h1`：24px（与文章标题相同）
   - `h2`：22px（比 h1 小 2px）
   - `h3`：20px（比 h2 小 2px）
   - `h4`：18px（比 h3 小 2px）
   - `h5`：16px（比 h4 小 2px）
   - `h6`：14px（比 h5 小 2px）

#### 设计原理
- **递减规律**：每级标题比上一级小 2px，确保清晰的视觉层级
- **一致性**：文章标题与 h1 标签大小保持一致
- **可读性**：字体大小适中，在各种设备上都有良好的可读性

### 表格样式规范

#### 设计目标
解决表格宽度超出内容导致右侧出现不必要空白和边框的问题，采用 `width: fit-content` 样式让表格宽度自适应内容。

#### 通用表格样式类
**类名**：`toolkit-table`  
**适用场景**：所有需要自适应宽度的表格

#### HTML 结构示例
```html
<table class="toolkit-table">
  <thead>
    <tr>
      <th>表头 1</th>
      <th>表头 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>数据 1</td>
      <td>数据 2</td>
    </tr>
  </tbody>
</table>
```

#### CSS 核心代码
以下是 `.toolkit-table` 的完整样式，包含暗色模式适配：

```css
.toolkit-table {
  width: fit-content;
  max-width: 100%;
  border-collapse: collapse;
  border: 1px solid #e1e5e9;
  margin: 20px 0;
  box-sizing: border-box;
}

.toolkit-table th {
  padding: 12px;
  border: 1px solid #e1e5e9;
  background-color: #f1f3f4;
  font-weight: bold;
  text-align: left;
  box-sizing: border-box;
}

.toolkit-table td {
  padding: 10px;
  border: 1px solid #e1e5e9;
  vertical-align: top;
  box-sizing: border-box;
}

.toolkit-table td:first-child {
  white-space: nowrap;
  background-color: #f8f9fa;
  font-weight: 500;
}

.toolkit-table tr:hover {
  background-color: #f5f5f5;
}

.toolkit-table tr:hover td:first-child {
  background-color: #e8f0fe;
}

/* 暗色模式适配 */
@media (prefers-color-scheme: dark) {
  .toolkit-table {
    border-color: #333;
  }
  .toolkit-table th {
    background-color: #2c2c2c;
    border-color: #333;
  }
  .toolkit-table td {
    border-color: #333;
  }
  .toolkit-table td:first-child {
    background-color: #252525;
  }
  .toolkit-table tr:hover {
    background-color: #2a2a2a;
  }
  .toolkit-table tr:hover td:first-child {
    background-color: #1c3a5e;
  }
}
```

#### 表格样式特性
- **自适应宽度**：表格宽度根据内容自动调整
- **响应式设计**：最大宽度 100%，适配各种屏幕尺寸
- **交互效果**：鼠标悬停时行高亮显示
- **暗色模式**：自动适配系统暗色模式
- **第一列强调**：第一列背景色不同，字体加粗

### 图片 Caption 样式规范

#### 设计目标
为图片添加居中显示的说明文字（Caption），使用灰色斜体样式，与正文内容区分开来，提升图片的可读性和说明性。

#### 适用场景
- 需要为图片添加说明文字
- 图片来源标注
- 图片内容描述

#### HTML 结构示例
```html
![图片描述](/images/posts/article-name/image.webp)

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>这是图片的说明文字</em>
</div>
```

#### Markdown 中的使用示例
```markdown
![死去之后的重生画面](/images/posts/hades-2-game-review/image2.webp)

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>死去之后的重生画面</em>
</div>
```

#### 样式说明
- **文本对齐**：`text-align: center` - 居中显示
- **文字颜色**：`color: #666` - 灰色，区别于正文
- **字体大小**：`font-size: 0.9em` - 比正文略小
- **上边距**：`margin-top: -10px` - 紧贴图片，减少间距
- **下边距**：`margin-bottom: 20px` - 与下方内容保持适当距离
- **斜体样式**：`<em>` 标签 - 使用斜体强调这是说明文字

#### 使用注意事项
1. **紧跟图片**：Caption 的 HTML 代码应紧跟在图片 Markdown 语法之后
2. **内容简洁**：说明文字应简洁明了，避免过长
3. **统一格式**：所有图片 Caption 使用相同的样式格式
4. **可选使用**：不是所有图片都需要 Caption，根据实际需要添加

#### 暗色模式适配
在暗色模式下，灰色文字（`#666`）在深色背景上可能对比度不够。如需优化，可以在 `custom.css` 中添加：

```css
@media (prefers-color-scheme: dark) {
  .post-content div[style*="color: #666"] {
    color: #999 !important;
  }
}
```

## 样式开发最佳实践

### 1. 样式优先级管理

#### 常见问题
在 `custom.css` 中修改样式时，可能遇到样式不生效的情况。

#### 解决方案
- **提高选择器特异性**：使用更具体的选择器，如 `.post-header .post-title`
- **使用 !important**：在必要时添加 `!important` 声明
- **检查加载顺序**：确保自定义样式在主题样式之后加载

#### 示例
```css
/* 低特异性 - 可能不生效 */
.post-title {
  font-size: 24px;
}

/* 高特异性 - 更容易生效 */
.post-header .post-title {
  font-size: 24px;
}

/* 强制优先级 - 最后手段 */
.post-title {
  font-size: 24px !important;
}
```

### 2. 响应式设计原则

#### 移动端适配
- **使用 @media 查询**：针对不同屏幕尺寸调整样式
- **关键断点**：移动端（<768px）通常需要特殊处理
- **字体和间距**：移动端适当减小字体大小和间距

#### 示例
```css
/* 桌面端样式 */
.post-title {
  font-size: 24px;
  margin-bottom: 20px;
}

/* 移动端适配 */
@media (max-width: 768px) {
  .post-title {
    font-size: 20px;
    margin-bottom: 15px;
  }
}
```

### 3. 统一性原则

#### 设计一致性
- **相同元素统一样式**：所有页面的同类元素保持一致
- **规律性数值**：使用有规律的数值，如标题大小每级减小 2px
- **颜色体系**：建立统一的颜色规范

#### CSS 变量应用
```css
:root {
  --title-font-size-1: 24px;
  --title-font-size-2: 22px;
  --title-font-size-3: 20px;
  --primary-color: #007acc;
  --border-color: #e1e5e9;
}

h1 { font-size: var(--title-font-size-1); }
h2 { font-size: var(--title-font-size-2); }
h3 { font-size: var(--title-font-size-3); }
```

## 样式调试和维护

### 开发工具使用
1. **浏览器开发者工具**：实时调试样式效果
2. **Hugo 本地服务器**：`hugo server -D` 实时预览
3. **样式检查器**：检查样式优先级和继承关系

### 常见问题排查
1. **样式不生效**：检查选择器特异性和加载顺序
2. **移动端显示异常**：检查响应式断点和媒体查询
3. **暗色模式问题**：确保所有自定义样式都有暗色模式适配

### 性能优化
- **CSS 压缩**：Hugo 自动处理 CSS 压缩和合并
- **避免重复**：使用 CSS 变量减少重复代码
- **选择器优化**：避免过于复杂的选择器

## 主题定制扩展

### 添加新样式组件
1. **在 custom.css 中定义**：所有新样式都应在此文件中
2. **遵循命名规范**：使用有意义的类名，如 `blog-specific-component`
3. **包含暗色模式**：新组件应同时支持亮色和暗色模式

### 修改主题默认样式
1. **识别目标元素**：使用开发者工具找到对应的 CSS 选择器
2. **在 custom.css 中覆盖**：使用更高特异性的选择器
3. **测试兼容性**：确保修改不影响其他页面元素

### 样式文档维护
- **记录重要修改**：在代码注释中说明修改原因
- **定期审查**：清理不再使用的样式代码
- **版本控制**：通过 Git 跟踪样式文件的变更历史

## 相关文件和资源

### 关键文件位置
- **自定义样式**：`assets/css/extended/custom.css`
- **主题文件**：`themes/PaperMod/`
- **Hugo 配置**：`hugo.yaml`

### 参考资源
- **PaperMod 文档**：[Hugo PaperMod Wiki](https://github.com/adityatelange/hugo-PaperMod/wiki)
- **Hugo 文档**：[Hugo Documentation](https://gohugo.io/documentation/)
- **CSS 规范**：遵循现代 CSS 最佳实践

### 相关规范文档
- **内容类型规范**：[`content_types_overview.md`](content_types_overview.md)
- **图片处理规范**：[`global_image_compression_workflow.md`](global_image_compression_workflow.md)
