@echo off
REM Install script for Child Obesity Food Guide Skill
set SKILL_DIR=%USERPROFILE%\.workbuddy\skills\custom\child-obesity-food-guide-skill
if not exist "%SKILL_DIR%" mkdir "%SKILL_DIR%"
copy /Y skill.yaml "%SKILL_DIR%\" >nul
copy /Y SKILL.md "%SKILL_DIR%\" >nul
copy /Y system_prompt.md "%SKILL_DIR%\" >nul
copy /Y knowledge_base.md "%SKILL_DIR%\" >nul
copy /Y recipes_data.md "%SKILL_DIR%\" >nul
copy /Y dietary_formulas.md "%SKILL_DIR%\" >nul
echo Child Obesity Food Guide Skill installed to: %SKILL_DIR%
pause
