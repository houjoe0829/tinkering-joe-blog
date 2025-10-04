# 天空之眼图片添加工作流程规范

## 概述

天空之眼（Sky Eye）是博客上展示无人机拍摄的 360° 全景照片的专属栏目。本文档详细规定了添加新全景图片的标准流程，包括图片准备、处理、创建内容和质量检查等各个环节。

## 内容特点

- **360° 全景图片**：必须是无人机拍摄的 360° 全景照片
- **高质量展示**：支持交互式全景浏览（拖拽、缩放、全屏）
- **元数据丰富**：包含拍摄时间、地点、坐标等信息
- **性能优化**：经过压缩和格式转换，确保快速加载
- **响应式设计**：适配桌面端和移动端不同设备

## 技术规格

### 全景图片规格
- **分辨率**：6000x3000 像素（从原始 8192x4096 调整而来）
- **格式**：WebP
- **质量**：85%
- **存储位置**：`static/images/sky-eye/optimized/`

### 缩略图规格
- **分辨率**：800x400 像素
- **格式**：JPG
- **质量**：85%
- **存储位置**：`static/images/sky-eye/`

### 文件命名规范
- 使用英文单词，避免使用拼音
- 单词之间使用短横线 `-` 分隔
- 必须具有描述性，体现拍摄地点
- 示例：`hangzhou-xihu-lake.jpg`、`scotland-skye-island.jpg`

## 完整添加流程

### 前期准备

#### 1. 环境依赖检查

确保已安装必要的工具：

```bash
# 检查 ImageMagick（用于图片处理）
magick --version

# 检查 exiftool（用于读取 EXIF 信息）
exiftool -ver

# 如果未安装，使用以下命令安装
# macOS
brew install imagemagick exiftool

# Ubuntu/Debian
sudo apt-get install imagemagick libimage-exiftool-perl
```

#### 2. 获取原始全景图片

从无人机导出原始全景图片（通常为 JPG 格式，分辨率为 8192x4096）。

### 主要处理流程

#### 步骤 1：提取图片元数据

将原始全景图片放入 `temp_files/` 目录，然后使用 `exiftool` 提取 EXIF 信息：

```bash
# 进入临时文件目录
cd temp_files/

# 提取 EXIF 信息
exiftool your-panorama-image.JPG
```

**重点信息**：
- `Date/Time Original`：拍摄时间
- `GPS Position`：GPS 坐标（格式：30 deg 38' 50.80" N, 119 deg 49' 12.50" E）

**坐标格式转换**：
将度分秒格式转换为十进制格式。例如：
- `30 deg 38' 50.80" N` → `30.647444`
- `119 deg 49' 12.50" E` → `119.820417`

**计算公式**：度 + (分/60) + (秒/3600)

**地点名称获取**：
使用坐标在 Google Maps 中查找，获取人类可读的地点名称。

#### 步骤 2：生成优化的全景图

使用 ImageMagick 将原始图片调整大小并转换为 WebP 格式：

```bash
# 从 temp_files/ 目录执行
# 将文件名替换为实际的文件名（使用英文命名）

magick your-panorama-image.JPG \
  -auto-orient \
  -strip \
  -resize 6000x3000 \
  -quality 85 \
  -sampling-factor 4:2:0 \
  -colorspace sRGB \
  ../static/images/sky-eye/optimized/your-file-name.webp
```

**参数说明**：
- `-auto-orient`：自动处理图片方向
- `-strip`：移除 EXIF 等元数据（减小文件大小）
- `-resize 6000x3000`：调整分辨率
- `-quality 85`：压缩质量 85%
- `-sampling-factor 4:2:0`：优化色彩采样
- `-colorspace sRGB`：使用 sRGB 色彩空间

**预期效果**：文件大小从 14MB 减小到约 1MB（压缩率约 93%）

#### 步骤 3：生成缩略图

从原始图片生成缩略图：

```bash
# 从 temp_files/ 目录执行

magick your-panorama-image.JPG \
  -auto-orient \
  -strip \
  -resize 800x400^ \
  -gravity center \
  -extent 800x400 \
  -quality 85 \
  ../static/images/sky-eye/your-file-name-thumb.jpg
```

**参数说明**：
- `-resize 800x400^`：调整大小，保持比例并填满目标尺寸
- `-gravity center`：居中裁剪
- `-extent 800x400`：精确裁剪到目标尺寸

#### 步骤 4：创建 Markdown 内容文件

