@echo off

:: Start the mock API in a new terminal window
echo Starting mock API...
start cmd /k python mock_api.py

:: Start the main script in a new terminal window
echo Starting main script...
start cmd /k python main.py

:: Prevent the script from closing immediately
echo.
echo Scripts are running. Press any key to close this window.
pause >nul
