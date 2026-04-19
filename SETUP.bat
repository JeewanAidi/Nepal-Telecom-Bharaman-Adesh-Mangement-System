@echo off
title Nepal Telecom Travel Management - Setup
color 1F
echo.
echo ================================================
echo   Nepal Telecom Travel Management System
echo   Mahendranagar Branch - Setup Script
echo ================================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.10+ from https://python.org
    pause
    exit /b 1
)

echo [1/6] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment.
    pause
    exit /b 1
)

echo [2/6] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/6] Installing required packages...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo [ERROR] Failed to install packages.
    pause
    exit /b 1
)

echo [4/6] Running database migrations...
python manage.py makemigrations
python manage.py migrate
if errorlevel 1 (
    echo [ERROR] Migration failed.
    pause
    exit /b 1
)

echo [5/6] Seeding initial data (admin user + sample employees)...
python manage.py seed_data

echo [6/6] Setup complete!
echo.
echo ================================================
echo   SETUP SUCCESSFUL!
echo ================================================
echo.
echo   Login Credentials:
echo     URL      : http://127.0.0.1:8000/login/
echo     Username : admin
echo     Password : admin123
echo.
echo   Starting server now...
echo   Press Ctrl+C to stop the server.
echo ================================================
echo.

python manage.py runserver

pause
