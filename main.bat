@echo off

:: Start the mock API in the background
echo Starting mock API...
start /b cmd /c python mock_api.py

:: Pause briefly to ensure mock API starts
timeout /t 2 /nobreak >nul

:: Start the main script
echo Starting main script...
python main.py

:: Prevent the script from closing immediately
echo.
echo Scripts are running. Press any key to close this window.
pause >nul
