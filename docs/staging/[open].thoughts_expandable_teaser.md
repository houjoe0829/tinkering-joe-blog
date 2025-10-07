# Thoughts 列表展开交互 - 产品需求文档（PRD）

## 1. 项目概述
- 当前 Thoughts 卡片在首页、标签页、相关文章推荐等列表位置仅展示三行内容，超出部分没有直接的延伸阅读入口，读者必须跳转详情页。
- 本次迭代希望引入可展开/收起的交互，让读者在列表位置快速阅读全文，同时保留卡片紧凑布局与现有标签区域。

## 2. 目标与成功指标
- 提升 Thoughts 卡片的可读性，增加列表位置的完读率。
- 控制页面信息密度，保障卡片展开后依然整洁有序。
- 次级指标：读者在展开后点击详情页按钮的转化率、展开与收起操作的完成率。

## 3. 范围界定
### 3.1 In Scope
- 首页混合流中的 Thoughts 卡片。
- 标签页、归档页、相关文章推荐区域里出现的 Thoughts 卡片。
- 桌面端与移动端的视觉与交互统一实现。

### 3.2 Out of Scope
- Blog（文章）卡片的展示逻辑与样式。
- Thoughts 详情页本身的内容结构与评论功能。

## 4. 体验设计
### 4.1 默认预览态
- 文本通过 CSS 限制在三行展示，样式与当前实现一致。
- 若正文不足三行，保持原样，无额外交互控件。
- 卡片右下角的标签、发布日期等元素位置不变。

### 4.2 展开态
- 当正文被截断时，在第三行末尾追加 `展开想法` 交互。
- 点击后卡片在原位置展开，展示完整 Markdown 内容（不含评论）。
- Thoughts 中的图片、音频、视频等多媒体元素在展开状态下原样呈现，以促使作者主动控制篇幅。
- 展开后交互文案切换为 `收起`，再次点击恢复三行摘要。
- 展开/收起时保持卡片宽度不变，避免影响周围布局；滚动位置尽量保持卡片顶端在视口内。

### 4.3 收起态
- `收起` 点击后恢复三行限制，同时隐藏 `进入详情页` 按钮，仅保留原卡片的跳转方式。
- 若用户在展开态操作多媒体（如播放音频），收起时需要明确定义状态（默认直接停止播放）。

### 4.4 详情页入口
- 展开态下，在正文底部与标签区域之间新增按钮样式的 `进入详情页` 入口。
- 按钮点击后按照现有逻辑跳转到该 Thought 的详情页。

## 5. 交互细节
- 展开/收起动画时长不超过 200ms，过渡曲线建议使用 ease-in-out。
- `展开想法`、`收起`、`进入详情页` 均需支持键盘 Tab 聚焦与 Enter/Space 触发。
- 当键盘用户展开内容时，应确保焦点留在触发控件上，避免焦点意外跳转。
- 若页面加载时卡片已在展开状态（未来可能的深链场景），需要正确渲染按钮与标签位置。

## 6. 视觉与排版要求
- `展开想法`/`收起` 的文案样式需与正文区分（颜色或下划线），但保持同一行内展示；若存在省略号，置于控件前。
- `进入详情页` 采用按钮视觉，建议使用次级按钮（副按钮）样式，以免与主要 CTA 冲突。
- 展开后卡片右下角标签区域仍固定在卡片底部；必要时为标签区域设置定位或撑开容器高度，避免被正文或按钮覆盖。
- 多媒体的最大宽度与卡片宽度一致，超出需自动缩放；高度可按原比例显示，可选懒加载或占位图以优化性能。

## 7. 内容与多媒体策略
- Thoughts 作者可继续使用 Markdown 插入图片、音频、视频；列表中默认不屏蔽多媒体。
- 推荐对图片启用懒加载，对音视频提供静态封面或播放控件，防止首屏阻塞。
- 若多媒体加载失败，需保留占位符并可点击进入详情页查看完整内容。

## 8. 技术实现要点

