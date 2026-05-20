@echo off
chcp 65001 >nul
setlocal

set "SCRIPT_DIR=%~dp0"
set "TARGET_DIR=%USERPROFILE%\.workbuddy\skills\custom\osteoporosis-food-guide-skill"

if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"

copy "%SCRIPT_DIR%skill.yaml" "%TARGET_DIR%\" >nul
copy "%SCRIPT_DIR%system_prompt.md" "%TARGET_DIR%\" >nul
copy "%SCRIPT_DIR%knowledge_base.md" "%TARGET_DIR%\" >nul
if exist "%SCRIPT_DIR%recipes_data.md" copy "%SCRIPT_DIR%recipes_data.md" "%TARGET_DIR%\" >nul
if exist "%SCRIPT_DIR%recipes_overview.md" copy "%SCRIPT_DIR%recipes_overview.md" "%TARGET_DIR%\" >nul

echo ✅ 骨质疏松症食养助手安装完成！
echo    安装路径: %TARGET_DIR%
pause
