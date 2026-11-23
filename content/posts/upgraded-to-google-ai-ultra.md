---
author: "Joe"
date: 2026-11-23T12:28:28+08:00
description: "从 Claude 和 OpenAI 切到 Google AI Ultra 的体验对比、跨区付费折腾过程，以及对 AI 订阅和个人工作流的一点想法。"
draft: false
tags: ["AI 相关", "折腾软硬件"]
title: "折腾了一番 Google AI，升级到了 Ultra"
---

这两天网上对 Google 模型的「吹捧」太多了，看得出大家苦 Claude 账号久矣，终于又盼来个能顶上的。

我也是前天晚上先升级到了 Google AI Pro 试用了一下，昨天又升到了 Ultra 100 刀的套餐。

今年更早之前，基本是 Claude Opus 搞定一切，直到 10 月开始被封号，后来就换成了 OpenAI 的 Sol 模型。

6.2 Sol 发布之后，对 OpenAI 略微有些失望。作为第一梯队，主要的瑕疵没有解决，审美太差和过度设计。

下面这个网友的示例就是最好的解释：该有的都有，但是不好看；不该有的也有，纯属过度考虑。而且这么一来还有个额外问题，任务耗时总是很长，不知道它在后台做什么，一个劲地捶打，一遍又一遍。

<a href="/images/posts/upgraded-to-google-ai-ultra/astra-defensive-design-example.webp" class="post-image-zoom" target="_blank" rel="noopener"><img src="/images/posts/upgraded-to-google-ai-ultra/astra-defensive-design-example.webp" alt="X 网友 @10xmylife 的示例" style="width: 787px; max-width: 100%; margin: 1rem auto; display: block;" /></a>

<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;">
<em>X 网友 @10xmylife 的示例</em>
</div>

Google AI 的出现，尤其是 Neon 4，让我们这些毫无设计能力的人，终于又能把 AI 的产出叫做「设计」，而不只是「原型」，算是能端出来了。

不过按我自己的体感，网上这么多夸奖，很大程度是因为大家用不上 Claude。单论能力，Claude Opus 5.5 依然是目前的首选，审美在线、沟通务实、做事省心。但如果没得选，现在 Google AI 的 Neon 4 比 OpenAI 的 Sol 好用，尤其是文本表达，我觉得好过 Opus 和 Sol，还补上了 Sol 审美设计差的不足。

代价是什么呢？

Google AI 是支持中国的 Visa 卡支付的，这个让很多人能独立完成购买了，但对网络节点的要求，非常严苛，和 Claude 等同，而且账号本身也得折腾一番。

第一步是修改账号地区，先把账号迁移到美国，这个申请大概一个小时内就能生效。

<a href="/images/posts/upgraded-to-google-ai-ultra/google-region-change-confirmation.webp" class="post-image-zoom" target="_blank" rel="noopener"><img src="/images/posts/upgraded-to-google-ai-ultra/google-region-change-confirmation.webp" alt="Google 账号地区迁移确认通知" style="width: 567px; max-width: 100%; margin: 1rem auto; display: block;" /></a>

迁移完准备购买时，记得确认选对了支付账户。尤其是改过账号地区的人，名下往往会有多个 Payment profile，别选岔了。

<a href="/images/posts/upgraded-to-google-ai-ultra/google-select-payments-profile.webp" class="post-image-zoom" target="_blank" rel="noopener"><img src="/images/posts/upgraded-to-google-ai-ultra/google-select-payments-profile.webp" alt="选择 Google 支付资料" style="width: 367px; max-width: 100%; margin: 1rem auto; display: block;" /></a>

等到真正付款前，还有两件事最好提前搞定：一是把网络代理开成全局，二是完成账号验证。一般打开 [payments.google.com](https://payments.google.com/) 就会弹出验证入口。

<a href="/images/posts/upgraded-to-google-ai-ultra/google-payments-verify-identity.webp" class="post-image-zoom" target="_blank" rel="noopener"><img src="/images/posts/upgraded-to-google-ai-ultra/google-payments-verify-identity.webp" alt="Google 付款中心账号验证入口" style="width: 912px; max-width: 100%; margin: 1rem auto; display: block;" /></a>

对于付费，我看很多人趁着黑色星期五优惠，升级了年付的 Google AI Pro，其实不太建议，虽然 Google 家的套餐极为慷慨，不只是 AI 用量，还包括云盘、YouTube 等等一系列福利。但，AI 产品本来就不适合年付，变化太快了，想想半年前大家还在对 OpenAI 家 Codex 大加赞誉。而且，从 Google AI 过往的表现来看，它的能力供给一直不算稳定。

反正我的主力 AI 一直在换。组合方式倒没怎么变，选择一家第一梯队模型的大套餐（100 刀），再搭配一个多模型聚合平台的小套餐（20 刀），只不过之前是 Claude、OpenAI，现在轮到了 Google AI。我自己的那套本地 Agent 服务，也适配了各家的 CLI，把 Skill、Memory、上下文接入和历史对话呈现都做了单独解耦。

依然期待 OpenAI 的下一个模型，但还是那句话，尽量减少对单一模型的依赖，核心是构建一套属于自己的稳定交付工作流。
