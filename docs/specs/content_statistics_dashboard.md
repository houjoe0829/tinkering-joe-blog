# 博客内容统计 Dashboard 规范

## 概述

博客内容统计 Dashboard 是一个自动化的内容分析系统，可以实时统计博客的创作成果，包括字数统计、内容分类和时间维度分析。该系统通过 Git Pre-commit Hook 实现完全自动化，为创作者提供直观的数据反馈。

## 功能特性

### 核心功能
- **字数统计**：自动统计中文字符数和英文单词数
- **内容分类**：分别统计博文、随思录和全景图片数量
- **时间维度**：提供总体统计和今年统计两个维度
- **完全自动化**：通过 Git Pre-commit Hook 实现无感知自动更新

### 展示位置
- **主要入口**：博客搜索页面
- **展示内容**：创作成果的可视化统计信息
- **数据格式**：以万字为单位显示，方便阅读

### 统计维度
1. **📊 总体统计**：
   - 总字数（中文字符 + 英文单词）
   - 博文总数
   - 随思录总数
   - 全景图片总数

2. **🎯 今年统计**：
   - 今年创作的字数
   - 今年发布的内容数量
   - 按内容类型分类的年度统计

## 统计规则详解

### 字数统计包含内容
以下内容会被计入字数统计：

1. **正文内容**：文章的主要文字内容
2. **代码块内容**：```代码块中的所有文本
3. **引用文本内容**：> 引用块中的文字
4. **图片 Alt 文本**：`![Alt文本](图片路径)` 中的描述文字

### 字数统计排除内容
以下内容不会被计入字数统计：

1. **Markdown 语法标记**：如 `#`、`**`、`[]()` 等格式化符号
2. **链接 URL**：链接地址本身（但保留链接显示文本）
3. **Front Matter 元数据**：YAML 头部的配置信息
4. **HTML 标签**：`<div>`、`<span>` 等 HTML 标记
5. **全景图片文字**：天空之眼内容中的描述文字（按需求可配置）

### 内容分类规则
- **博文 (Posts)**：`content/posts/` 目录下的所有 `.md` 文件
- **随思录 (Thoughts)**：`content/thoughts/` 目录下的所有 `.md` 文件
- **全景图片 (Sky Eye)**：`content/sky-eye/` 目录下的所有 `.md` 文件

## 自动化机制

### Git Pre-commit Hook（推荐方案）

#### 工作原理
- **触发时机**：每次执行 `git commit` 时自动触发
- **智能检测**：只有当 `content/` 目录有变更时才运行
- **自动更新**：自动更新字数统计数据并加入本次提交
- **无感知运行**：完全不需要手动操作

#### 使用方法
```bash
# 正常的 Git 工作流，字数统计会自动更新
git add content/thoughts/your-new-thought.md
git commit -m "新增 Thought"
# Hook 会自动检测内容变更，更新字数统计，并将更新后的数据文件加入提交
```

#### 智能特性
1. **环境检测**：如果虚拟环境或依赖不存在，会优雅跳过（不阻止提交）
2. **静默运行**：不会干扰正常的 Git 工作流
3. **高效执行**：只在有内容变更时运行，避免无意义的更新
4. **错误处理**：即使统计失败也不会阻止 Git 提交

### 手动触发方式

#### 开发环境启动
使用自动化开发脚本，会在启动前更新字数统计：
```bash
./scripts/dev.sh
```

#### 生产构建
使用自动化构建脚本，会在构建前更新字数统计：
```bash
./scripts/build.sh
```

#### 手动更新统计数据
如果只需要手动更新字数统计数据：
```bash
# 激活虚拟环境
source .venv/bin/activate

# 生成字数统计数据
cd scripts
python3 generate_word_count_data.py
```

#### 单文章调试
如果需要查看单篇文章的字数统计：
```bash
source .venv/bin/activate
python3 scripts/word_count.py --file content/posts/article-name.md
```

## 技术实现架构

### 数据处理流程
1. **数据预处理**：Python 脚本解析 Markdown 文件，清理文本内容
2. **字数计算**：区分中文字符和英文单词进行精确统计
3. **数据存储**：统计结果保存为 `data/word_count.json` 供 Hugo 读取
4. **前端展示**：搜索页面模板读取数据文件并渲染统计信息

