@echo off
REM 脑卒中食养助手 - 安装脚本 (Windows)

setlocal enabledelayedexpansion

set SKILL_NAME=stroke-food-guide
set SKILL_DIR=%USERPROFILE%\.workbuddy\skills\custom\%SKILL_NAME%

echo =========================================
echo   脑卒中食养助手 - 安装
echo =========================================
echo.

if not exist "%SKILL_DIR%" mkdir "%SKILL_DIR%"

copy "%~dp0skill.yaml" "%SKILL_DIR%\"
copy "%~dp0system_prompt.md" "%SKILL_DIR%\"
copy "%~dp0knowledge_base.md" "%SKILL_DIR%\"
if exist "%~dp0recipes_data.md" copy "%~dp0recipes_data.md" "%SKILL_DIR%\"

echo.
echo [OK] 文件已复制到 %SKILL_DIR%
echo.
echo 安装完成！
echo 使用方式：在对话中提及「脑卒中」「中风」「卒中」等关键词即可触发

pause
