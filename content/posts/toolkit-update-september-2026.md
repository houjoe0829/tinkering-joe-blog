---
author: "Joe"
date: 2026-10-06T16:23:52+08:00
description: "最近半年，围绕 Obsidian 改造自己的 AI、笔记和日常小工具，也换了一些随身软硬件。"
draft: false
tags: ["折腾软硬件", "提升幸福感的好物", "AI 相关"]
title: "我的工具包，最近更新了什么？｜202609"
---

折腾手头常用的工具包一直是我的最爱，那种感觉，像是在一点点设计自己的生活，一边精挑细选，搭出顺手的组合，一边把旧的工具淘汰或者升级，包括软件和硬件，乐此不疲。

为了保持一种持续性，我在个人博客里留着一个页面，把在用的所有工具组合罗列在上面，定期更新，每次分享只需丢出链接，我叫它工具包。最近这半年，这份清单变了很多，也值得简单写一写了，就像代码仓库的更新一样，给这个清单变更提交一次 Commit。

工具清单页面→： https://houjoe.me/posts/current-software-hardware-toolkit/

如果要总结的话，Obsidian 是这次工具变化的基本盘。

## 使用 AI 的方式变了

我几乎不怎么用各家 Agent 的官方客户端。

也是因为，有点厌烦现在 Agent 客户端的通货膨胀。越来越长的侧边栏，已经掩饰不住各家厂商的野心，什么都往里面加，而我只用里面那个小小的对话框。相比之下，电脑终端里的 Agent 就成了一片净土，只有一个一个的对话。而且它活在终端里，意味着，我能处理的，它也基本都可以。

<img src="/images/posts/toolkit-update-september-2026/ai-client-sidebar.webp" alt="某国产 AI 的侧边栏" style="width: 281px; max-width: 100%; margin: 1rem auto;" />

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>某国产 AI 的侧边栏</em>
</div>

更具体一点，我也不是直接在终端里使用 Agent。尽管有着层出不穷的 Mac 终端工具，最终仍然选择依托各家 Agent 的 CLI（命令行界面），构建自己的 Agent，把它做在 Obsidian 里，方便与自己的笔记互动，比如 Claude Code CLI、Codex CLI 或者 Cursor CLI。界面主要就是简约的对话列表，还可以显示与 Obsidian 笔记关联的对话。现在，我能知道某条笔记和哪些 Agent 对话有关，是把全文作为对话上下文，还是划线引用，抑或 AI 修改了其中的内容。

<img src="/images/posts/toolkit-update-september-2026/craftian-sidebar.webp" alt="Obsidian 里个人 Agent 的侧边栏效果" style="width: 437px; max-width: 100%; margin: 1rem auto;" />

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>Obsidian 里个人 Agent 的侧边栏效果</em>
</div>

改造 Agent 的过程，也是了解 Agent 的过程，上下文的处理、对话的呈现、Harness 的加固，让人乐此不疲。甚至，我经常会有种内疚感，因为把太多时间花在了构建自己的 Agent 这件「无用的」事情上。

而且，这种折腾也没停在电脑上。我给自己的 Agent 做了个移动端的搭档，也是放在 Obsidian 里，这样手机和电脑引用上下文的方式就统一了，还能远程操控电脑。这和单纯各端自己接入 API 不一样，两者共同使用一套改装之后的 Agent 和环境，都是满血版 AI。

用着用着，手机也逐渐成了使用 AI 更有趣的场景。很多想法，就是在路上，在马桶上，在睡前的床上，和电脑上的 Agent 聊着聊着，慢慢想清楚的。那些打发时间的间隙，我可以从收件箱里挑出一个想法，和 Agent 拆解一下，等到研究得差不多了，正好存个笔记或者 Memo 到 Obsidian 里。

现在用手机和电脑跟 AI 聊天的比例，大概是 4∶6 吧。

## 使用笔记的方式变了

之前记笔记，用的是一堆工具的组合，Notion + Day One + Whimsical，现在换成了 Obsidian，其实，我只关心存储在本地的那一堆通用 Markdown 格式的数据文件。

但我还是保留自己的偏见，从上手体验来说，依然非常不推荐 Obsidian。因为它像是一个毛坯房，哪怕只是想要简单的跨设备同步，都要自己折腾一下，但也恰恰因为它是个毛坯房，什么都可以按自己的想法来改装。

