---
author: "Joe"
date: 2025-04-18
description: "介绍如何在 Notion 中设置和使用 Daily Note 功能，通过自动化实现每日笔记的创建和管理"
draft: false
tags: ["折腾软硬件"]
title: "三步为 Notion 开启 Daily Note 功能"
---

最近的笔记工作流非常依赖 Daily note，常见的用途和大家一样，方便随心所欲记一些不成形的想法和资料，如果有精力，再通过标签或者双向链接来完成聚合归类，甚至懒的话，我也会放弃归类，只是将 Daily note 作为当天的草稿箱，完成无压力的记录，这样不用在记录的时候就想着归类，减轻心智负担。

不过，我还有一个用途，每天会在 Daily note 里写一些和当天相关的安排备忘，最关键的是，今天最重要的三件事，以及一些和安排相关的事宜，比如已经定好的中午吃什么的安排，写几个字备注一下，减少让人分心的重复性决策。

最近使用了各种笔记工具，比如 Logseq、Obsidian、Craft，都有自己官方支持的 Daily note 功能，但是 Notion 一直都没有，不过，我发现，Notion 也可以很变相实现，并且完全自动化。

## 第一步：新建 Database

可以先在任意页面新建一个 Database，命名为 Daily Note，更建议加个图标，图标本身比文字名称更具辨识度。

![创建 Daily Note 数据库](/images/posts/notion-daily-note-setup-guide/create-database.webp)

## 第二步：设置 Database 自动化

入口在这个位置

![自动化菜单入口](/images/posts/notion-daily-note-setup-guide/automation-menu.webp)

点击之后，选择"New automation"，然后做以下设置就可以了，每天 0 点会自动创建新的以当天日期命名的 Page。

- When（触发器）设置为：Every Day
- Do（操作）设置为将名称设置为日期，其实这里是通过 @ 选择 Data triggered

![自动化设置](/images/posts/notion-daily-note-setup-guide/automation-settings.webp)

## 第三步：将 Daily Note 放在主页（Home）

这一步不是非必需，你也可以将 Daily Note 以收藏的方式放在最上面，只不过，放在主页看上去更顺畅一些。

首先，在 Home 里先开启 Database Views 的 Widgets（组件）

![启用 Widgets](/images/posts/notion-daily-note-setup-guide/enable-widgets.webp)

其次，在 Database Views 里选择数据库源（Source）

![选择数据库源](/images/posts/notion-daily-note-setup-guide/select-database.webp)

## 一些使用 tips：

- 在 Daily Note 里，可以使用 @now 来插入当前的时间，适合碎片记录的标记。
- 很多人习惯用 Tag 来做碎片内容的归类，在 Notion 里，直接用双向链接即可，为每一个主题新建同名 Page，每次归类的时候 @ 并关联即可。 