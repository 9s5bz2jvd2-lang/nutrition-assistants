@echo off
REM Install script for Hyperlipidemia Food Guide Skill
REM Usage: install.bat

set SKILL_DIR=%USERPROFILE%\.workbuddy\skills\custom\hyperlipidemia-food-guide-skill

REM Create directory
if not exist "%SKILL_DIR%" mkdir "%SKILL_DIR%"

REM Copy files
copy /Y skill.yaml "%SKILL_DIR%\" >nul
copy /Y SKILL.md "%SKILL_DIR%\" >nul
copy /Y system_prompt.md "%SKILL_DIR%\" >nul
copy /Y knowledge_base.md "%SKILL_DIR%\" >nul
copy /Y recipes_data.md "%SKILL_DIR%\" >nul
copy /Y recipes_overview.md "%SKILL_DIR%\" >nul
copy /Y dietary_formulas.md "%SKILL_DIR%\" >nul

echo Hyperlipidemia Food Guide Skill installed to: %SKILL_DIR%
pause