比如，Obsidian 本身不支持协作，我就做了笔记的发布体系，需要协作时，一键发布到飞书，在飞书里一起编辑和评论，信息的主版本仍然保留在 Obsidian。只是分享的话，也可以发布到自己的 NAS 上，自动生成一个公开的网页，连呈现的样式都可以自定义。

写日记也是我的日常，所以我自己做了插件 [Spark Memo](https://houjoe.me/posts/spark-memo-obsidian-diary-plugin/)，替代之前的 Day One，日记也统一存储在 Obsidian 里。

连画图也可以在笔记里完成。手动绘制流程图基本成了过去式，让 AI 用 Mermaid 来画，原型图则用 ASCII 来呈现。两种图都可以在 Markdown 里用文本编辑并直接渲染，不用另外打开一个画图工具。

## 迷上 DIY 自己的小工具

除了 AI Agent 和笔记，DIY 日常会用到的工具也是折腾的一部分。有些会在本地慢慢生长，有些最终会发布成产品，更多的则只是活在我的 Obsidian 里，以插件的形态。

我舍弃了经典的 Reeder 和之前有争议的 Folo 等 RSS 阅读工具，自己做了一款阅读器，也放在 Obsidian 里。它可以订阅 RSS 文章和 Newsletter，也能添加单篇文章，留着稍后阅读。很自然地，这些内容也都可以和 Obsidian 里的自制 Agent 互动。

我依然喜欢这种订阅式的阅读，读什么由自己挑选，不用算法替我决定。

<img src="/images/posts/toolkit-update-september-2026/rss-reader.webp" alt="Obsidian 插件：RSS 阅读器" style="width: 1041px; max-width: 100%; margin: 1rem auto;" />

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>Obsidian 插件：RSS 阅读器</em>
</div>

阅读之外，还有一个专注计时工具 Flow。此时在写下这些文字的时候，它就这样在 Obsidian 侧边栏开着，一次 30 分钟，这期间安心只做一件事情，最终的记录也会存储在 Obsidian 里。

<img src="/images/posts/toolkit-update-september-2026/flow-focus-timer.webp" alt="Obsidian 插件：Flow" style="width: 419px; max-width: 100%; margin: 1rem auto;" />

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>Obsidian 插件：Flow</em>
</div>

除了这些 Obsidian 插件，我也做了一些已经发布的 DIY 小工具：

- [Roam FM](https://roamfm.app/)，将全球电台作为背景音乐的 Mac 菜单栏工具。
- [Copy URL](https://copyurl.houjoe.me/)，一款方便以不同格式复制浏览器链接地址的 Chrome 插件。
- [OmniAudio](https://omniaudio.info/)，将文章一键转换为可订阅的私人播客的工具，方便路上听文章。

## 其他工具

当然，工具清单的变更不止 Obsidian 相关，也不止软件。

### 语音输入的王者：Typeless

Twitter 上依然保持着隔几天一款新的开源或者「平替」产品的出现，但始终无法超越 Typeless 在我心中的地位。

这半年里，它已经帮我完成了超过 36 万字的语音输入。单看这个数字，可能没什么概念，但它已经比我自己这么多年写过的所有博客文章加起来还要多，码字还是太少了。

语音输入的意义，也不只是输入得更快。有了它之后，很多原本可能因为懒得打字而省略的想法，现在都可以直接说出来。AI 像一个巨大的宝藏，需要不断提问、追问，才能慢慢挖掘出更多。我们的思路、看法、做决策的背景，讲得越清楚，也越容易得到有帮助的回答。不应该让打字的麻烦，挡住这些有趣也有价值的互动。

不过，码字本身依然是语音输入最少的场景，也是少有的我需要文字跟着我一起思考的过程。

<img src="/images/posts/toolkit-update-september-2026/typeless-statistics.webp" alt="Typeless 的输入统计" style="width: 843px; max-width: 100%; margin: 1rem auto;" />

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>Typeless 的输入统计</em>
</div>

### AirPods 5

拿到手的第一感觉是，现在的无线耳机居然已经做的这么小巧了。

这是今年我唯一跟着官方更新换新的产品。佩戴舒适，降噪也够用。后来，我在闲鱼卖掉了自己的 AirPods Max 一代（头戴耳机），它在嘈杂环境的通话体验实在糟糕，平时能用到的地方也不多，但胜在可以在多台苹果设备之间无缝切换。

开车的路上，我会开启 AirPods「自适应模式」，带一点轻度降噪，既能听见周围的声音，也能更沉浸听听播客。在车机上有了官方的豆包之后，和豆包对话也不用再依赖之前那副单独的豆包耳机了。

不过，用得更多的还是开会。它替代了之前的有线耳机和 AirPods Max，比较意外的是收音效果，这次自驾到宜昌的时候，可以在车流川息的路边无干扰得完成一场线上会议。

还有一个用途，戴着睡觉。尤其是白天有点困，想睡 15 分钟回回血的时候。以前会戴上 AirPods Max，现在直接戴上更轻便的 AirPods 5，开启降噪就行了，够用。

这么一来，出门也轻省了不少，头戴耳机、有线耳机、豆包耳机，一下子少带了三副。

<img src="/images/posts/toolkit-update-september-2026/airpods.webp" alt="AirPods 5" style="width: 367px; max-width: 100%; margin: 1rem auto;" />

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>AirPods 5</em>
</div>

### 重回索尼大法：PS5 Slim

这个不在我的工具包里，但游戏始终占据着生活中比较重要的一部分，顺带写一写这个大的硬件变更。

用了两年的 PC + Steam Deck 组合之后，7 月份我又回到了索尼的 PS。主要图个开箱即用，也能勉强带出门。掌机运行起 3A 大作的画面实在堪以入目，PC 又太需要折腾，不想把时间花在这些事情上。

最近自驾，也带上了 PS5 Slim（轻薄的那款），连同便携显示器，一起收纳在一个专用小包里，大概相当于车子后备箱增加一个额外电脑背包的空间占用。

![收纳箱：PS5 + 手柄 + 光盘 + 便携显示器（这里无广）](/images/posts/toolkit-update-september-2026/ps5-travel-case.webp)

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>收纳箱：PS5 + 手柄 + 光盘 + 便携显示器（这里无广）</em>
</div>

![在酒店玩 PS5](/images/posts/toolkit-update-september-2026/ps5-in-hotel.webp)

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>在酒店玩 PS5</em>
</div>

### 咖啡随行杯：Black blum

从云南自驾回来之后，已经是每天一杯自制冰美式的习惯了，喝水的习惯变更也一定会带上喝水装备的变更，我开始寻找适合的随行保冷杯。

由于只喝冰美式，大的敞口就非常重要，方便放冰块。为了带出门，又需要极好的密封性。容量还得至少有 600 mL，不想还没有啄两口就没有了。没想到，这几个条件组合下来，符合要求的杯子并不多，有点像是不可能三角。

最终淘到了这个很小众的英国品牌的水杯，现在的喝水日常是，一杯冰美式，加两到三杯冰水，满足一天的饮水量。

<img src="/images/posts/toolkit-update-september-2026/coffee-travel-cup.webp" alt="咖啡随行杯" style="width: 290px; max-width: 100%; margin: 1rem auto;" />

### 小米磁吸音箱

买音箱对于我来说，几乎和买水杯一样频繁了，也是因为常听播客。

看重的是它的便携：很小，差不多一个鸡蛋大小，还可以通过磁吸吸附在手机背面，作为支架。这样在使用时就和手机融为一体了，不需要单独花一份精力照看它。最近用得最多的两个场景是骑行和居家，居家主要是伴随，吃饭、洗漱、干家务，都可以拿出来吸附在手机背面，它会自动开机，然后，享受一段有声播客的伴随时光。

<img src="/images/posts/toolkit-update-september-2026/xiaomi-magnetic-speaker.webp" alt="小米磁吸音箱" style="width: 497px; max-width: 100%; margin: 1rem auto;" />

以上就是这次工具包的全部变更了，不定期分享一下。

也附上一张无关的照片，是此次九月底自驾到湖北秭归的骑行，眺望三峡大坝。自驾开始的时候，这篇文章正好开了个头，写完时，差不多国庆节就要结束了。

![秭归骑行时眺望三峡大坝](/images/posts/toolkit-update-september-2026/zigui-cycling.webp)

![眺望三峡大坝](/images/posts/toolkit-update-september-2026/three-gorges-dam.webp)