### 8.1 当前架构分析
**存在的技术障碍：**
1. Hugo 模板当前只输出截断的纯文本摘要（200 字符），完整的 Markdown 渲染内容未包含在 HTML 中
2. 卡片使用透明链接覆盖层（`.entry-link`）实现整卡可点击，会拦截内部按钮点击事件
3. 内容使用 CSS `-webkit-line-clamp: 3` 控制三行显示，但没有完整内容可供展开

**涉及的文件：**
- `layouts/partials/thought_card.html` - Thoughts 卡片模板
- `layouts/_default/list.html` - 列表页模板
- `assets/css/extended/custom.css` - 自定义样式（443-455 行）
- `assets/js/` - 需新增交互脚本

### 8.2 Hugo 模板层改造

**修改 `thought_card.html`：**
1. 同时输出摘要和完整渲染内容两个版本：
   - 摘要版本：保持当前逻辑，用于默认预览态
   - 完整版本：使用 `.Content` 输出完整 Markdown 渲染结果，默认隐藏
2. 在模板中判断内容是否超过三行：
   - 计算 `plainify` 后的字符数或行数
   - 只在内容溢出时添加「展开想法」按钮
3. 为卡片添加唯一标识（如 `data-thought-id`）以便 JS 定位

**示例结构：**
```html
<article class="thought-entry" data-thought-id="{{ .File.UniqueID }}">
  <div class="entry-content">
    <!-- 摘要版本（默认显示） -->
    <div class="content-preview">
      <p>{{ $summary }}...</p>
      <button class="expand-btn" aria-expanded="false">展开想法</button>
    </div>
    
    <!-- 完整版本（默认隐藏） -->
    <div class="content-full" style="display: none;">
      {{ .Content }}
      <button class="collapse-btn">收起</button>
      <a href="{{ .Permalink }}" class="detail-link-btn">进入详情页</a>
    </div>
  </div>
  
  <footer class="entry-footer">
    <!-- 标签和日期 -->
  </footer>
  
  <!-- 只在收起状态下启用整卡链接 -->
  <a class="entry-link" href="{{ .Permalink }}"></a>
</article>
```

### 8.3 CSS 样式调整

**修改 `custom.css` 中的 Thoughts 相关样式：**

1. **预览态样式**（保持三行截断）：
```css
.thought-entry .content-preview p {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

2. **展开按钮样式**：
```css
.thought-entry .expand-btn {
  display: inline;
  color: var(--primary);
  text-decoration: underline;
  background: none;
  border: none;
  padding: 0;
  font-size: inherit;
  cursor: pointer;
  position: relative;
  z-index: 2; /* 高于 entry-link */
}
```

3. **完整内容样式**：
```css
.thought-entry .content-full {
  /* 展开动画 */
  transition: opacity 0.2s ease-in-out;
}

.thought-entry.expanded .content-preview {
  display: none;
}

.thought-entry.expanded .content-full {
  display: block;
}

