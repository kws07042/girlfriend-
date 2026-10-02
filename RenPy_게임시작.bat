@echo off
chcp 65001 >nul
cd /d "%~dp0"
"도구\renpy-8.5.3-sdk\renpy.exe" "%~dp0RenPy_게임"
