@echo off
rem Double-click to start AAI Lab. Keep this window open while you use the app.
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start_lab.ps1" %*
if errorlevel 1 pause
