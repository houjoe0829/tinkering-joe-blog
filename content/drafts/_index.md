---
title: "草稿箱"
description: "这里存放尚未完成的文章草稿"
layout: "list"
draft: true
---

这个目录用于存放正在编写中的文章草稿。当文章完成后，可以将文件移动到 `content/posts` 目录发布。

以下是当前的草稿列表：

## 使用方法

1. 在 `content/drafts` 目录下创建新的 Markdown 文件
2. 文件命名规则与 posts 相同，使用英文短横线分隔
3. 在本地预览时（使用 `hugo server -D`）可以看到草稿内容
4. 文章完成后，将文件移动到 `content/posts` 目录即可发布

## 示例文件头

```yaml
---
title: "文章标题"
date: 2024-02-10
draft: true
tags: ["标签1", "标签2"]
categories: ["分类"]
---
``` 