在 `content/sky-eye/` 目录创建新的 Markdown 文件：

```bash
# 创建新文件（文件名与图片文件名保持一致）
hugo new sky-eye/your-file-name.md
```

这会基于 `archetypes/sky-eye.md` 模板创建文件，自动生成基础结构。

#### 步骤 5：编辑内容文件

编辑生成的 Markdown 文件，填写完整的元数据：

```yaml
---
title: "浙江省湖州市德清县莫干山云海"
date: 2024-03-15T10:30:00+08:00  # 使用从 EXIF 提取的拍摄时间
description: "清晨时分，莫干山上云雾缭绕，形成壮观的云海景观"
thumbnail: "/images/sky-eye/your-file-name-thumb.jpg"
panorama_image: "/images/sky-eye/optimized/your-file-name.webp"
location: "浙江省湖州市德清县莫干山"  # 使用 Google Maps 查询的地点名称
coordinates: "30.647444,119.820417"  # 从 EXIF 提取并转换的坐标
draft: false
---
```

**重要说明**：
- `title`：简洁描述性的标题，建议包含地点名称
- `date`：使用 ISO 8601 格式，包含时区信息（+08:00 表示北京时间）
- `description`：详细描述拍摄的场景、天气、特点等
- `location`：人类可读的地点名称，从大到小（省/市/区/具体地点）
- `coordinates`：十进制格式的经纬度，格式为 "纬度,经度"
- 文件路径必须与实际生成的文件路径一致

#### 步骤 6：清理临时文件

完成处理后，清理临时文件：

```bash
# 删除 temp_files/ 目录中的原始文件
rm temp_files/your-panorama-image.JPG
```

### 质量检查

#### 1. 图片引用检查

运行脚本检查图片引用是否有效：

```bash
# 在项目根目录执行
python3 scripts/check_image_refs.py
```

确保没有错误或警告信息。

#### 2. 文件大小验证

检查生成的图片文件大小是否符合预期：

```bash
# 检查优化后的全景图
ls -lh static/images/sky-eye/optimized/your-file-name.webp
# 预期：约 1-2MB

# 检查缩略图
ls -lh static/images/sky-eye/your-file-name-thumb.jpg
# 预期：约 50-100KB
```

## 高级功能

### 在博文中嵌入天空之眼图片

可以在普通博文中嵌入天空之眼全景图：

```markdown
{{< sky-eye-embed id="your-file-name" title="浙江省湖州市德清县莫干山云海" >}}
```

**参数说明**：
- `id`：对应天空之眼 Markdown 文件名（不含 .md 扩展名）
- `title`：显示的标题

这会在博文中插入一个交互式的全景图预览卡片。

## 故障排除

### 图片无法加载
1. 检查文件路径是否正确（区分大小写）
2. 确认文件已经生成且在正确的目录下
3. 检查文件权限是否正确

### 全景浏览功能异常
1. 清除浏览器缓存后重试
2. 检查 JavaScript 控制台是否有错误信息
3. 确认图片格式是否为标准的 2:1 全景图

### 坐标或地点信息显示不正确
1. 检查 Front Matter 中的格式是否正确
2. 确认坐标格式为 "纬度,经度"（逗号分隔，无空格）
3. 验证坐标是否在合理范围内（纬度 -90~90，经度 -180~180）

### 缩略图质量不佳
1. 提高质量参数（从 85 提高到 90 或 95）
2. 调整裁剪位置，选择更有代表性的区域
3. 考虑手动创建缩略图以获得最佳效果

## 参考资料

- **Hugo 文档**：https://gohugo.io/documentation/
- **ImageMagick 文档**：https://imagemagick.org/script/command-line-options.php
- **Pannellum 文档**（全景查看器库）：https://pannellum.org/documentation/overview/
- **WebP 格式指南**：https://developers.google.com/speed/webp
- **GPS 坐标格式转换**：https://www.latlong.net/

## 相关文档

- 📋 [`content_types_overview.md`](content_types_overview.md) - 内容类型总览
- 📋 [`global_image_compression_workflow.md`](global_image_compression_workflow.md) - 全局图片压缩流程
- 📋 [`image_reference_validation.md`](image_reference_validation.md) - 图片引用验证
- 📋 [`content_cross_reference_system.md`](content_cross_reference_system.md) - 内容交叉引用系统

## 版本历史

- **v1.0**（2025-10-04）：初始版本，建立完整的天空之眼图片添加流程规范

