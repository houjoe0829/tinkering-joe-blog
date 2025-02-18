---
title: "最好的本地 AI 笔记软件：Obsidian + Cursor"
date: 2025-02-18
draft: false
description: "探索如何将 Obsidian 和 Cursor 结合使用，打造一个真正本地优先的 AI 笔记解决方案"
tags: ["折腾软硬件", "AI"]
author: "Joe"
---

看到[歸藏老师](https://x.com/op7418/status/1891827233423012308)在 Twitter 上提到了这个，真的是与最近的使用感受非常类似。

![Twitter 截图](/images/posts/best-local-ai-note-taking-tools/twitter-screenshot.webp)

我自己最近除了将个人博客从 Notion 搬到了个人站点 houjoe.me，也将日常笔记从 Notion 迁到了 Obsidian，主要是用 Cursor 这类 AI 编程工具多了之后，Coding with AI 的正反馈让我也更希望 Note-Taking with AI。

其实，一般代码仓库里都有一个最大的"笔记"，README.md，可以理解为一个方便快速上手代码仓库的 Markdown 备忘录。

而且，近期为了让 AI 能够精准且充分理解需求上下文，我在另一个实验性产品的代码仓库里，直接新建了 Docs 文件夹，然后将 PRD 以 Markdown 文件的形式放在里面，这样就可以更愉快地让 AI 精细化干活了。

## 为什么选择 Obsidian？

如上面提到的，因为代码编辑工具认 Markdown 格式的文件。所以，理论上以 Markdown 来存储内容的 Logseq 也是可以的，但是它的 Markdown 会加很多额外的格式。一番对比下来，Obsidian 的 Markdown 会接近代码里的格式规范一些。

## 如何让 Cursor 与 Obsidian 协作

使用 Obsidian 之后，会有一个 Vault 文件夹，可以理解为数据库文件夹，Obsidian 所有笔记数据都以 Markdown 形式存储在里面，这个时候只需要用 Cursor 或者其他 AI 编程工具打开这个文件夹就可以开始了。

别忘了，字节的 AI 编程工具 Trae 还免费呢，可以试试。

## 为什么是 AI IDE

以 Cursor 为例，Cursor 的上下文引用能力远高于目前遇到的任何文档，可以 @ 一篇文档、一个文件夹，甚至是之前与 AI 的历史对话，而且，还可以选择是否基于 Codebase 回答。

如果你不想 @ 上下文，其 Agent（智能体）模式还可以自主拆解问题，读取上下文，相比较而言，我觉得大部分文档的 AI 能力有些机械，说一句做一句。

![Cursor 上下文功能](/images/posts/best-local-ai-note-taking-tools/cursor-context.webp)

另外，Cursor 对文档内容的修改是 Inline（句子）级别的。

举个例子，在 Notion 里面，当我们让 AI 一次润色好几段内容，它会修改全部，我们要么一起接受，要么都放弃，而在 Cursor 里，对文本的修改就像代码一样，它会按需修改，然后我们可以逐条选择或者拒绝，这才是精细化修改应该有的样子呀。

## 可以让体验更好一些

Cursor 这类 IDE 工具毕竟是为代码而生的，有一定门槛，需要简单上个手。

### 第一步，学习一下编程工具的界面

不需要学习代码，只是熟悉界面，而且，一旦认识之后，以后再学习编程的门槛就更低了。

### 第二步，安装一些 Markdown 插件

编程工具是把所有文件当做代码来编辑，需要一些插件来改善编辑体验，这里我最推荐的是 [Markdown All in One](https://marketplace.cursorapi.com/items?itemName=yzhang.markdown-all-in-one)，还有很多其他的，比如，还有能让编辑 Markdown 像 Word 文档那样的体验，不过，不推荐，因为，影响了 AI 的能力发挥。

![Markdown 插件](/images/posts/best-local-ai-note-taking-tools/markdown-plugin.webp)

### 第三步，去掉一些 Markdown 语法的检测

如果不禁用，会显示很多波浪线形式的下划线，有点类似于文档编辑里的拼写检查，影响编辑的心情。不过，如果不介意的话，可以忽略这一步。因为，去掉这个有些麻烦，需要更改配置文件，我是让 AI 帮忙修改的配置文件。

### 第四步，创建笔记别忘了加上后缀

与普通笔记不一样，用代码编辑器来新增 Markdown 文件是需要这样的格式：name.md

这样一来，我们就有了一个真 Local first（本地优先）的 AI 笔记方案。 