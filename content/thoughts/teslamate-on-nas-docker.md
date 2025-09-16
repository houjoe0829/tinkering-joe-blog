---
author: "Joe"
date: 2025-09-16
description: "Teslamate 迁移到 NAS Docker 后的部署体验，继续利用自动化保持日历记录同步。"
draft: false
tags: ["折腾软硬件"]
title: ""
---

已经把 Teslamate 完整搬到了 Nas 的 Docker 上。

基于之前 [让特斯拉行程无缝接入日历](/posts/tesla-calendar-integration-automation) 的已有实现，这次搬到 Nas 上之后，VPS 的费用就省掉了，完全本地化运行，并且，依然可以在日历里看到车辆的行驶记录（模糊化后的数据），作为精准的日程事件，一览无余。

这个过程依然是 Codex 先写一版初始的代码，然后 Cursor 里的 Claude 4 Sonnet 来微调。
