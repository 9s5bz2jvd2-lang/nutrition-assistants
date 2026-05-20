#!/bin/bash
# 骨质疏松症食养助手 安装脚本

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$HOME/.workbuddy/skills/custom/osteoporosis-food-guide-skill"

mkdir -p "$TARGET_DIR"

cp "${SCRIPT_DIR}/skill.yaml" "$TARGET_DIR/"
cp "${SCRIPT_DIR}/system_prompt.md" "$TARGET_DIR/"
cp "${SCRIPT_DIR}/knowledge_base.md" "$TARGET_DIR/"
[ -f "${SCRIPT_DIR}/recipes_data.md" ] && cp "${SCRIPT_DIR}/recipes_data.md" "$TARGET_DIR/"
[ -f "${SCRIPT_DIR}/recipes_overview.md" ] && cp "${SCRIPT_DIR}/recipes_overview.md" "$TARGET_DIR/"

echo "✅ 骨质疏松症食养助手安装完成！"
echo "   安装路径: $TARGET_DIR"
