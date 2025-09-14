# 全局图片压缩工作流程规范

## 概述

为了优化网站加载速度和存储空间，博客需要定期对图片进行压缩处理和 WebP 转换。本文档详细规定了全局图片压缩的标准流程和最佳实践。

## 压缩目标

- **性能优化**：减少图片文件大小，提升网站加载速度
- **存储优化**：节省服务器存储空间和带宽成本
- **格式统一**：将所有图片统一转换为 WebP 格式
- **质量保证**：在压缩的同时保持图片的视觉质量

## 压缩工具和参数

### 核心工具
- **主要脚本**：`scripts/compress_images.py`
- **依赖工具**：ImageMagick
- **处理范围**：`static` 目录下的所有图片（包括子目录）

### 压缩参数配置
- **质量设置**：85%（可在脚本中调整 quality 参数）
- **最大尺寸**：1920x1920 像素（保持原始宽高比）
- **元数据处理**：自动移除图片元数据以减少文件大小
- **格式转换**：
  - PNG 文件：使用无损压缩转换为 WebP
  - JPG 文件：使用有损压缩转换为 WebP
- **保护文件**：网站图标相关文件（favicon、apple-touch-icon、android-chrome）保持原格式

## 完整压缩流程

### 环境准备

#### 1. 安装依赖工具
```bash
# macOS 用户
brew install imagemagick

# Ubuntu/Debian 用户
sudo apt-get install imagemagick

# CentOS/RHEL 用户
sudo yum install ImageMagick
```

#### 2. 验证工具安装
```bash
# 验证 ImageMagick 是否正确安装
magick --version
```

### 执行压缩流程

#### 步骤 1：运行压缩脚本
```bash
python3 scripts/compress_images.py
```

**执行结果**：
- 在项目根目录创建 `static_compressed` 目录
- 存放所有压缩后的文件，保持原有目录结构
- 显示压缩进度和统计信息

#### 步骤 2：复制压缩后的文件
```bash
cp -r static_compressed/* static/
```

**执行结果**：
- 将压缩后的文件复制回原目录
- 原始文件作为备份保留
- 新的 WebP 文件与原文件并存

#### 步骤 3：更新图片引用
```bash
python3 scripts/update_image_refs.py
```

**执行结果**：
- 自动扫描所有 Markdown 文件
- 将图片引用更新为 WebP 格式
- 例如：`![示例图片](/images/example.jpg)` → `![示例图片](/images/example.webp)`

#### 步骤 4：预览要删除的原始文件
```bash
python3 scripts/clean_original_images.py
```

**执行结果**：
- 显示将被删除的原始文件列表
- 显示可以节省的存储空间大小
- 不会实际删除任何文件，仅供预览

#### 步骤 5：删除原始文件
```bash
python3 scripts/clean_original_images.py --execute
```

**执行结果**：
- 删除已经转换为 WebP 格式的原始图片文件
- 保留网站图标等特殊文件
- 释放存储空间

#### 步骤 6：清理临时文件
```bash
# 清理 Notion 处理的临时文件
rm -rf temp_notion
rm -f temp_files/*.zip

# 清理图片压缩的临时目录
rm -rf static_compressed
rm -rf static/images_compressed
```

**执行结果**：
- 删除所有临时目录和文件
- 保持项目目录整洁

## 自动化脚本选项

### 批量处理脚本
可以创建一个自动化脚本来执行完整流程：

```bash
#!/bin/bash
# 全局图片压缩自动化脚本

echo "开始全局图片压缩..."

# 1. 运行压缩脚本
echo "步骤 1: 压缩图片..."
python3 scripts/compress_images.py

# 2. 复制压缩后的文件
echo "步骤 2: 复制压缩文件..."
cp -r static_compressed/* static/

# 3. 更新图片引用
echo "步骤 3: 更新图片引用..."
python3 scripts/update_image_refs.py

# 4. 预览要删除的文件
echo "步骤 4: 预览要删除的文件..."
python3 scripts/clean_original_images.py

# 询问用户是否继续
read -p "是否继续删除原始文件？(y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    # 5. 删除原始文件
    echo "步骤 5: 删除原始文件..."
    python3 scripts/clean_original_images.py --execute
    
    # 6. 清理临时文件
    echo "步骤 6: 清理临时文件..."
    rm -rf temp_notion
    rm -f temp_files/*.zip
    rm -rf static_compressed
    rm -rf static/images_compressed
    
    echo "全局图片压缩完成！"
else
    echo "已取消删除原始文件。"
fi
```

## 质量检查

### 压缩后验证
```bash
# 检查图片引用是否有效
python3 scripts/check_image_refs.py

# 检查文件大小变化
du -sh static/images/
```

### 视觉质量检查
- 随机抽查几张压缩后的图片
- 确认图片质量符合预期
- 检查是否有明显的压缩痕迹

## 最佳实践

### 执行时机
1. **新增大量图片后**：添加多篇包含图片的文章后
2. **定期维护**：建议每月执行一次全局压缩
3. **部署前**：重要更新部署前进行一次压缩
4. **存储空间紧张时**：当存储使用率较高时

### 注意事项
1. **备份重要图片**：执行前确保重要图片有备份
2. **测试环境验证**：先在测试环境执行完整流程
3. **分批处理**：如果图片数量很多，可以考虑分批处理
4. **监控磁盘空间**：确保有足够的临时存储空间

### 性能优化建议
1. **选择合适时间**：在服务器负载较低时执行
2. **并行处理**：对于大量图片，可以考虑并行压缩
3. **增量处理**：只处理新增或修改的图片

## 故障排除

### 常见问题

**Q: ImageMagick 安装失败怎么办？**
A: 尝试使用不同的包管理器，或从官网下载二进制包安装。

**Q: 压缩脚本运行出错怎么办？**
A: 检查 Python 环境和依赖，确保所有必要的库都已安装。

**Q: 压缩后图片质量下降明显怎么办？**
A: 调整脚本中的质量参数，从 85% 提高到 90% 或 95%。

**Q: 某些图片无法压缩怎么办？**
A: 检查图片格式是否支持，某些特殊格式可能需要单独处理。

### 回滚方案
如果压缩结果不满意，可以通过以下方式回滚：
1. 从 Git 历史恢复原始文件
2. 使用备份文件替换压缩后的文件
3. 重新运行引用更新脚本

## 性能指标

### 预期效果
- **文件大小减少**：通常可减少 30-70% 的文件大小
- **加载速度提升**：页面加载速度提升 20-50%
- **带宽节省**：减少 CDN 带宽使用成本

### 监控指标
- 压缩前后文件大小对比
- 网站页面加载时间变化
- 用户访问体验反馈