### 关键文件说明
- **统计脚本**：`scripts/word_count.py` - 单文件字数统计
- **数据生成**：`scripts/generate_word_count_data.py` - 生成完整统计数据
- **数据文件**：`data/word_count.json` - Hugo 读取的数据源
- **Git Hook**：`.git/hooks/pre-commit` - 自动化触发脚本

### 数据结构示例
```json
{
  "total": {
    "chinese_chars": 125000,
    "english_words": 15000,
    "posts_count": 85,
    "thoughts_count": 120,
    "sky_eye_count": 25
  },
  "current_year": {
    "chinese_chars": 25000,
    "english_words": 3000,
    "posts_count": 15,
    "thoughts_count": 30,
    "sky_eye_count": 5
  }
}
```

## 部署和配置

### 环境要求
- **Python 环境**：Python 3.7+
- **依赖库**：参考 `requirements.txt`
- **Hugo 版本**：支持数据文件读取的版本

### 初始化设置
1. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

2. **配置虚拟环境**：
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **初始化数据**：
   ```bash
   cd scripts
   python3 generate_word_count_data.py
   ```

### Git Hook 配置
Git Pre-commit Hook 通常在项目克隆后自动配置，如需手动设置：

1. **检查 Hook 状态**：
   ```bash
   ls -la .git/hooks/pre-commit
   ```

2. **确保可执行权限**：
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

## 使用指南

### 查看统计结果
1. **访问位置**：博客搜索页面 (`/search/`)
2. **统计内容**：
   - 📊 总体统计：总字数、博文数、随思录数、全景图片数
   - 🎯 今年统计：今年创作的字数和内容数量
3. **数据格式**：字数以万字为单位显示，便于阅读

### 日常使用流程
1. **正常创作**：按常规流程创作和编辑内容
2. **提交内容**：使用 `git commit` 提交内容变更
3. **自动更新**：系统自动更新统计数据
4. **查看结果**：在搜索页面查看最新统计

### 故障排除
1. **统计数据不更新**：
   - 检查 Git Hook 是否正常工作
   - 手动运行数据生成脚本
   - 确认虚拟环境和依赖正常

2. **字数统计异常**：
   - 检查 Markdown 文件格式是否正确
   - 确认 Front Matter 格式符合规范
   - 查看脚本运行日志

3. **页面显示问题**：
   - 确认 `data/word_count.json` 文件存在
   - 检查 JSON 文件格式是否正确
   - 重新构建 Hugo 站点

## 性能和优化

### 性能特点
- **增量更新**：只在内容变更时运行，避免无必要的计算
- **快速处理**：单次统计通常在几秒内完成
- **低资源消耗**：Python 脚本占用资源少，不影响系统性能

### 优化建议
1. **定期清理**：清理不再使用的临时文件
2. **监控日志**：关注统计脚本的运行日志
3. **数据备份**：定期备份统计数据文件

## 扩展和定制

### 添加新的统计维度
1. **修改统计脚本**：在 `word_count.py` 中添加新的统计逻辑
2. **更新数据结构**：修改 JSON 数据结构
3. **调整前端模板**：更新搜索页面的显示模板

### 自定义统计规则
1. **修改包含/排除规则**：调整字数统计的范围
2. **添加内容类型**：支持新的内容分类
3. **时间维度扩展**：添加月度、季度等统计维度

## 注意事项和最佳实践

### 重要注意事项
- **推荐使用 Git Hook**：这是最便捷的方式，完全无需手动操作
- **Cloudflare 构建限制**：由于 Cloudflare Pages 只运行 `hugo` 命令，字数统计数据需要通过 Git 提交来保持同步
- **数据一致性**：Git Hook 确保每次提交内容时，字数统计数据都是最新的

### 最佳实践
1. **定期检查**：偶尔检查统计数据的准确性
2. **备份数据**：重要的统计数据应该有备份
3. **文档更新**：当统计规则变更时及时更新文档
4. **性能监控**：关注统计功能对整体性能的影响

## 相关文档和资源

### 相关规范文档
- **内容类型规范**：[`content_types_overview.md`](content_types_overview.md)
- **Thoughts 创建流程**：[`thoughts_creation_workflow.md`](thoughts_creation_workflow.md)
- **Notion 内容导入**：[`notion_zip_processing_workflow.md`](notion_zip_processing_workflow.md)

### 技术参考
- **Hugo 数据文件**：[Hugo Data Templates](https://gohugo.io/templates/data-templates/)
- **Git Hooks**：[Git Hooks Documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- **Python Markdown 处理**：相关 Python 库文档
