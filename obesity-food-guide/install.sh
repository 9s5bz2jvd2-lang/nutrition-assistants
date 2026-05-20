#!/bin/bash
# Install script for Stunting Food Guide Skill
# Usage: bash install.sh

SKILL_DIR="$HOME/.workbuddy/skills/custom/stunting-dietary-guide-skill"

mkdir -p "$SKILL_DIR"

cp skill.yaml "$SKILL_DIR/"
cp SKILL.md "$SKILL_DIR/"
cp system_prompt.md "$SKILL_DIR/"
cp knowledge_base.md "$SKILL_DIR/"
cp recipes_data.md "$SKILL_DIR/"
cp recipes_overview.md "$SKILL_DIR/"
cp dietary_formulas.md "$SKILL_DIR/"

echo "Stunting Food Guide Skill installed to: $SKILL_DIR"
