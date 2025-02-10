---
title: '性价比最高的科学上网方案：Shadowrocket'
date: 2024-11-12
draft: false
description: "一个简单但完整的 Shadowrocket 使用指南，从购买到配置的全过程详解。"
tags: ["折腾软硬件", "软件推荐"]
author: "Joe"
---

> ⚠️ 注意：
> - 如果不知道怎么改规则，让 AI 改，很靠谱的
> - 这个方案更适合已经了解基本科学上网的人，写得比较简略
> - 此方案仅适配苹果系设备，不支持 Windows、Android
> - 科学上网 = 代理软件（Shadowrocket）+ 海外线路
> - 最强保险依然是，买两家线路，更抗风险，当然，越多越好
> - 有 QuantumltX 的可以看 [最简约的科学上网方案：Quantumlt X](https://www.notion.so/Quantumlt-X-d0d663d0c40b4b7391d7b76b410b1331?pvs=21)

![Mac 界面效果](/images/posts/shadowrocket/image1.png)

## 为什么推荐 Shadowrocket

- 只需要购买一次，2.99刀（超便宜），即可在 Apple 苹果系设备上使用
- 是买断制，不需要订阅
- 支持 `Mac`、`iPhone`、`iPad`、`Apple TV` 等苹果全系设备
    - Mac 就是个 iPad 版本，但是关闭窗口，仍然可以运行在后台
- 配置全平台通用，节点线路资源和代理规则可分开管理，很方便添加多家机场节点
- 网络活动抓包很容易看懂，而且可以根据网络自己再添加不同的规则，比 QuantumultX 其实更简单

[‎Shadowrocket 官方下载链接](https://apps.apple.com/hk/app/shadowrocket/id932747118)

## 如何购买 Shadowrocket

- 需要国外的 Apple ID 才可以下载这个代理工具
- 如果没有的话，万能的淘宝吧
    - 另外也可以在 Google 搜索，我感觉最近淘宝封锁的厉害，很难找到

## 关于机场服务推荐

软件只是代理工具，真正使用还搭配线路。

最强保险当然是买两家线路，或者一家机场，但有很多地区的线路节点，分摊风险。

- 稳定且速度快的一家 [https://agneo.co/?rc=epng2diu](https://agneo.co/?rc=epng2diu)
- 性价比较高的一家 [https://renzhe.cloud/auth/register?code=ciDE](https://renzhe.cloud/auth/register?code=ciDE)
    - 不过，这一家需要自己国外 IP 才可以访问购买，国内无法直接访问
- 整体而言，一般建议买一个月试一试，亲身体验一下，以上两家我都用了三年以上，网上也有其他的很多，可以都找一找。

## 一步一步配置 Shadowrocket

> 💡 一句话就是：添加节点订阅 + 节点分组 + 配置文件

### （1）添加节点订阅

一般各大机场都会针对 Shadowrocket 出单独的订阅链接，比如我上面提到的两家都有，登录至直接导入到 Shadowrocket 就可以的。

![添加订阅](/images/posts/shadowrocket/image2.png)

### （2）导入配置

> ⚠️ 导入配置之后记得选择使用该配置哦，我分享了两个配置。**关于如何下载，打开 conf 文件之后会在浏览器的 Tab 里打开，右单击打开的内容，选择"存储为"即可。**

[这是一个非常简单的配置](/conf/minimal_rules_by_jojo.conf)

[这个有更多的分组，但是也没有带广告](/conf/modified_by_jojo_2025-01-18.conf)

网上有超级多 Shadowrocket 的配置分享，我自己也分享我自己的，风格还是一如既往：

- 整体规则用 Claude AI 来生成
- 尽可能简化规则，不必要的都删除掉，越简单越能减少网络玄学问题
- 为节点按地区分区，这很重要，这样方便特定网址走特定地区，比如 Spotify、AI 等
- 每个地区分组自动测速
- 为 AI 单独增加策略组，已经添加了 ChatGPT、Claude、Gemini 等 AI
- 为 Social Channel 增加了策略组
- 为海外视频会议单独设置了策略组
- Apple、微软也增加了单独的策略组，均 Direct

### （3）节点分组

这里主要是设定一个全局测速的自动节点，针对所有可用的节点，可以汇总多家机场。

![节点分组](/images/posts/shadowrocket/image3.png)

在首页-全局路由-分组里，开启简单模式，增加分组之后，如果不改或者空着就会默认选中所有的节点，这里建议加上筛选，因为机场有些节点是不可用的，容易干扰，尤其是那些用来显示流量的。

筛选的正则表达式是这样的即可，主要排除一些无效节点（这个真的很重要哦）。

```json
^(?!.*(流量|套餐|当前网址|海外用户)).*
```

![筛选设置](/images/posts/shadowrocket/image4.png)

### （4）一些零碎设置

- 在全局路由里，一定要将代理设置为"按配置"，不然很容易全局代理
- 建议开启日志，这样代理有问题的时候，可以基于日志增删规则，在"数据-日志-代理"
- 建议开启 iCloud 同步，在"数据-iCloud"
- 建议开启自动更新，在"设置-更新-配置"里，但记得关闭提醒
- 建议开启订阅更新，在"设置-更新-订阅"里，开启打开时更新和自动后台更新 