@echo off
title NTC Travel Management - Server
color 1F
echo.
echo ================================================
echo   Nepal Telecom Travel Management System
echo   Starting Development Server...
echo ================================================
echo.
echo   URL: http://127.0.0.1:8000/
echo   Press Ctrl+C to stop.
echo ================================================
echo.

call venv\Scripts\activate.bat
python manage.py runserver

pause
