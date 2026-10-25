---
author: "Joe"
date: 2026-10-25T15:58:48+08:00
description: "开启 Chrome 的两个实验选项，在切换到其他应用、窗口被遮住时，让 YouTube 视频自动进入画中画。"
draft: false
tags: ["折腾软硬件"]
title: "如何在 Chrome 里实现 YouTube 自动小窗口播放"
---
想在 Mac 上实现一个小功能：在 Chrome 浏览器里看 YouTube，切到其他窗口时，视频能自动缩成小窗，在屏幕右下角继续播放。
我知道 Chrome 本身有这个插件，但需要每次手动开启一下。
另外，我也知道还有一个叫 Pip 的第三方插件，可以实现自动开启，但有限定条件，需要先切换到其他标签页才行，细思一下，这不就约等于手动了嚒……
而我自己的日常是，经常在 Mac 上不同窗口间切换，尤其是与 Agent 人机协作的时候，适合边看视频边等 Agent 输出。
网上搜罗了一番，没想到，Chrome 自己就有，只是藏在实验设置里。
可以在地址栏分别打开下面两个地址，把对应选项改成 `Enabled`，然后重启：

```text
chrome://flags/#browser-initiated-automatic-picture-in-picture
chrome://flags/#auto-picture-in-picture-on-window-occluded
```

前一个让 Chrome 主动开启画中画，后一个让它在视频窗口被其他窗口遮住时触发。
之后，正常播放有声音的视频，切到其他应用，让窗口盖住 Chrome，视频就会自己弹出来。
不过，目前的小缺陷是，打开不同的视频，小窗尺寸会重置，以及，不能显示 YouTube 字幕。
