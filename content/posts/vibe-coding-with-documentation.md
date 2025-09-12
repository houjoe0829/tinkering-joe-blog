---
author: "Joe"
date: 2025-09-12
description: "与 AI 协作编程的实践总结：通过合理的文档分工，让 README 和 docs 各司其职，减少协作噪音，提升开发效率"
draft: false
tags: ["Vibe Coding", "工作感悟"]
title: "基于文档的 Vibe Coding：README 与 docs 的分工"
---


与 AI 协作编程的这半年，已经把 Vibe Coding 的过程还原成一件朴素的事：用文档与 AI 协作。

毕竟，对话里的噪音太多，只要 AI 没有突破上下文的限制，顾此失彼的修改是 AI 常有的事情。而文档可以成为与 AI 共享的相对稳定的语境，从模糊的念头到逐渐清晰的方案，从独立小任务的实现到基于文档的代码 Review。

不过，文档既算记忆，也是秩序。需要把沉淀性文档和过程性文档区分开，这大概是俗称的，如果都是重点就没有重点，目标是，减少噪音，并让确定性的逻辑既能被固化，又能随时更新。

现在，在代码仓库里直接写文档已经是不争的时候，而且即使不是公开仓库，我也会认真写一写 README，既写给未来的自己，也写给 AI 看。

基于这段时间的实践，重新设计了一下 README 与 docs 的分工。不过，这只是我的尝试，未必适合所有人，但或许能提供一些参考。

## 文档分工：README 与 docs

- **README.md**：仓库的入口说明，负责「整体介绍、环境配置、目录导航、文档规则」。它是对外的门面，也是你未来快速理解仓库的指南。
- **docs/**：仓库的知识库，负责「产品愿景、需求定论、过渡方案、Bug 记录」。它是内部的沉淀，承载所有与产品和实现相关的决策与经验。

二者的关系：

- README 是**索引和规则**，告诉你「项目里有什么、怎么用」。
- docs 是**内容和知识**，存放需求、方案、Bug 及相关定论。

## README 设计

1. **Overview**
- 一句话介绍项目用途
- 简要说明仓库包含代码与文档（scope/specs/staging/bugs）
2. **Getting Started**
- 环境依赖
- 安装步骤
- 运行方式
3. **Project Structure**
- 树状图展示仓库目录（src, tests, scripts, docs 等）
4. **Docs Structure**
- 概述 docs/ 的子目录及功能：
- `scope/` → 愿景与原则
- `specs/` → 固化定论
- `staging/` → 执行文档（带状态）
- `bugs/` → Bug 记录（带状态）
- 明确命名规则：`[状态] 简短描述.md`

## 知识库 docs 设计

### 📂 目录组织

```
docs/
├── scope/       # 产品愿景、范围、原则等长期定论
├── specs/       # 已经固化下来的需求与技术实现逻辑
├── staging/     # 过渡区：从想法到执行的方案，最终会并入 specs 或废弃
├── bugs/        # 疑难 Bug 记录与解决方案
```

### 📝 文档命名规范

```
[状态] 简短描述.md
```

** 状态定义 **

- `[open]`：进行中，方案在推进或问题正在排查
- `[solved]`：已解决，方案已落地并固化进 specs，或 Bug 已有结论
- `[abandoned]`：放弃，不再推进或确认无法复现

** 示例 **

- staging/[open]new-import-flow.md
- staging/[solved]data-cleaning-logic.md
- bugs/[abandoned]proxy-auth-bug.md

### 🔄 文档生命周期

1. 新需求 → 写入 `staging/[open] xxx.md`
2. 方案完成并固化 → 移动 / 合并到 `specs/`，原文件改为 `[solved]` 或删除
3. 确认不做的方案 → 改为 `[abandoned]`
4. Bug 同理，最终状态只可能是 `[solved]` 或 `[abandoned]`

这样设计后：

- **README** 是门面，让 AI 或者未来的自己能快速理解项目。
- **docs** 是知识库，确保产品与实现的知识有序沉淀。
- ** 最佳实践 ** 是通过 README → docs 的分工，让代码和文档同源、同步演进。
