:: Clear console the terminal to good look 
@echo off 

:: Checking python version 
python --version 2>NUL 

if errorlevel 1 goto errorNoPython

:: make virtual environtment 
python -m venv venv

Call "%cd%/venv/Scripts/activate"

@REM :: Installing python environtment 
pip install -r "%cd%/document/requirements.txt"

:: Wait to typing anything 
Pause 
goto eof

:: checkking is errorNoPython 
:errorNoPython 
echo. 
echo error^ = Python 3.8.10 is not found 
Pause

