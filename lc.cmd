@echo off
chcp 65001>nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\lc_runner.ps1" %*
