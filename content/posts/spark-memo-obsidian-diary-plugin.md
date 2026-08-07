---
title: "成年人也写日记，我为 Obsidian 做了个日记插件"
date: 2026-08-06T20:00:00+08:00
draft: false
description: "Spark Memo：把想法和日记直接存进 Obsidian 的 Daily notes，带照片时间与地理位置，还能聚合成一张足迹地图。"
tags: ["折腾软硬件", "造物笔记"]
author: "Joe"
---

我为 Obsidian 做了一款记录想法和日记的插件 [Spark Memo](https://community.obsidian.md/plugins/spark-memo)，桌面端和手机端都能用。所有日记直接存进 Daily notes，能和 Obsidian 已有的笔记互动，数据也完全在自己手里。

对于记录，我自己的习惯是先拍照，再补文字。当下来不及写，拍一张就等于先占住了那一刻，隔几天再回来补也不怕漏。Spark Memo 就是从这儿来的：添加图片时自动读取照片里的时间和地理位置，可以回到当初那个时间、那个地方。

<img src="/images/posts/spark-memo-obsidian-diary-plugin/memo-photo-meta.webp" alt="添加图片时自动读取照片的时间与地理位置" style="width: 443px; max-width: 100%; margin: 1rem auto;" />

而且，所有带地理位置的想法会聚合成一张足迹地图。下图是我的 2733 条 Memos 铺开之后的样子。

<img src="/images/posts/spark-memo-obsidian-diary-plugin/footprint-map.webp" alt="足迹地图" style="width: 441px; max-width: 100%; margin: 1rem auto;" />

如果你坚持记录，还可以看到每天的进步，以热力图的形式来标记。

<img src="/images/posts/spark-memo-obsidian-diary-plugin/heatmap.webp" alt="记录热力图" style="width: 444px; max-width: 100%; margin: 1rem auto;" />

## 为什么要做它？

哎…… 做这个插件的目的其实是为了不做它。

作为一个长期设计生产力工具的 PM，Vibe Coding 之后，我很难按捺住手里的 AI 「超能力」，总是想对自己常用的工具做定制化改造，比如笔记，比如番茄钟…… 甚至年初的几个月，我完整开发出了跨 iOS、Mac 版本的笔记 App，基于 iCloud 同步，并迭代了三个月。但最终，我选择让它沉寂在我的代码仓库里，下图是半年前完成跨端同步的效果，也算留个纪念，至少它的名字和理念还是传承下去了。

![半年前完成的跨端同步效果](/images/posts/spark-memo-obsidian-diary-plugin/old-note-app.webp)

这次也一样，我既想实现这个速记的需求，也知道它收益极低，并且，我不想做个半成品的玩具，现在最不缺的就是这个了。

说到底，构建产品变简单了，但涉及数据存储的工具，还是得有点责任心，它需要长时间打磨，也需要一直维护下去，哪怕我哪天停下来，用户的数据也得还在。能力大了，责任也得有。

这么一想，Obsidian 的插件差不多就是最佳选项了。

开发成本不大，我是基于另外一个插件的开源代码 Fork 之后改造的，这在[仓库](https://github.com/houjoe0829/sparkmemo)里有备注，只是需要花时间打磨一下细节。数据格式是开放的，完全基于 Obsidian Daily notes 的 Markdown，即使哪天我不再维护代码了，Markdown 的数据也照样可读可写。另外，Obsidian 本身已经非常稳定，是个足够成熟的软件基底。

开始构建之后，Spark Memo 在六月份的时候，已经发布了一版，直到今天，才发布 0.2.0 版本，我觉得这已经是接近最终版的效果了，终于可以在地图上游览所有带地理位置信息的 Memo。

回到开头那句，做完 Spark Memo 反而平和了，这样可以腾出时间做其他我觉得更有趣的产品，而不用困在「笔记工具」的梦里。

不过，我会一直用，所以也会一直迭代下去。

## 为什么做成 Obsidian 的插件？

一句话总结的话，就是数据 All in one，又完全属于自己的魅力。自从 Notion 开启发疯式的迭代之后，我开始回归最简单的 Markdown 文件和文件夹来撰写笔记。

做成插件的好处也就跟着来了，一是能接上 Obsidian 已有的笔记和标签体系，双向链接也正常生效，我在侧边栏写想法的时候，经常直接 @ 一篇已有的笔记。

二是复用 Obsidian 的基建，最核心的是 Obsidian CLI，原生对接所有的 AI Agent。

更重要的是，数据是通用的 Markdown，代码也开源，你完全可以让自己的 Agent 读一遍，把散在其他地方的日记转换成 Spark Memo 的格式。

这正好是我迁移 Day One 的动力之一。我自己是超过十年的 Day One 用户，它是我最喜欢的日记软件，没有之一，但现在也成了信息孤岛，虽说支持 AI 读取，效率却极低。

不过迁移的时候记得先小范围试一批，确认没问题再批量导入，不然容易留下一堆脏数据。

数据聚合之后，我每次在罗列周计划时，都会先让 AI 读取 Spark Memo 过去一周的日记。日记记的是实际发生了什么，周计划记的是本来打算做什么，两边一对照，上周哪些完成了、哪些落下了就很清楚。AI 再结合 Obsidian 里的年度计划，直接生成新一周的周计划建议。

## 打开的新世界

安装这个插件比较简单，直接在 Obsidian 的社区插件里搜索 Spark Memo 就行，也可以访问 https://community.obsidian.md/plugins/spark-memo 。

不过安装只是其中一种用法。如果你自己也折腾代码，完全可以 fork [我的代码](https://github.com/houjoe0829/sparkmemo)，按自己的想法来改造。

这套存储方式其实是个很值得借鉴的套路。只要一个 App 有自己的数据，都可以方便地挪进来，做成 Obsidian 插件来维护。

我自己就把一些原本跑在 Nas 上的应用转了过来，比如番茄钟工具，只给自己用，完全没发布。转过来之后，它自动就有了那些好处：能和已有的笔记互动，能被 AI 读取，数据也还是本地的 Markdown 文件。

这个是我的番茄钟工具 Flow，之前在我的 Nas 的 Docker 上。

<img src="/images/posts/spark-memo-obsidian-diary-plugin/flow-1.webp" alt="番茄钟工具 Flow" style="width: 444px; max-width: 100%; margin: 1rem auto;" />

<img src="/images/posts/spark-memo-obsidian-diary-plugin/flow-2.webp" alt="Flow 的统计界面" style="width: 445px; max-width: 100%; margin: 1rem auto;" />

这有两个有趣的结果。

一个是，那些不足以撑起一个产品的想法，可以让它先以最简单机制运行在自己的「内容」上，慢慢成长着，说不定未来会有意外收获，就像我的 [Roam FM](https://roamfm.app/)。

另一个是，靠各种插件和 CSS 片段，除了 Obsidian 本身的软件访问和数据结构呈现，其他我基本都自己定制了，比如笔记内容的渲染、与 AI 的集成、界面标签页的行为……

所以这东西特别适合爱折腾的人。有了 AI、这套 Obsidian CLI、庞大的插件生态，再加上 CSS，可玩性几乎没有上限，折腾它本身就已经挺有趣了。
