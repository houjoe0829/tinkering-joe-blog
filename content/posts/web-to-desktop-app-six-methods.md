---
title: "将网页变成桌面应用的6种方式"
date: 2025-01-19
draft: false
description: "介绍6种将网页工具转换为桌面应用的方法，包括Chrome快捷方式、MenubarX、Slidepad等，以及推荐的网页工具清单。"
tags: ["折腾软硬件"]
author: "Joe"
---

过去的几个月，尝试过各种将网页变成桌面应用的方式。

不得不说，越来越多的工具，其 Web 端已经做得极其完善，甚至直接是 Web 起家。比如 flomo、Notion、Todoist 等众多工具。

可能是讨厌在众多浏览器标签中寻找对应的标签，也可能是频繁切换让人烦躁，抑或是在一台电脑上许多应用其实不值得为其安装一个客户端，而遭受大家吐槽的 Electron 套壳方式（比如 Notion）确实占地面积愈来愈大，且被越来越多的网页应用所使用。

## 先附上6种方式的对比

| 方式 | 特点 | 平台支持 |
|------|------|----------|
| **Chrome 快捷方式** | 创建桌面应用，完全免费 | Windows、Mac |
| **MenubarX** | 创建顶栏应用，可随时调用 | 仅 Mac，在 Setapp |
| **Slidepad** | 创建快捷窗口应用，快捷键唤出 | 仅 Mac，在 Setapp |
| **Vivaldi 浏览器** | 将网页添加到浏览器侧边栏 | Windows、Mac |
| **Unite 4** | 将任意网站变成桌面或者顶栏应用 | 仅 Mac |
| **Station** | All in one 的网页应用集合 | Windows、Mac、Linux |

## 1. Chrome 创建桌面应用

可能很多人不知道，Chrome 本身就自带这个功能，可以一键将任意网页创建为桌面应用，完全免费。

![Chrome创建桌面应用步骤1](/images/posts/web-to-desktop-app-six-methods/chrome-create-app-1.webp)

![Chrome创建桌面应用步骤2](/images/posts/web-to-desktop-app-six-methods/chrome-create-app-2.webp)

这里一定要勾选「在窗口中打开」，否则和一般的书签就没有啥区别了。

其实 Chrome 桌面应用最大的好处是，创建之后，其他浏览器的插件仍然可适用，比如如果创建了 Notion 桌面应用的话，就可以试试很多第三方 Notion 的插件，比官方客户端更强大。比如 [Notion-enhancer](https://chrome.google.com/webstore/detail/notion-enhancer/dndcmiicjbkfcbpjincpefjkagflbbnl?utm_campaign=en&utm_source=en-et-na-us-oc-webstrhm&utm_medium=et)

## 2. MenubarX 创建顶栏应用

[MenubarX - A powerful Mac menu bar browser](https://menubarx.app/)

![MenubarX应用界面](/images/posts/web-to-desktop-app-six-methods/menubarx-interface.webp)

这是一款国内独立开发者的产品，也是目前唯一还在持续使用的方式，主要是顶栏应用有入口上的优势，支持多种 UA 的调整（可选电脑、手机或者平板）也支持了自定义尺寸，适合很多小应用，比如 DeepL、Twitter 等，支持买断。

另外，建议配合一款免费的 Mac 顶栏管理工具使用，效果更佳：[Hidden Bar](https://github.com/dwarvesf/hidden)

## 3. Slidepad 创建快捷窗口应用

[Slidepad - A Slide Over browser on your Mac](https://slidepad.app/)

Slidepad 主要是可以生成一个可随时唤出的快捷窗口，非常适合一些快速笔记、快速任务录入等场景，支持快捷键或者鼠标移动到屏幕指定位置快速唤出，即用即消失。

![Slidepad快捷窗口](/images/posts/web-to-desktop-app-six-methods/slidepad-window.webp)

## 4. Vivaldi 浏览器 创建侧边栏应用

[Vivaldi | 快速且私密的浏览器，更有独特功能加持](https://vivaldi.com/zh-hans/)

在很久之前的文章里特别推荐过 Vivaldi 浏览器，这是一款自定义程度极高的 Chrome 内核浏览器，不过，近期这款浏览器还将 RSS、邮件、日历等功能加入了进来，越来越臃肿，反而不太喜欢了，不过，还好，都可以自由关闭。

Vivaldi 浏览器最显著的特点之一就是可自由添加网页的侧边栏（Panel），可以在浏览器的左侧或者右侧打开一个侧边栏，只能是移动端视图（也就是手机模式），可以与已有标签页并存，小的缺点是，由于只能是移动端网页，部分网页工具在 PC 上查看和操作时有一些小问题，比如 Notion、Workflowy 等网页工具的编辑。

[Web Panels | Vivaldi Browser Help](https://help.vivaldi.com/desktop/panels/web-panels/) - 官方功能简介和说明

![Vivaldi侧边栏控制](/images/posts/web-to-desktop-app-six-methods/vivaldi-web-panel.webp)

## 5. Unite 4 创建桌面应用或者顶栏应用

[Unite for macOS](https://www.bzgapps.com/unite)

既可以创建桌面应用，也可以创建顶栏应用的工具，唯一的缺点是，稍微有点贵，不过，已经加入了 [Setapp](https://setapp.com/)。

![Unite桌面应用模式](/images/posts/web-to-desktop-app-six-methods/unite-desktop-mode.webp)

桌面应用模式

![Unite顶栏应用模式](/images/posts/web-to-desktop-app-six-methods/unite-menubar-mode.webp)

顶栏应用模式

## 6. Station 创建桌面应用集合

[Station • One app to rule them all](https://getstation.com/)

Station 可以理解为一个特别定制的多标签浏览器，针对网页应用做了一定程度的优化，可以很方便在很多个网页应用之间切换，缺点就是，性能一直是一个问题，而且，如果添加的网页应用过多，感觉和浏览器没有什么差别。

![Station界面](/images/posts/web-to-desktop-app-six-methods/station-interface.webp)

## 有哪些推荐的网页工具？

不是所有网页工具都适合转换为桌面应用，只有那些需要频繁需要访问的网页工具才适合转换成某种形式的桌面级应用。比如，对于我自己，可能一个月偶尔才用一次的在线图片压缩工具，只适合放在浏览器书签里，而常用的翻译工具 DeepL 就适合放在顶栏。

以下是放在收藏夹的小工具，网页版非常好用，而且完全够用：

| 工具名称 | 链接 |
|---------|------|
| DeepL 超强网页翻译工具 | https://www.deepl.com/translator |
| Google 翻译 | https://translate.google.com/ |
| YouTube 视频下载工具 | https://zh.savefrom.net/142/ |
| 在线图片压缩工具 | https://squoosh.app/ |
| Notion 笔记工具 | https://www.notion.so/ |
| flomo 卡片笔记 | https://flomoapp.com/ |
| Telegram 网页版 | https://telegram.org/ |
| Inoreader RSS 订阅工具 | https://www.inoreader.com/ |
| Gitmind 在线思维导图 | https://gitmind.com/ |
| 滴答清单网页版 | https://dida365.com/ |
| 全球在线电台 | http://radio.garden/ |
| 法律查询工具 | https://www.justlaws.cn/ |
| 移除网页付费阅读的工具 | https://www.removepaywall.com/ | 