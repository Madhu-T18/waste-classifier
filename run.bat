@echo off
echo.
echo  ==============================
echo   WasteWise - Starting App...
echo  ==============================
echo.

:: Start FastAPI backend
echo  Starting FastAPI Backend...
start cmd /k "cd /d C:\Users\Admin\Desktop\waste classifier\api && uvicorn main:app --reload"

:: Wait 3 seconds for API to start
timeout /t 3 /nobreak > nul

:: Open frontend in browser
echo  Opening Frontend...
start "" "C:\Users\Admin\Desktop\waste classifier\frontend\index.html"

echo.
echo  App is running!
echo  API: http://127.0.0.1:8000
echo  Frontend: opened in browser
echo.
pause
```

