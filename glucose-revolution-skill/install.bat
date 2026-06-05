@echo off
chcp 65001 >nul

:: 控糖革命 Skill 安装脚本 (Windows)
:: Glucose Revolution Skill Installer for Windows

echo ======================================
echo  控糖革命 Skill 安装器
echo  Glucose Revolution Skill Installer
echo ======================================
echo.

set "SKILL_NAME=glucose-revolution"
set "SKILL_DIR=%~dp0"

:: 检测常见安装路径
set "INSTALL_PATH="

if exist "%USERPROFILE%\.workbuddy\skills\custom" (
    set "INSTALL_PATH=%USERPROFILE%\.workbuddy\skills\custom"
    set "PLATFORM=WorkBuddy"
) else if exist "%USERPROFILE%\.lingtai\custom" (
    set "INSTALL_PATH=%USERPROFILE%\.lingtai\custom"
    set "PLATFORM=Lingtai TUI"
)

if "%INSTALL_PATH%"=="" (
    echo ⚠️ 未检测到 WorkBuddy 或灵台 TUI 安装目录
    echo.
    echo 请手动指定安装路径:
    echo 例如: C:\Users\你的用户名\.workbuddy\skills\custom
    set /p "INSTALL_PATH=请输入路径: "
    set "PLATFORM=Custom"
)

echo ✓ 检测到平台: %PLATFORM%
echo ✓ 安装路径: %INSTALL_PATH%
echo.

:: 检查是否已存在
if exist "%INSTALL_PATH%\%SKILL_NAME%" (
    echo ⚠️ 检测到已存在 %SKILL_NAME% Skill
    set /p "overwrite=是否覆盖? [y/N]: "
    if /i not "%overwrite%"=="y" (
        echo 已取消安装
        pause
        exit /b 0
    )
    rmdir /s /q "%INSTALL_PATH%\%SKILL_NAME%"
)

:: 复制文件
echo 正在安装...
if not exist "%INSTALL_PATH%" mkdir "%INSTALL_PATH%"
xcopy /s /e /i "%SKILL_DIR%" "%INSTALL_PATH%\%SKILL_NAME%" /exclude:%~nx0 >nul 2>&1

echo.
echo ======================================
echo  ✅ 安装成功!
echo ======================================
echo.
echo Skill名称: %SKILL_NAME%
echo 安装位置: %INSTALL_PATH%\%SKILL_NAME%
echo.
echo 触发关键词:
echo   - 控糖
echo   - 血糖
echo   - 饮食顺序
echo   - 胰岛素
echo   - ...以及任何血糖相关问题
echo.
echo 快速开始:
echo   1. 重启你的 AI 助手
echo   2. 输入"控糖"或"帮我管理血糖"激活 Skill
echo   3. 输入"控糖自测"开始症状评估
echo.
pause
