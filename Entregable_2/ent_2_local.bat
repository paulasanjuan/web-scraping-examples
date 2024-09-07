@echo off
REM Set the current working directory to the directory containing the batch script
cd /d "%~dp0"
REM Set up the virtual environment
python -m venv venv
call venv\Scripts\activate.bat
REM Install dependencies
pip install -r requirements.txt
REM Run the Python script
echo Executing command: python ent_2_local.py
python ent_2_local.py > output.log 2>&1
REM Display a message indicating the script has finished
echo Script execution completed. Please check output.log for any errors.
pause
