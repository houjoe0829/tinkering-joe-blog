---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }} # 从原始文件名中提取的日期
description: ""
thumbnail: "/images/sky-eye/{{ .File.ContentBaseName }}-thumb.jpg"  # 缩略图路径
panorama_image: "/images/sky-eye/optimized/{{ .File.ContentBaseName }}.webp"   # 优化后的全景图路径
location: "" # 拍摄地点名称，如“上海市黄浦区”
coordinates: "" # 经纬度，格式为“纬度,经度”，如“31.2304,121.4737”
draft: false
---
