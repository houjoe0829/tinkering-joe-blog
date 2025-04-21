---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }} # 从原始文件名中提取的日期
description: ""
thumbnail: "/images/sky-eye/{{ .File.ContentBaseName }}-thumb.jpg"  # 缩略图路径
panorama_image: "/images/sky-eye/optimized/{{ .File.ContentBaseName }}.webp"   # 优化后的全景图路径
draft: false
---
