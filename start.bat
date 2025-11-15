@echo off

cd /d %~dp0

choice /c YN /m "Install Dependancies? (Y/N)"

if %ERRORLEVEL%==1 (
    echo Installing Dependancies...
    pip install -r requirements.txt
)
echo Starting...

python main.py

pause

