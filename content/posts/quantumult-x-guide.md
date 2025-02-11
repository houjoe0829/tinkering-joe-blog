---
title: '最简约的科学上网方案：Quantumlt X'
date: 2024-06-27
draft: false
description: "一个简单但完整的 Quantumult X 使用指南，从购买到配置的全过程详解。"
tags: ["折腾软硬件", "软件推荐"]
author: "Joe"
---

> ⚠️ 注意：
> - 这个方案更适合已经了解基本科学上网的人，写得比较简略
> - 此方案仅适配苹果系设备，不支持 Windows、Android
> - 科学上网 = 代理软件（QuantumultX） + 海外线路
> - 最强保险是，买两家线路，更抗风险

![Mac 界面效果](/images/posts/quantumult-x/image1.png)

## 为什么推荐 Quantumult X

- Quantumult X 只需要购买一次，7.99刀，即可在 Apple 苹果系设备上使用
- 是买断制，不需要订阅
- 支持 `Mac`、`iPhone`、`iPad`、`Apple TV` 等苹果全系设备
- 好看，也算吧，不过，这个比较个人倾向
- 配置全平台通用，节点线路资源和代理规则可分开管理，很方便添加多家机场节点
- 稳定性很好，我使用过的中间，QuantumltX > Stash > Shadowrocket
- 网络活动抓包很容易看懂，而且可以根据网络自己再添加不同的规则

[‎Quantumult X 官方下载链接](https://apps.apple.com/ca/app/quantumult-x/id1443988620)

## 如何购买 Quantumult X

- 需要国外的 Apple ID 才可以下载这个代理工具
- 如果没有的话，万能的淘宝，最优解
    - 尽量选择那种已经购买 QuantumultX 的账号，或者买了海外 ID 之后，再找商家充值来购买

## 关于机场服务推荐

软件只是代理工具，真正使用还搭配线路。

最强保险当然是买两家线路，或者一家机场，但有很多地区的线路节点，分摊风险。

- 稳定且速度快的一家 [https://agneo.co/?rc=epng2diu](https://agneo.co/?rc=epng2diu)
- 性价比较高的一家 [https://renzhe.cloud/auth/register?code=ciDE](https://renzhe.cloud/auth/register?code=ciDE)
    - 不过，这一家需要自己国外 IP 才可以访问购买，国内无法直接访问
- 整体而言，一般建议买一个月试一试，亲身体验一下，以上两家我都用了三年以上，网上也有其他的很多，可以都找一找。

## 最佳 Quantumlt X 配置

- **如果嫌麻烦，一般购买的机场线路服务里有配置导入，也可以直接导入即可使用**
- 不嫌麻烦的话，可以用我的配置文件来修改，都是经验累积，适应性更好，配置文件已经放在下面
- 在样例中，已经尽可能去掉多余的规则，尤其是去广告，规则越复杂，越难 Debug
- 支持所有节点的自动测速，也支持手动选择特定节点
- 支持为 AI 工具设置单独的策略，包括 ChatGPT、Claude、Gemini
- 支持聚合多家机场服务商的节点，并按照地区分组
- 已经为 Spotify 设置单独的线路，一般比较忌讳香港线路，需留意
- 已经为 Slack 设置单独的线路，可以单独选择线路
- Apple 与 iCloud 相关按照 Direct 来处理

> ⬇️ 配置文件样例

![配置示例](/images/posts/quantumult-x/image2.webp)

[配置文件下载](/conf/quantumult_20240722182237.conf)

- 如截图，在配置文件里的 [server_remote] 模块，替换为自己的机场链接，链接需选择机场提供的的 "QuantumltX 订阅链接"
- 替换之后，机场链接前的 # 符号去掉，替换几个机场就去掉几个
- 可以添加多个机场，模板里是两个，可以自己复制并粘贴

## 注意事项

- 记得在 QuantumltX 设置里修改模式为规则分流，默认的情况下是全部走代理
    
![设置界面](/images/posts/quantumult-x/image3.png)
    
- 没有一劳永逸的办法，这个也只能减少折腾
- 添加新的机场链接之后，到设置-节点资源-全部更新一下，不然不会生效

## 遇到过的问题

### （1）打开 QuantumultX 之后无法使用手机的投屏

只需要在"设置-其他设置-VPN"打开"兼容性增强"即可。

### （2）需要定期打开 QuantumltX

似乎在后台无法及时更新，如果遇到网络不正常，打开一次等它更新即可。

## 继续补充中 