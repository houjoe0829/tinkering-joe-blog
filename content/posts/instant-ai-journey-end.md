---
author: "Joe"
date: 2026-02-12
description: "Instant AI 的短暂旅程，从 Quick AI 的设计到 Instant AI 的上线与下线"
draft: false
tags: ["AI 相关", "Vibe Coding", "工作感悟"]
title: "Instant AI 的短暂旅程，我的第一款 Mac 客户端下线了"
---

可能没人会在意一个小产品的下线，但一件事总得有始有终。

Instant AI 是我做的一个极简风格的 AI 客户端，基于 Electron，界面只有一栏，没有多余的东西。现在，我准备把它下线了。

![CleanShot 2026-02-12 at 21.29.18@2x.png](/images/posts/instant-ai-journey-end/CleanShot_2026-02-12_at_2129182x.webp)

## 比 Instant AI 更早的故事

其实这个产品的想法比 Instant AI 本身要早得多。刚开始有 AI 的时候，我就想做一个极简的 AI 客户端，当时和一个做 Swift 开发的朋友一起，设计了最早的一版，名字叫 Quick AI。

不过那个时候 AI 编程的能力还很差，只能以传统的方式来协作。我们都是以兼职在推，进度很慢，只推进到了 Demo 阶段，OpenCat 就出了。加上我自己构建产品的一个经验，超过一定时间没有明显进展，就及时止损。Quick AI 就这样停在了那里。

![Quick AI 的设计稿](/images/posts/instant-ai-journey-end/CleanShot_2026-02-12_at_2109492x.webp)

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>Quick AI 的设计稿 </em>
</div>

## 一个刚好的时机

等到想法再次被唤醒，是 DeepSeek 出了，由于算力紧张，各大云服务商的第三方 Token 一下子火了起来。

这次我找到了一个开源项目 [DeepChat](https://deepchat.thinkinai.xyz/)，决定基于它来做。产品的核心理念没变，还是极简，能省则省，再加上类似 [Slidepad](https://slidepad.app/) 那样随时在窗口边缘可以唤出的交互。

不过说实话，做这个产品的主要目的，是我想亲自尝试一遍客户端的编译、打包、签名、分发的完整流程，也是 Vibe Coding 路途上的一次重要实验。

![上线推文](/images/posts/instant-ai-journey-end/CleanShot_2026-02-12_at_2113242x.webp)

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em> 上线推文: <a href="https://x.com/houjoe1/status/1897850866956484666">https://x.com/houjoe1/status/1897850866956484666</a></em>
</div>

就这样，Instant AI 上线了，这也是我的第一款 Mac 客户端。上线之后得到了许多推友的点赞和转发助力，算是一次不错的反馈了。

## 免费的代价

Instant AI 从一开始就是完全免费的。原因很简单，我的 AI Coding 经验不足，不知道能维护多久，索性不对用户做任何承诺。这确实不是做产品的态度，但当时觉得这样最诚实。

后来发现，确实很难维护，很多看起来简单的 Bug 都费了极大的气力来修复。而免费也意味着，后续维护缺少动力。当 Claude、ChatGPT 的客户端越来越好用的时候，我自己也不再打开 Instant AI 了。一个连自己都不用的产品，继续维护下去也没有意义。

## 有始有终吧

所以，就让它在这里好好结束……

不过，持续构建产品，依然是我的愿景。

虽然 Instant AI 下线了，但其中的很多思路我还会用到后续的产品里。比如那个单栏的设计，依然是我会持续追求的极简风格。产品不会一次就成功，重要的是一直在做。说不定哪天，你会在另一个产品里再次看到它的影子。
