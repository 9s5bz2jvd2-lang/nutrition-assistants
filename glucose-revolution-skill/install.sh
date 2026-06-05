#!/bin/bash

# 控糖革命 Skill 安装脚本
# Glucose Revolution Skill Installer

set -e

SKILL_NAME="glucose-revolution"
SKILL_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "======================================"
echo " 控糖革命 Skill 安装器"
echo " Glucose Revolution Skill Installer"
echo "======================================"
echo ""

# 检测平台
PLATFORM=""
INSTALL_PATH=""

if [ -d "$HOME/.workbuddy/skills/custom" ]; then
    PLATFORM="WorkBuddy"
    INSTALL_PATH="$HOME/.workbuddy/skills/custom"
elif [ -d "$HOME/.lingtai/custom" ]; then
    PLATFORM="Lingtai TUI"
    INSTALL_PATH="$HOME/.lingtai/custom"
elif [ -d "/home/yuan/.lingtai/custom" ]; then
    PLATFORM="Lingtai TUI (WSL)"
    INSTALL_PATH="/home/yuan/.lingtai/custom"
elif [ -d "/home/yuan/.workbuddy/skills/custom" ]; then
    PLATFORM="WorkBuddy (WSL)"
    INSTALL_PATH="/home/yuan/.workbuddy/skills/custom"
else
    echo "⚠️ 未检测到 WorkBuddy 或灵台 TUI 安装目录"
    echo ""
    echo "请选择安装方式："
    echo "1) 手动指定路径"
    echo "2) 安装到当前目录的 .skills 子目录"
    echo "3) 退出"
    read -p "选择 [1-3]: " choice
    
    case $choice in
        1)
            read -p "请输入技能目录路径: " custom_path
            INSTALL_PATH="$custom_path"
            PLATFORM="Custom"
            ;;
        2)
            INSTALL_PATH="$PWD/.skills"
            mkdir -p "$INSTALL_PATH"
            PLATFORM="Local"
            ;;
        *)
            echo "已退出安装"
            exit 0
            ;;
    esac
fi

echo "✓ 检测到平台: $PLATFORM"
echo "✓ 安装路径: $INSTALL_PATH"
echo ""

# 检查是否已存在
if [ -d "$INSTALL_PATH/$SKILL_NAME" ]; then
    echo "⚠️ 检测到已存在 $SKILL_NAME Skill"
    read -p "是否覆盖? [y/N]: " overwrite
    if [[ ! $overwrite =~ ^[Yy]$ ]]; then
        echo "已取消安装"
        exit 0
    fi
    rm -rf "$INSTALL_PATH/$SKILL_NAME"
fi

# 复制文件
echo "正在安装..."
mkdir -p "$INSTALL_PATH/$SKILL_NAME"
cp -r "$SKILL_DIR"/* "$INSTALL_PATH/$SKILL_NAME/"

# 清理安装脚本本身（如果在目标目录中）
if [ -f "$INSTALL_PATH/$SKILL_NAME/install.sh" ]; then
    rm "$INSTALL_PATH/$SKILL_NAME/install.sh"
fi

echo ""
echo "======================================"
echo " ✅ 安装成功!"
echo "======================================"
echo ""
echo "Skill名称: $SKILL_NAME"
echo "安装位置: $INSTALL_PATH/$SKILL_NAME"
echo ""
echo "触发关键词:"
echo "  - 控糖"
echo "  - 血糖"
echo "  - 饮食顺序"
echo "  - 胰岛素"
echo "  - ...以及任何血糖相关问题"
echo ""
echo "快速开始:"
echo "  1. 重启你的 AI 助手"
echo "  2. 输入'控糖'或'帮我管理血糖'激活 Skill"
echo "  3. 输入'控糖自测'开始症状评估"
echo ""
echo "完整文档:"
echo "  - README.md: 使用说明"
echo "  - QUICK_REFERENCE.md: 快速参考卡"
echo "  - system_prompt.md: 系统提示词（开发者）"
echo ""
