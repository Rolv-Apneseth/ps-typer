echo off
@REM Navigate out of 'bin' directory
cd ..


@REM SETUP
@REM Create venv if one does not exist. Also upgrades venv pip version
if not exist .\Scripts\ (
    cd ..
    python -m venv speed-typer
    cd speed-typer

    echo .
    echo Virtual environment created
    echo .

    cmd /c ".\Scripts\activate.bat && pip install --upgrade pip"

    echo .
    echo Pip upgraded
    echo .
)

@REM Install requirements if they are not already installed
if not exist .\Lib\site-packages\PyQt5\ (
    cmd /c ".\Scripts\activate.bat && pip install -r requirements.txt"

    echo .
    echo Dependencies installed
    echo .
)

@REM RUN PROGRAM
@REM Run virtual environment and main.py
call .\Scripts\activate.bat && python speed-typer\main.py
