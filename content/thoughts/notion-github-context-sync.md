---
author: "Joe"
date: 2026-03-02
description: "用 Git Hook 自动把代码仓库里的 README 和 Specs 文档同步到 Notion，让两边共享最新的项目上下文"
draft: false
tags: ["Vibe Coding"]
title: ""
---

让 Notion 和 GitHub 仓库保持上下文同步的一种方法。

首先，这个主要适用于同时使用 Notion 和 Claude Code 的场景。

我自己依然保持着文档驱动开发的习惯，也就是长期维护 README，并且针对产品的关键模块也会单独维护一个 Spec 文档，映射代码逻辑和架构，方便我以自然语言 Review。

但产品的上下文就这样分割在 Notion 和 GitHub 仓库了，毕竟无法事无巨细的把所有项目文档都塞到代码仓库里。加上，Notion 连接 GitHub 的能力，被限制在组织的代码仓库里。

这事儿太适合 AI 自己做了。

于是，最近做了一个简单的 Hook，当提交 Commit 的时候，如果发现代码仓库里的 README 以及 Specs 文档有新增或者变更，自动同步到 Notion 的对应页面里，用 Database 来维护，这样很大程度上，两边可以共享上下文，还是更新的。
