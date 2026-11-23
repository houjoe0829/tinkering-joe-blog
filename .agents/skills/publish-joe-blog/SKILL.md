---
name: publish-joe-blog
description: 将 MindCraft 中的 Obsidian 笔记发布为 Joe 的 Hugo 博客文章。适用于用户说「发布到博客」「作为 blog 发布」或要求把当前笔记导入 tinkering-joe-blog。按已有博文处理正文、图片和图注，先提供本地预览，再按用户确认的范围发布。
---
## 导入博文
1. 用 `obsidian-cli` 读取用户指定的笔记，收集其中实际引用的图片、图注和链接。目标仓库是 `/Users/houjoe/Resilio/Mycodebase/tinkering-joe-blog`，博文写入 `content/posts/<slug>.md`，配图写入 `static/images/posts/<slug>/`。检查是否已有同一篇博文或同名路径。
2. 动手前读取仓库 `README.md` 的元数据与标签规则、`docs/specs/blog_styling_guide.md` 的「图片 Caption 样式规范」，再找一篇已发布的同类文章对照。可用 `content/posts/guangde-one-meal-trip.md` 对照图注结构。元数据按仓库约定填写，正文沿用原标题、措辞、段落和图片顺序。若正文开头重复了元数据中的标题，仅在博客副本中去掉重复标题。
3. 将本地配图按仓库已有方式转成 WebP，核对方向、比例和文字清晰度。遇到 `![[文件名|宽度]]` 或 `![[文件名|图注|宽度]]` 时，图注文字原样保留，宽度数字不能丢弃，需按原宽度输出带点击放大链接的 HTML 图片（`<a href="图片路径" class="post-image-zoom" target="_blank" rel="noopener"><img src="图片路径" alt="替代文字" style="width: 宽度px; max-width: 100%; margin: 1rem auto; display: block;" /></a>`）。未指定宽度的图片沿用普通 Markdown 图片语法。有图注时，再按样式规范在图片下方单独写出居中、小号、灰色斜体的可见图注。把仅在 Obsidian 生效的链接转换为已核实的博客链接，无法确定公开去向时先说明。
## 本地预览与发布
1. 按仓库说明和 `start-local-dev-server` 启动 Hugo 本地预览。打开实际渲染的文章，对照原笔记核验图片和可见图注的数量、对应关系与顺序，核对带宽度图片的实际显示宽度与居中效果，并与旧文比较图注的居中、颜色、字号、斜体和图片间距。检查正文分段及转换后的链接。图片成功加载和替代文字存在只能验证图片引用，可见图注要在页面中单独检查。
2. 把本地预览链接交给用户验收。确认后再按 `submit-commit` 提交博文、关联配图及仓库钩子自动更新的统计文件。推送前核对目标分支，并说明推送到 `origin/main` 会触发 Cloudflare Pages 自动部署。按用户的选择推送和关闭预览。默认以推送结果为交付状态，用户要求核实上线时再查部署或公开页面。
