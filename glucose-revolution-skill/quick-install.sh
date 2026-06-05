#!/bin/bash

# 控糖革命 Skill - 一键安装脚本
# 从 GitHub 直接下载并安装

set -e

REPO="yourusername/glucose-revolution-skill"
VERSION="${1:-latest}"

if [ "$VERSION" = "latest" ]; then
    URL="https://github.com/${REPO}/releases/latest/download/glucose-revolution-skill.zip"
else
    URL="https://github.com/${REPO}/releases/download/${VERSION}/glucose-revolution-skill.zip"
fi

echo "======================================"
echo " 控糖革命 Skill - 一键安装"
echo "======================================"
echo ""
echo "下载地址: ${URL}"
echo ""

# 检测安装路径
INSTALL_PATH=""
if [ -d "$HOME/.workbuddy/skills/custom" ]; then
    INSTALL_PATH="$HOME/.workbuddy/skills/custom"
    echo "✓ 检测到 WorkBuddy"
elif [ -d "$HOME/.lingtai/custom" ]; then
    INSTALL_PATH="$HOME/.lingtai/custom"
    echo "✓ 检测到 灵台 TUI"
else
    echo "⚠️ 未检测到 WorkBuddy 或灵台 TUI"
    echo "将安装到当前目录的 .skills 文件夹"
    INSTALL_PATH="$PWD/.skills"
    mkdir -p "$INSTALL_PATH"
fi

echo "✓ 安装路径: ${INSTALL_PATH}"
echo ""

# 下载
echo "正在下载..."
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

if command -v curl &> /dev/null; then
    curl -L -o skill.zip "$URL"
elif command -v wget &> /dev/null; then
    wget -O skill.zip "$URL"
else
    echo "❌ 需要 curl 或 wget"
    exit 1
fi

# 解压
echo "正在解压..."
unzip -q skill.zip -d glucose-revolution-skill

# 安装
if [ -d "$INSTALL_PATH/glucose-revolution-skill" ]; then
    echo "⚠️ 已存在旧版本，正在备份..."
    mv "$INSTALL_PATH/glucose-revolution-skill" "$INSTALL_PATH/glucose-revolution-skill.backup.$(date +%Y%m%d%H%M%S)"
fi

mv glucose-revolution-skill "$INSTALL_PATH/"

# 清理
cd -
rm -rf "$TEMP_DIR"

echo ""
echo "======================================"
echo " ✅ 安装成功!"
echo "======================================"
echo ""
echo "安装位置: ${INSTALL_PATH}/glucose-revolution-skill"
echo ""
echo "使用方法:"
echo "  1. 重启你的 AI 助手"
echo "  2. 输入'控糖'或'帮我管理血糖'激活 Skill"
echo "  3. 开始对话！"
echo ""
echo "触发关键词:"
echo "  - 控糖 / 血糖"
echo "  - 餐后困倦 / 减肥困难"
echo "  - 怎么控糖 / 控糖自测"
echo ""
