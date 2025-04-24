---
title: "关于我"
date: 2024-02-10
draft: false
description: "了解更多关于 Joe 的信息"
hideMeta: true
---

## 👨‍💻 自我介绍

我是 Joe，不知名的产品经理，主业与兴趣都是设计各类 ToC 或者 ToB 生产力工具.

`Coding with AI`、`Product Manager`、`喜欢码字`、`Nas 小白用户`、`无人机机长`、`主机游戏玩家`、`有个流浪猫`、`江浙沪包游中`、`骑行新手`、`顺风车司机`

主要涉及的产品领域：编辑器、协同文档、笔记工具、Database、白板，以及 AI。

产品经历：[Evernote](https://evernote.com/)、[AFFiNE](https://affine.pro/)、[轻雀文档](https://qingque.cn/products/docs)、[轻雀协作](https://qingque.cn/practice)

## 📮 找到我

如果有任何问题、合作想法或只是想打个招呼，欢迎通过以下方式找到我：

- 📧 **Email**：[houqiao829@gmail.com](mailto:houqiao829@gmail.com)
- 🐦 **Twitter**：[@houjoe1](https://x.com/houjoe1) - 更新比较随意，私信开放！
- 🐙 **GitHub**：[houjoe0829](https://github.com/houjoe0829) -  我也开始写代码了……
- 💬 **Wechat**：微信号[houjoe829]  -  请备注来意

## 🔧 我的日常工具包

<p class="toolkit-description">定期整理自己在用的软硬件工具，方便断舍离，减少不必要的分心。</p>

<div class="bento-container">
  <a href="/posts/current-software-hardware-toolkit/" class="bento-card software">
    <div class="card-content">
      <div class="card-icon">📱</div>
      <h3>软件工具</h3>
      <p>我日常使用的各类软件工具，包括记录与文档、浏览器、任务管理、阅读、音乐、AI 助手等</p>
      <span class="read-more">查看详情 →</span>
    </div>
  </a>
  
  <a href="/posts/current-software-hardware-toolkit/#硬件部分" class="bento-card hardware">
    <div class="card-content">
      <div class="card-icon">💻</div>
      <h3>硬件装备</h3>
      <p>我的随身和随车硬件装备，包括电脑、耳机、手机、无人机、折叠自行车等</p>
      <span class="read-more">查看详情 →</span>
    </div>
  </a>
</div>

<style>
:root {
  --card-background: #fff;
  --border-color: #eaeaea;
  --text-color: #333;
  --shadow-color: rgba(0,0,0,0.08);
  --shadow-hover-color: rgba(0,0,0,0.12);
  --primary-color: #0066cc;
  --software-gradient: linear-gradient(135deg, #e0f7fa, #bbdefb);
  --hardware-gradient: linear-gradient(135deg, #f3e5f5, #e1bee7);
  --audio-gradient: linear-gradient(135deg, #fff8e1, #ffecb3);
  --ai-gradient: linear-gradient(135deg, #e8f5e9, #c8e6c9);
  --software-dark-gradient: linear-gradient(135deg, #0d4b63, #0a3d62);
  --hardware-dark-gradient: linear-gradient(135deg, #4a235a, #512e5f);
  --audio-dark-gradient: linear-gradient(135deg, #5d4037, #6d4c41);
  --ai-dark-gradient: linear-gradient(135deg, #1b5e20, #2e7d32);
}

@media (prefers-color-scheme: dark) {
  :root {
    --card-background: #1f1f1f;
    --border-color: #333;
    --text-color: #e0e0e0;
    --shadow-color: rgba(0,0,0,0.2);
    --shadow-hover-color: rgba(0,0,0,0.3);
    --primary-color: #5c9eff;
  }
}

.bento-container, .projects-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin: 30px 0;
}

.bento-card {
  position: relative;
  border-radius: 16px;
  overflow: visible;
  box-shadow: 0 4px 20px var(--shadow-color);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  text-decoration: none;
  color: var(--text-color);
  background-color: transparent;
  border: none;
  box-sizing: border-box;
  padding-bottom: 1px; /* 添加额外的底部内边距 */
}

.bento-card {
  background: var(--card-background);
}

.bento-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 16px;
  z-index: 0;
}

.bento-card.software::before {
  background: var(--software-gradient);
}

.bento-card.hardware::before {
  background: var(--hardware-gradient);
}

.bento-card.audio-project::before {
  background: var(--audio-gradient);
}

.bento-card.ai-project::before {
  background: var(--ai-gradient);
}

.bento-card {
  color: #333;
}

@media (prefers-color-scheme: dark) {
  .bento-card.software::before {
    background: var(--software-dark-gradient);
  }
  
  .bento-card.hardware::before {
    background: var(--hardware-dark-gradient);
  }
  
  .bento-card.audio-project::before {
    background: var(--audio-dark-gradient);
  }
  
  .bento-card.ai-project::before {
    background: var(--ai-dark-gradient);
  }
  
  .bento-card {
    color: #fff;
  }
}

.bento-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 12px 30px var(--shadow-hover-color);
}

/* 添加伪元素创建边框效果 */
.bento-card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 16px;
  background: transparent;
  z-index: -1;
}

.card-content {
  padding: 24px;
  height: 100%;
  display: flex;
  flex-direction: column;
  position: relative;
  z-index: 1;
}

.card-icon {
  font-size: 2.5rem;
  margin-bottom: 16px;
  display: inline-block;
}

.card-content h3 {
  margin-top: 0;
  margin-bottom: 12px;
  font-size: 1.5rem;
  font-weight: 600;
}

.card-content p {
  margin-bottom: 20px;
  line-height: 1.6;
  flex-grow: 1;
}

.read-more {
  display: inline-block;
  font-weight: 500;
  margin-top: auto;
  padding: 6px 0;
  position: relative;
}

.read-more:after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: currentColor;
  transition: width 0.3s ease;
}

.bento-card:hover .read-more:after {
  width: 100%;
}

@media (max-width: 768px) {
  .bento-container {
    grid-template-columns: 1fr;
  }
}
</style>


## 🌟 Side Projects

<div class="bento-container projects-container">
  <a href="https://omniaudio.info/" class="bento-card audio-project">
    <div class="card-content">
      <div class="card-icon">🎧</div>
      <h3>OmniAudio</h3>
      <p>AI 稍后再听服务，将网页文章、文档转化为私人播客，生成可直接在 Podcast 应用中订阅收听的 Feed URL，让你随时随地，轻松畅听信息。</p>
      <span class="read-more">访问网站 →</span>
    </div>
  </a>
  
  <a href="https://instantai.houjoe.me/" class="bento-card ai-project">
    <div class="card-content">
      <div class="card-icon">🤖</div>
      <h3>Instant AI</h3>
      <p>一款极简风格的 Mac 版 AI 客户端，支持侧滑快捷访问，无缝连接多种主流大语言模型，完全免费。</p>
      <span class="read-more">访问网站 →</span>
    </div>
  </a>
</div>

