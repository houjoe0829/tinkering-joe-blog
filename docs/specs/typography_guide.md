# 站点字体设计规范

## 概述

本站点采用优雅的衬线字体设计,以 **Noto Serif SC**(思源宋体)为主字体,营造传统书籍般的阅读体验。字体设计参考了 UNTAG 等优秀中文内容网站的排版方案。

## 字体栈配置

### 全局字体

```css
font-family: "Noto Serif SC", "Noto Serif", "Noto Serif CJK SC", "Noto Serif CJK", 
             "Source Han Serif SC", "source-han-serif-sc", 
             "Times New Roman", "Georgia", serif;
```

**字体优先级说明:**
1. **Noto Serif SC** - 思源宋体简体中文版,主要中文字体
2. **Noto Serif** - 思源宋体通用版本
3. **Noto Serif CJK SC** - 思源宋体 CJK 版本(简体中文)
4. **Noto Serif CJK** - 思源宋体 CJK 通用版本
5. **Source Han Serif SC** - 思源宋体(Adobe 命名),备用中文字体
6. **Times New Roman** - 经典英文衬线字体
7. **Georgia** - 优雅的英文衬线字体
8. **serif** - 系统默认衬线字体

### 代码字体

```css
font-family: -apple-system, BlinkMacSystemFont, "Menlo", "Monaco", "Consolas", 
             "Courier New", monospace;
```

代码块使用等宽字体以保持代码的可读性和对齐性。

## 字体权重

| 元素类型 | 字体权重 | 说明 |
|---------|---------|------|
| 正文内容 | 500 (medium) | 比标准字重稍重,提升可读性 |
| 标题 | 700 (bold) | 突出层级结构 |
| 代码 | 400 (normal) | 保持代码清晰度 |

## 字间距设置

| 元素类型 | letter-spacing | 说明 |
|---------|---------------|------|
| 正文 | 0.03em | 让文字更舒展,易于阅读 |
| 标题 | 0.02em | 稍紧凑,保持标题的集中感 |
| 代码 | 0 | 等宽字体不需要额外间距 |

## 行高配置

### 正文内容
- 段落行高: **2em**
- 列表项行高: **2em**
- 引用块行高: **2em**

**设计理念:** 采用 2em 的行高大幅提升阅读舒适度,给予文字充足的呼吸空间,特别适合长文阅读。

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
- 移动端: 18px (增大以提升移动阅读体验)

## 渲染优化

### 字体平滑
```css
-webkit-font-smoothing: antialiased;        /* macOS/iOS 优化 */
-moz-osx-font-smoothing: grayscale;         /* Firefox 优化 */
```

### 文本渲染
```css
text-rendering: optimizeLegibility;         /* 标题渲染优化 */
```

这些设置可以让字体在不同浏览器和操作系统上呈现更一致、更平滑的效果。

## 颜色设置

所有文本内容使用主题的 `--content` 变量,确保:
- 在浅色模式下文字足够深,清晰易读
- 在深色模式下自动适配为浅色文字
- 保持全站颜色一致性

```css
color: var(--content);
```

## 应用范围

### 全局应用
- body, html
- 所有页面的正文内容
- 文章内容区域
- 卡片描述文字

### 标题应用
- h1-h6 标签
- .post-title
- .entry-header h2

### 代码应用
- code, pre, kbd, samp, tt, var
- 代码块和行内代码

## 段落样式

```css
.post-content p {
    margin: 1em 0;
    line-height: 2em;
}
```

段落间距为 1em,与行高形成和谐的垂直节奏。

## 列表样式

```css
.post-content li {
    line-height: 2em;
}

.post-content li > p {
    line-height: 2em;
    margin: 0;
}
```

列表项继承相同的行高,保持统一的视觉节奏。

## 引用块样式

```css
.post-content blockquote {
    line-height: 2em;
    margin: 0 0 1.5em;
}
```

引用块使用相同的行高,下方留出 1.5em 的间距。

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

移动端字体从 16px 增大到 18px,行高略微调整为 1.7 以适应小屏幕。

## 设计优势

### 1. 优雅美观
- 思源宋体是专为屏幕阅读优化的现代衬线字体
- 具有传统书籍的优雅气质
- 中英文混排和谐

### 2. 阅读舒适
- 2em 的行高给予文字充足空间
- 500 字重确保清晰度
- 合理的字间距让文字舒展

### 3. 性能优化
- 优先使用系统已安装的字体
- 无需加载外部字体文件
- 页面加载速度快

### 4. 兼容性好
- 完整的字体栈确保各环境都有合适的字体
- 多级回退机制
- 支持所有现代浏览器

## 字体来源

**Noto Serif SC** 是 Google 和 Adobe 联合开发的开源字体:
- 开源免费
- 覆盖完整的中文字符集
- 为屏幕显示优化
- 多数现代操作系统已内置

如果用户系统未安装,会自动回退到 Times New Roman 或 Georgia 等经典衬线字体。

## 实现文件

字体配置主要在以下文件中:
- `/assets/css/extended/custom.css` - 全局字体样式定义

## 未来优化方向

如需确保所有访客都能看到 Noto Serif SC:
1. 可以通过 Google Fonts 引入 Web 字体
2. 需权衡页面加载性能与视觉一致性
3. 建议仅在必要时引入,当前方案已足够

## 参考资源

- [Noto Serif SC - Google Fonts](https://fonts.google.com/noto/specimen/Noto+Serif+SC)
- [思源宋体 - Adobe](https://github.com/adobe-fonts/source-han-serif)
- [UNTAG 网站](https://utgd.net/) - 设计参考

