# 站点字体设计规范

## 概述

本站点以 Noto Serif SC（思源宋体）为全站标题和正文字体，通过 Google Fonts 加载。

## 字体栈配置

### 全局字体

由 `assets/css/extended/custom.css` 定义，正文采用 500 字重，标题采用 700 字重：

```css
font-family: "Noto Serif SC", "Noto Serif", "Noto Serif CJK SC", "Noto Serif CJK",
             "Source Han Serif SC", "source-han-serif-sc",
             "Times New Roman", "Georgia", serif;
```

字体优先级说明：
1. Noto Serif SC、Noto Serif：主要字体。
2. Noto Serif CJK SC、Noto Serif CJK：Noto CJK 宋体备用字体。
3. Source Han Serif SC、source-han-serif-sc：思源宋体备用字体。
4. Times New Roman、Georgia：西文备用字体。
5. serif：系统默认衬线字体。

### 代码字体

```css
font-family: -apple-system, BlinkMacSystemFont, "Menlo", "Monaco", "Consolas",
             "Courier New", monospace;
```

代码块使用等宽字体以保持代码的可读性和对齐性。

## 行高配置

### 正文内容
- 段落行高: **2em**
- 列表项行高: **2em**
- 引用块行高: **2em**

**设计理念:** 采用 2em 的行高大幅提升阅读舒适度，给予文字充足的呼吸空间，特别适合长文阅读。

### 标题行高
- H1: **1.4**
- H2: **2em**
- H3: **2em**
- H4-H6: 默认

## 字体大小

### 标题层级

| 标题级别 | 字体大小 | 上边距 | 下边距 |
|---------|---------|--------|--------|
| H1 | 2.2em | 40px | 32px |
| H2 | 1.5em | 1.5em | 0.75em |
| H3 | 1.25em | 1.25em | 0.625em |
| H4-H6 | 1.125em | 1em | 1em |

### 正文
- 桌面端: 16px
- 移动端: 18px（增大以提升移动阅读体验）

## 渲染优化

### 字体平滑
```css
-webkit-font-smoothing: antialiased;        /* macOS/iOS 优化 */
-moz-osx-font-smoothing: grayscale;         /* Firefox 优化 */
```

## 颜色设置

所有文本内容使用主题的 `--content` 变量，确保：
- 在浅色模式下文字足够深，清晰易读
- 在深色模式下自动适配为浅色文字
- 保持全站颜色一致性

```css
color: var(--content);
```

## 移动端适配

```css
@media screen and (max-width: 768px) {
    .post-content,
    .post-content p {
        font-size: 18px !important;
        line-height: 1.7;
    }
}
```

移动端字体从 16px 增大到 18px，行高略微调整为 1.7 以适应小屏幕。

## 实现文件

字体配置主要在以下文件中：
- `/themes/PaperMod/assets/css/core/reset.css` - 全局字体定义（主题默认）
- `/assets/css/extended/custom.css` - 自定义样式扩展
- `/assets/css/giscus.css`：评论区单独加载思源宋体，沿用全站字体栈和正文 500 字重。
