#!/bin/bash
# 肌少症食养助手 - 安装脚本 (macOS / Linux)

set -e

SKILL_NAME="sarcopenia-food-guide"
SKILL_DIR="${HOME}/.workbuddy/skills/custom/${SKILL_NAME}"

echo "========================================="
echo "  肌少症食养助手 - 安装"
echo "========================================="
echo ""

# 创建目录
mkdir -p "${SKILL_DIR}"

# 复制文件
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cp "${SCRIPT_DIR}/skill.yaml" "${SKILL_DIR}/"
cp "${SCRIPT_DIR}/system_prompt.md" "${SKILL_DIR}/"
cp "${SCRIPT_DIR}/knowledge_base.md" "${SKILL_DIR}/"
cp "${SCRIPT_DIR}/recipes_data.md" "${SKILL_DIR}/"
cp "${SCRIPT_DIR}/recipes_overview.md" "${SKILL_DIR}/"

echo "✓ 文件已复制到 ${SKILL_DIR}"
echo ""
echo "安装完成！"
echo "使用方式：在对话中提及「肌少症」「肌肉流失」「食养」等关键词即可触发"
