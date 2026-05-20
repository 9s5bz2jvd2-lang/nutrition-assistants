#!/bin/bash
# 脑卒中食养助手 - 安装脚本 (macOS / Linux)

set -e

SKILL_NAME="stroke-food-guide"
SKILL_DIR="${HOME}/.workbuddy/skills/custom/${SKILL_NAME}"

echo "========================================="
echo "  脑卒中食养助手 - 安装"
echo "========================================="
echo ""

mkdir -p "${SKILL_DIR}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cp "${SCRIPT_DIR}/skill.yaml" "${SKILL_DIR}/"
cp "${SCRIPT_DIR}/system_prompt.md" "${SKILL_DIR}/"
cp "${SCRIPT_DIR}/knowledge_base.md" "${SKILL_DIR}/"
[ -f "${SCRIPT_DIR}/recipes_data.md" ] && cp "${SCRIPT_DIR}/recipes_data.md" "${SKILL_DIR}/"

echo "✓ 文件已复制到 ${SKILL_DIR}"
echo ""
echo "安装完成！"
echo "使用方式：在对话中提及「脑卒中」「中风」「卒中」等关键词即可触发"
