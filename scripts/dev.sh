#!/bin/bash

# 博客开发服务器脚本
# 功能：
# 1. 自动更新字数统计数据
# 2. 启动 Hugo 开发服务器

set -e  # 遇到错误时退出

echo "🚀 启动博客开发服务器..."

# 获取脚本所在目录的父目录（项目根目录）
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "📊 正在更新字数统计数据..."

# 检查虚拟环境是否存在
if [ ! -d ".venv" ]; then
    echo "❌ 虚拟环境不存在，请先创建虚拟环境"
    exit 1
fi

# 激活虚拟环境并运行字数统计脚本
source .venv/bin/activate

# 检查依赖是否已安装
if ! python3 -c "import frontmatter" 2>/dev/null; then
    echo "📦 安装 Python 依赖..."
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org python-frontmatter PyYAML
fi

# 运行字数统计数据生成脚本
echo "🔢 生成字数统计数据..."
cd scripts
python3 generate_word_count_data.py
cd ..

echo "✅ 字数统计数据更新完成"

# 启动 Hugo 开发服务器
echo "🏗️  启动 Hugo 开发服务器..."
hugo server -D 