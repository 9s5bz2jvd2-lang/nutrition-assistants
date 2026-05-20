@echo off
REM 肌少症食养助手 - 安装脚本 (Windows)

setlocal enabledelayedexpansion

set SKILL_NAME=sarcopenia-food-guide
set SKILL_DIR=%USERPROFILE%\.workbuddy\skills\custom\%SKILL_NAME%

echo =========================================
echo   肌少症食养助手 - 安装
echo =========================================
echo.

REM 创建目录
if not exist "%SKILL_DIR%" mkdir "%SKILL_DIR%"

REM 复制文件
copy "%~dp0skill.yaml" "%SKILL_DIR%\"
copy "%~dp0system_prompt.md" "%SKILL_DIR%\"
copy "%~dp0knowledge_base.md" "%SKILL_DIR%\"
copy "%~dp0recipes_data.md" "%SKILL_DIR%\"
copy "%~dp0recipes_overview.md" "%SKILL_DIR%\"

echo.
echo [OK] 文件已复制到 %SKILL_DIR%
echo.
echo 安装完成！
echo 使用方式：在对话中提及「肌少症」「肌肉流失」「食养」等关键词即可触发

pause