/* 展开态下禁用整卡链接 */
.thought-entry.expanded .entry-link {
  pointer-events: none;
}
```

4. **进入详情页按钮样式**：
```css
.thought-entry .detail-link-btn {
  display: inline-block;
  margin-top: 15px;
  padding: 8px 16px;
  background: var(--tertiary);
  border-radius: 6px;
  color: var(--content);
  text-decoration: none;
  position: relative;
  z-index: 2;
}
```

5. **响应 prefers-reduced-motion**：
```css
@media (prefers-reduced-motion: reduce) {
  .thought-entry .content-full {
    transition: none;
  }
}
```

### 8.4 JavaScript 交互逻辑

**新建 `assets/js/thought-expand.js`：**

```javascript
document.addEventListener('DOMContentLoaded', function() {
  // 初始化所有 Thoughts 卡片
  const thoughtCards = document.querySelectorAll('.thought-entry');
  
  thoughtCards.forEach(card => {
    const expandBtn = card.querySelector('.expand-btn');
    const collapseBtn = card.querySelector('.collapse-btn');
    const entryLink = card.querySelector('.entry-link');
    
    if (!expandBtn) return; // 内容未溢出，无需交互
    
    // 展开逻辑
    expandBtn.addEventListener('click', function(e) {
      e.stopPropagation(); // 阻止事件冒泡到 entry-link
      e.preventDefault();
      
      card.classList.add('expanded');
      expandBtn.setAttribute('aria-expanded', 'true');
      
      // 懒加载图片
      lazyLoadImages(card);
      
      // 保持卡片顶部在视口内
      scrollToCard(card);
    });
    
    // 收起逻辑
    collapseBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      e.preventDefault();
      
      card.classList.remove('expanded');
      expandBtn.setAttribute('aria-expanded', 'false');
      
      // 停止所有多媒体播放
      stopMedia(card);
      
      scrollToCard(card);
    });
    
    // 键盘支持
    [expandBtn, collapseBtn].forEach(btn => {
      btn.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          btn.click();
        }
      });
    });
  });
  
  // 懒加载图片
  function lazyLoadImages(card) {
    const images = card.querySelectorAll('.content-full img[data-src]');
    images.forEach(img => {
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
    });
  }
  
  // 停止多媒体播放
  function stopMedia(card) {
    const videos = card.querySelectorAll('video');
    const audios = card.querySelectorAll('audio');
    
    videos.forEach(v => v.pause());
    audios.forEach(a => a.pause());
  }
  
  // 滚动到卡片顶部
  function scrollToCard(card) {
    const rect = card.getBoundingClientRect();
    if (rect.top < 0) {
      card.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
});
```

### 8.5 内容溢出检测

**在 Hugo 模板中判断是否需要展开按钮：**

```go
{{- $cleanedContent := .RawContent | replaceRE "{{< link .*? >}}" "" -}}
{{- $plainContent := $cleanedContent | plainify | htmlUnescape -}}
{{- $needsExpand := gt (len $plainContent) 200 -}}

{{- if $needsExpand -}}
  <!-- 显示展开按钮 -->
{{- end -}}
```

或在 JavaScript 中动态检测：
```javascript
// 检测内容是否超过三行
function checkOverflow(element) {
  return element.scrollHeight > element.clientHeight;
}
```

### 8.6 性能优化

1. **图片懒加载**：
   - 完整内容中的图片使用 `data-src` 属性
   - 展开时才加载图片资源
   - 使用 `IntersectionObserver` API 进一步优化

2. **内容复用**：
   - 避免在 HTML 中重复输出相同内容
   - 考虑使用 `<template>` 标签存储完整内容

3. **首屏优化**：
   - 只为首屏可见的卡片立即执行 JS 初始化
   - 其他卡片延迟初始化

### 8.7 降级方案

**无 JavaScript 环境下：**
1. 不显示「展开想法」按钮
2. 保持整卡链接可点击，跳转到详情页
3. 在 CSS 中使用 `:has()` 选择器提供部分支持（现代浏览器）

```css
/* 无 JS 环境下隐藏交互按钮 */
.no-js .expand-btn,
.no-js .collapse-btn {
  display: none;
}
```

### 8.8 兼容性验证

**需要测试的场景：**
1. 首页混合流中的 Thoughts 卡片
2. 标签页列表
3. 归档页列表
4. 相关文章推荐区域
5. 移动端触摸交互
6. 键盘导航
7. 屏幕阅读器

**浏览器兼容性：**
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- 移动端 Safari/Chrome


## 9. 可访问性要求
- 交互控件需使用语义化元素（例如 `<button>`），并提供 ARIA 标签（如 `aria-expanded`）。
- 动画应尊重 `prefers-reduced-motion` 设置，必要时提供无动画降级。
- 确保按钮与文本的颜色对比度符合 WCAG AA 标准。

## 10. 验收标准
- 溢出的 Thoughts 卡片展示 `展开想法`；点击后全文展开并显示按钮样式的 `进入详情页`，再点击 `收起` 恢复三行。
- 不溢出的 Thoughts 卡片无额外控件，交互与当前一致。
- 展开态下多媒体内容完整可见，标签区域始终位于卡片右下角。
- 交互在桌面端与移动端均正常，键盘可操作，动画流畅。

## 11. 未决事项
1. 多媒体的懒加载方案与占位样式需要与前端开发确认，实现成本与性能收益的平衡。
2. 展开态播放音视频后收起时是否强制停止播放，需产品/体验确认。
3. `进入详情页` 按钮的具体层级与尺寸（如是否需要全宽按钮）待视觉设计稿确认。
