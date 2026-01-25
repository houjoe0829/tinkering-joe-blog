---
title: "被灰度到 Notion Custom Agent 了"
date: 2026-01-26
draft: false
description: "Notion Custom Agent 灰度体验,定时更新日志和自定义助手的实践"
tags: ["AI 相关"]
author: "Joe"
---


不知道是不是因为我最近主动搜寻了一下 Notion Custom Agent, 并访问了官方的文档，第二天就被灰度到了。

现在我自己几乎每天重度使用 Notion AI, 之前的 [用 AI 写什么，不写什么](/posts/what-to-write-with-ai-and-what-not) 有提到更具体的场景和缘由。它最大的优势还是上下文本身，历史存量内容在这里，增量内容也在，可以自由引用。

只是，Notion AI 本身还是略显呆板，虽然可以自由定义 AI 的人设，但是一次只能一个，也缺少可复用的快捷指令，灵活度较差。

Custom Agent 有点类似于 Subagent 的概念设定，可以预设单独的人设、权限、上下文、选定的大模型，以及最重要的触发方式，比如:

- 直接与它对话
- 在对话里提及，灰度阶段好像还无法 @
- 定时执行
- 与 Notion 更新相关的操作
- 与 Slack 相关的操作

![Notion Custom Agent 触发方式配置界面](/images/posts/notion-custom-agent-experience/CleanShot_2026-01-25_at_2353572x.webp)

## 目前，我有两个使用的场景。

### 一个是，定时 Custom Agent

不是所有的上下文都是在 Notion 里产生的，比如产品的更新日志，往往是基于代码的变更，在代码仓库里维护，并更新在产品的官网上。于是，我设置了一个定时的 Custom Agent, 每天去检查一下官网的更新，一旦有新的内容，自动整理到对应的更新日志 Database 里，这样就有了最新的产品更新上下文。

![定时 Custom Agent 每日同步产品更新日志](/images/posts/notion-custom-agent-experience/CleanShot_2026-01-26_at_0005152x.webp)

### 另一个是，特定 AI 助手

这个比较常见，比如我的 Roam FM 用户回复助手，只是一些简单的回复约定。但这个回复的精准度其实依赖于第一个场景里的上下文更新，尽管我的产品方案、想法都在 Notion 里，但最及时的变更是在代码里，两者不在一个环境里。

而一旦有了这个上下文，AI 在拟定用户回复的时候，可以知道最准确的版本变更信息。

![Roam FM 用户回复助手配置](/images/posts/notion-custom-agent-experience/CleanShot_2026-01-26_at_0006382x.webp)

## 如何创建 Custom Agent?

Notion AI 并不是直接让你去填表或者写个长长的文档，而是可以用 AI 创建 AI, 基于自然语言对话就可以实现，还能持续修正。

最大的难度还是对自己的灵魂追问，我有什么规则值得沉淀下来呢？

![通过 AI 对话创建 Custom Agent](/images/posts/notion-custom-agent-experience/e65057d2-e9d5-4896-9345-f1d58f31ba95.webp)

## 不完善的地方

- 移动端还无法访问
- 无法在对话里直接提及，要不就是自动触发，要不就只能对话，这个应该很快可以解决吧

不过，Custom Agent 还是太重了。它适合定义一个完整的「Bot」, 却难以像 Skills 或 Commands 那样，作为一个具体的「动作」被灵活穿插在日常工作流中。
