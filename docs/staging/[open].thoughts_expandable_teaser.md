# Thoughts 列表展开交互 - 实现说明（Open Draft）

> 基于 2025-10-07 的当前代码状态整理，记录已落地的行为与仍未覆盖的待办项，供后续验收或二次迭代参考。

## 1. 实现概述
- Thoughts 卡片在首页、标签页、归档等列表中默认展示 3 行预览文本，并附带 `展开想法 ↓` 按钮。
- 点击按钮后卡片在原位置展开，展示完整 Markdown 内容、图片以及底部的 `进入详情页 →` 链接。
- 当前版本为「只展开不收起」，用户刷新或重新进入页面才会恢复预览态。

## 2. 关键体验与交互
- **预览态**：模板以 200 个字符为阈值截取摘要（追加省略号），CSS 继续使用 `-webkit-line-clamp: 3` 控制三行；字数不足时直接渲染全文且隐藏按钮。
- **展开行为**：按钮使用 `<button>` 元素；点击、Enter 或 Space 会：
  - 为卡片添加 `.expanded` 类，隐藏预览并展示完整内容容器；
  - 将 `aria-expanded` 设置为 `true`，按钮文案保持 `展开想法 ↓`；
  - 触发懒加载，立即为可见的 `data-src` 图片补全 `src`；
  - 延迟约 50ms 触发滚动，确保卡片顶端回到视口，顶部预留 60px 导航高度。
- **详情入口**：展开态底部出现 `进入详情页 →` 链接，并阻止冒泡避免触发整卡链接。
- **整卡链接**：收起态保留透明 `.entry-link` 覆盖层；展开后通过 CSS 关闭其 `pointer-events`，让正文与按钮可交互。
- **降级表现**：`<html>` 初始包含 `no-js`；脚本加载后替换为 `js`。无 JS 环境下按钮隐藏、内容保持三行、整卡链接仍可点击。

## 3. 技术实现要点
- **模板 (`layouts/partials/thought_card.html`)**：
  - 通过 `replaceRE` 去除 `{{< link >}}` 短代码，再 `plainify` 与 `htmlUnescape` 计算字符长度；判定 `len > 200` 时输出预览/全文双容器。
  - 为文章元素添加 `data-thought-id`，并在全文容器中包裹 `.thought-body.post-content` 与 `.thought-actions`。
- **脚本 (`assets/js/thought-expand.js`)**：
  - DOMContentLoaded 后初始化所有 `.thought-entry`，为每个卡片绑定展开、键盘触发、防止冒泡等逻辑。
  - `lazyLoadImages` 会将 `.content-full img[data-src]` 的 `data-src` 赋值给 `src` 并移除属性；同时注册 `IntersectionObserver` 在卡片进入视口前 50px 提前加载。
  - `scrollToCard` 依据卡片 `getBoundingClientRect()` 与当前滚动位置进行平滑滚动，顶部固定补偿 60px 并额外留出 20px 间距。
- **样式 (`assets/css/extended/custom.css`)**：
  - 定义 `.content-preview` 的三行截断、按钮样式、展开态显隐、图片尺寸与 `.thought-actions` 布局。
  - `.thought-entry.expanded` 下禁用 `.entry-link` 指针事件，并恢复正文区域的交互。
  - 针对 `prefers-reduced-motion` 移除过渡动画，移动端调大字体与点击区域。
- **资源注入 (`layouts/partials/extend_head.html`)**：
  - 通过 Hugo Pipes 压缩与指纹 `assets/js/thought-expand.js`，所有页面均加载该脚本。

## 4. 可访问性与性能
- 展开按钮与详情链接均可 Tab 聚焦，并支持 Enter/Space。展开后焦点保持在原按钮，未额外移动。
- 图片懒加载依赖作者在 Markdown 中赋予 `data-src`；未设置时将直接加载。
- `IntersectionObserver` 提升图片加载效率；旧浏览器不支持时仍在展开瞬间补齐 `src`。
- 默认仍保留整卡链接导航，满足键盘与屏幕阅读器使用者的跳转需求。

## 5. 与初版 PRD 的差异
- 尚未提供「收起」能力，也未实现展开后的文案切换或多媒体收起策略。
- 摘要阈值基于 200 字符而非严格的三行检测，文本溢出的判定来自模板层字符长度。
- `进入详情页` 仍为文本样式链接（复用 `.detail-link-btn`），未额外增强成按钮视觉。
- 未覆盖深链直接展开、初始状态判定等拓展场景。

## 6. 后续观察与建议
- 若需要收起功能，可在现有脚本上改为 toggle 模式并同步按钮文案与 `aria-expanded`。
- 可评估在生成阶段统一为图片添加 `data-src` 以降低内容维护成本。
- 顶部 60px 滚动补偿与导航高度耦合，若导航调整需同步修改脚本常量。
- 建议补充移动端与辅助技术的正式验收记录，并确认多媒体播放的收起策略。

> 如需恢复 PRD 视角或迭代更多规范，可在本实现说明基础上补充「后续计划」章节。
