---
author: "Joe"
date: 2025-08-17
description: "通过 Teslamate 和自动化脚本，将特斯拉行程数据无缝同步到日历应用中，实现行程记录的可视化管理"
draft: false
tags: ["折腾软硬件"]
title: "让特斯拉行程无缝接入日历"
---

我自己有种执念，希望生活中占据一整块的事项都能显示在日历里，记录已发生的行程，和展示即将出现的安排，有一种一览无余的掌控感。这样可以知晓，以前的某一天做了啥，接下来的哪一天有什么的安排。

这次花了两小时搭建的电子玩具，就始于我想让开车的记录显示在日历里，它代表了一天里精准的行程，有时间起止，也有位置变动。

而日历，其实有一种大家都认可的通用 iCal 格式，理论上所有能获取到的时间数据，都可以转换为这种可订阅的日历格式，并在各种日历 App 中订阅查看。

在这之前，我的日历上已经有了滴答清单的待办和专注时间、携程的火车票行程、航旅纵横的机票旅程、预约的腾讯会议、企业微信的日程、飞书的会议，以及户外的运动记录，这些都是各种平台预制好的订阅日历，正好 All in one。

而和很多特斯拉车主一样，从买车不久，我就听说了特斯拉的数据记录神器：Teslamate。一个可以私有化部署的实时读取并存储特斯拉车辆数据的记录器，支持以图表和地图来展示各种行驶概况，好看炫酷，但谁会没事登录去看看呢，这也成了之前折腾的最大阻力，预估，弄完即落灰。

![Teslamate-Overview.webp](/images/posts/tesla-calendar-integration-automation/Teslamate-Overview.webp)

不过，数据记录 + 日历展示，应该有搞头！

只需要借助 Teslamate 获取行驶数据，再将行程变为发生的日程，自动同步到日历里，这个数据就真的有用起来了，因为，日历是每天都会查看的，当然，主要是针对我个人。如之前所说，可以精准知晓某一天，什么时间段，从什么地方开往什么地方，当时的温度，消耗的续航里程，而这一切，一旦部署，完全自动化，创建的日程还分秒不差，准确反映现实。

![CleanShot 2025-08-17 at 14.26.44@2x.jpg](/images/posts/tesla-calendar-integration-automation/CleanShot%202025-08-17%20at%2014.26.44@2x.webp)

整套自动化大概的实现方式是：在 VPS（虚拟服务器）上部署 Teslamate 获取车机数据，再用 Python 脚本将数据转换为需要的日程信息，最后在 VPS 上构建出带有密码验证的 iCal 日历订阅链接即可。

<img src="/images/posts/tesla-calendar-integration-automation/CleanShot_2025-08-17_at_13.51.192x.webp" alt="CleanShot 2025-08-17 at 13.51.19@2x.jpg" style="width: 60%; max-width: 600px; height: auto; display: block; margin: 0 auto;" />

我没有任何代码读写能力，全部是借助 Cursor 远程连接一台 VPS（虚拟服务器），完成了代码编写，可以理解为，口述需求，让 AI 在终端部署和修改。而且，就连远程连接服务器本身，我都是让 AI 帮忙操作的。

如果你考虑尝试，再分享一些实施过程中的细节：

- 需要一台至少 1GB 内存、5GB 存储的虚拟服务器，Ultr 上大概最低 5 美元每月，可以用我的邀请码 [https://www.vultr.com/?ref=9794227-9J](https://www.vultr.com/?ref=9794227-9J)
- 重要的模块包括，Teslamate 数据获取和存储、Nginx 设置密码访问、清洗数据的 Python 脚本和生成可被日历接受的 iCal 文件服务。
- 也可以用上 Cloudflare 的免费 SSL 让订阅更顺畅，需要在 Cloudflare 域名，不过，没有也行，只是在订阅的时候会有安全提醒，不阻塞使用。
- Teslamate 授权访问你的车辆是需要两个 Token 的，一个是访问 Token，另一个是刷新 Token，这个有非常多的免费工具可以实现，比如 Auth for Tesla。

一旦服务来运作，你在特斯拉车机窗口顶部会不定时看到一个提示第三方应用程序在访问的小图标，点开可以看到详情，长下面这样，不过，不留意可能不会察觉。

![CleanShot 2025-08-17 at 13.58.57@2x.jpg](/images/posts/tesla-calendar-integration-automation/CleanShot_2025-08-17_at_13.58.572x.webp)

等我弄完，又发现，原来我的 Nas 支持构建容器，也就是说，我可以在 Nas 上部署整套服务，而且完全免费运行。很快，需求已经和 AI 一起写好了，等哪天再折腾一轮吧。
