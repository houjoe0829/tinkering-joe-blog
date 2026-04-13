# 博客文章英文翻译规范

## 一、核心原则

### 1.1 保持原文的口语化和亲切感
- 原文风格：轻松、口语化、带有个人色彩的叙述
- 翻译时避免过于正式或学术化的表达
- 保留原文中的语气词和情感色彩（如"哎"、"老实说"、"其实"等）

### 1.2 尊重中文语境下的专有表达
- 不强行直译中文特有的表达方式
- 在英文语境下寻找对等的自然表达
- 必要时用意译而非直译

### 1.3 技术术语的处理
- 技术类词汇使用英文语境下的标准术语
- 例如：
  - "远程工作" → "remote work"（而非 "distant work"）
  - "Demo" → 保持 "Demo"（已是通用术语）
  - "MVP" → 保持 "MVP"（Minimum Viable Product）
  - "Dog fooding" → 保持 "dog fooding"（行业黑话）
  - "Vibe Coding" → 保持 "Vibe Coding"（新兴概念）

## 二、具体翻译策略

### 2.1 地名和专有名词
- **中国地名**：使用拼音 + 英文解释（首次出现时）
  - 例："襄阳" → "Xiangyang (a city in Hubei Province)"
  - 后续出现直接用拼音："Xiangyang"
- **景点名称**：拼音 + 意译
  - 例："金山寺" → "Jinshan Temple"
  - "西津渡" → "Xijin Ferry (Historic District)"
- **食物名称**：拼音 + 描述性翻译
  - 例："锅盖面" → "Guogai Noodles (noodles cooked with a small lid)"
  - "水晶肴肉" → "Crystal Pork Terrine"
  - "灯盏糕" → "Dengzhan Cake (a local fried pastry)"

### 2.2 文化特定概念
- **节日习俗**：保留拼音 + 解释
  - "插清明" → "Chaqingming (a Qingming Festival ritual of placing flowers at graves)"
- **地方特色**：意译为主，必要时加注
  - "打工之城" → "a city known for its migrant workers"
  - "江浙沪包游" → "exploring the Jiangsu-Zhejiang-Shanghai region"

### 2.3 口语化表达的转换
原文中大量使用口语化表达，翻译时需要找到英文中对等的自然表达：

| 中文表达 | 不推荐的直译 | 推荐的翻译 |
|---------|------------|----------|
| "老实说" | "Honestly speaking" | "To be honest" / "Truth be told" |
| "其实" | "Actually" | "In fact" / "The thing is" |
| "说到底" | "Speaking to the bottom" | "At the end of the day" / "Fundamentally" |
| "哎" | "Ai" | "Well," / "Sigh," / 或省略 |
| "卧槽" | 直译不当 | "Wow" / "Holy cow" / "No way" |
| "有点哭笑不得" | 直译困难 | "It's bittersweet" / "I don't know whether to laugh or cry" |

### 2.4 标题翻译
- 保持简洁有力
- 可以适当调整以符合英文表达习惯
- 例如：
  - "乡村、县城与新的工位" → "Remote Work from My Village: A New Workspace"
  - "Demo 与产品之间，有条鸿沟" → "The Gap Between Demo and Product"
  - "温州，一座被刻板印象耽误了的城市" → "Wenzhou: Beyond the Stereotypes"

## 三、文章结构处理

### 3.1 Front Matter（元数据）
```yaml
---
author: "Joe"
date: 2026-04-11
description: "英文翻译的描述"
draft: false
tags: ["Small Town Stories", "Life Reflections"]  # 标签翻译
title: "英文标题"
---
```

### 3.2 图片路径
- 保持原有的图片路径不变
- 图片说明（如果有）需要翻译

### 3.3 段落和小标题
- 保持原文的段落结构
- 小标题翻译要简洁明了
- 例如："## 吸引我们来的是美食" → "## The Food Drew Us In"

## 四、特殊情况处理

### 4.1 引用和俗语
- 中国俗语：意译 + 必要时加原文注释
  - "镇江有三怪" → "Zhenjiang has 'Three Oddities' (a local saying)"

### 4.2 数字和单位
- 保持原有的公制单位（公里、米等）
- 可以在括号中添加英制单位（可选）
  - "100 公里" → "100 kilometers" 或 "100km"

### 4.3 时间表达
- 使用英文习惯的时间表达
  - "清明节前夕" → "just before Qingming Festival (Tomb-Sweeping Day)"
  - "四月下旬" → "late April"

## 五、质量检查清单

翻译完成后，检查以下几点：

- [ ] 是否保持了原文的口语化和亲切感？
- [ ] 技术术语是否使用了英文语境下的标准表达？
- [ ] 地名、食物名称等是否采用了拼音 + 解释的方式？
- [ ] 是否避免了生硬的直译？
- [ ] 标题是否简洁有力且符合英文习惯？
- [ ] 文章的情感色彩是否得到保留？
- [ ] 是否有明显的中式英语表达需要修正？

## 六、翻译工作流程

1. **通读全文**：理解文章的整体语气和核心信息
2. **标记难点**：标出需要特殊处理的文化概念、俗语等
3. **初译**：完成第一遍翻译
4. **润色**：检查口语化程度，调整不自然的表达
5. **校对**：对照质量检查清单进行最后检查
6. **文件放置**：翻译后的文件放在 `/content/en/posts/` 对应路径下

## 七、示例对照

### 示例 1：口语化段落
**原文：**
> 老实说，温州给我们的惊喜，从出发前就开始积累了：以为是打工之城，去了发现，美食与历史兼备。

**翻译：**
> To be honest, Wenzhou surprised us from the very beginning. We expected a factory town, but what we found was a city rich in both food and history.

### 示例 2：技术类段落
**原文：**
> Demo 跑通只是回答了「这件事能不能做出来」，而产品要回答的是在真实、混乱的情况下能否稳定帮用户完成任务。

**翻译：**
> A working demo only answers "Can this be built?" A product, on the other hand, must answer "Can it reliably help users complete their tasks in real, messy situations?"

---

**最后更新：** 2026-04-13
**适用范围：** 所有博客文章的英文翻译
