@echo off
echo Running backend tests...
cd /d "%~dp0"
python run_tests.py
pause
