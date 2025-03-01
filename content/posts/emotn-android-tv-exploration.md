---
author: "Joe"
date: 2021-11-24
description: "探索 Emotn 这款免费无广告的 Android TV 应用商店，以及如何在国产安卓电视上安装和使用各种流媒体应用"
draft: false
tags: ["折腾软硬件"]
title: "由 Emotn 开始的国产安卓电视折腾日记"
---

![Emotn 商店效果图](/images/posts/emotn-android-tv-exploration/emotn-store.webp)

目录 ⬇️

## Emotn 是什么？

一个免费无广告的 Android TV 应用商店，并且可以在不需要安卓电视有谷歌框架的情况下安装 YouTube、Netflix 等，打开这个应用商店有一种之前在小米盒子国际版里打开正规 Google Play Store 的错觉，激起了我折腾电视的想法。

[Emotn Store 官方下载地址](https://app.emotn.com/)

> 💡 Emotn 支持上传自己的 APK 应用安装包，在电视上无需账户，通过一个叫做分享码的方式来传输和安装，非常方便

## 安装 Emotn 非常简单

下载 APK 安装包到 U 盘，然后接入电视来安装，由于我的坚果投影仪自带的文件管理器不识别非视频、图片的文件，这个过程还下载了一个 ES 文件浏览器来打开 U 盘里的安装包，好在坚果没有什么未知应用安装的限制，直接安装成功了。

[ES 文件浏览器官网](http://www.estrongs.com/)

## 我安装了那些应用

### 先上 YouTube

我和我老婆已经非常习惯在 YouTube 上订阅并观看视频，之前是用 Xbox 来安装并通过 HDMI 来连接播放。Xbox 基本不用担心，正规设备。

在国产电视上安装，会有很多奇奇怪怪的小问题，比如这次下载了 YouTube TV 版本，结果，始终无法登录，点击即闪退，最后换成了据说是俄罗斯小伙开发的 Smart YouTube TV，成功了，而且还可以免广告，不过，我是 YouTube Premium，无法验证。

[Smart YouTube TV 主页](https://smartyoutubetv.github.io/)

### Netflix 失败了

Netflix 对设备要求很高，只有经过验证的设备才能安装最通用的 Netflix TV 版本，国产电视基本不可能，推荐安装 Emotn 里那个叫做 Netflix for Pad 的版本，不过，我的电视遥控器适配不是很好，有些小瑕疵，比如无法通过遥控器来播放指定集数，一怒之下，卸载了。

> 更新（2021 年 12 月 7 日）：没有更好的选择，为了可以看 Netflix，还是用了 Netflix for Pad 的版本。

### 虎牙 TV 3.12.1 版本

这是我一直收藏的版本，新版的虎牙 TV 去掉了非常多的资源，只有这个版本及更早之前的版本才是完整的，保留着，避免以后丢了。

![虎牙 TV 版停止运营通知](/images/posts/emotn-android-tv-exploration/huya-tv-notice.webp)

> 更新（2021 年 12 月 4 日）：虎牙 TV 版停止运营了

### 哔哩哔哩视频 1.6.2 版本

与虎牙 TV 一样，也是只有特定版本才是完整的资源。

### 全能型播放器 Kodi

可惜，我的坚果投影仪无法正常运行 Kodi 新版，它的强大，无以伦比，我甚至已经为它建好了一个专门的 Page 来挖掘一下，只能等坚果升级一下其系统再试试，NND。

[Kodi 官网](https://kodi.tv/)

推荐观看以下 YouTube 视频来了解 Kodi：
- [KODI 是什么？KODI 能做什么？这期做个介绍，随便辟辟谣。](https://www.youtube.com/watch?v=XEHoepm-ivg)
- [【KODI 应该这么玩】](https://www.youtube.com/playlist?list=PLTI5d7Gwez7pdJ_S-AV1tDrFFdwRly_e4)

![Kodi 界面预览](/images/posts/emotn-android-tv-exploration/kodi-interface.webp)

### 全球 6000 多 TV 直播源

先通过 Emotn 安装了一个叫做 IPTV 的流媒体客户端，然后添加了 GitHub 大神维护的直播源地址，超多 TV 直播源都可以看到，还可以收藏，一下子感觉国产电视国际化了。

以下为直播源 GitHub 地址，有教程和工具：
[https://github.com/imDazui/Tvlist-awesome-m3u-m3u8](https://github.com/imDazui/Tvlist-awesome-m3u-m3u8)

## 最后：关于科学上网

我的科学上网是一台 R2S 的软路由（OpenWRT）+ ShadowSockR Plus 插件来完成的，配合小米路由器，主要是方便家里所有电脑、手机、主机、电视盒子翻墙，这个说起来比较麻烦，我贴一下我参考的教程，需要自个研究一下，有机会再单写一次。

推荐观看以下 YouTube 视频来了解软路由：
- [划重点！入手软路由前你必须要了解的事情！！！](https://www.youtube.com/watch?v=NwJtD_JBfeI)
- [揭秘 openwrt 三大神器！clash ssrplus passwall 速度测试！软路由 openwrt lede 科学上网插件](https://www.youtube.com/watch?v=jwd7wvqcDYY)

科学上网线路服务商是 AgentNEO，能看 Netflix，稳定，链接：[https://agneo.co/?rc=epng2diu](https://agneo.co/?rc=epng2diu)