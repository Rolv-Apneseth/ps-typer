#!/bin/bash

# navigate our of bin directory
cd ..

# PATHS
CONTAINING_FOLDER=$(pwd)
ACTIVATE="$CONTAINING_FOLDER/bin/activate"
PYTHON3="$CONTAINING_FOLDER/bin/python3"
PYQT5="$CONTAINING_FOLDER/lib/python3.8/site-packages/PyQt5"
MAIN="$CONTAINING_FOLDER/speed-typer/main.py"

# SETUP
# Create venv if one does not exist. Also upgrades venv pip version
# In either case, activate venv
if [ ! -f "$PYTHON3" ]; then
    cd ..
    python3 -m venv speed-typer
    cd "$CONTAINING_FOLDER"

    echo .
    echo Virtual environment created
    echo .

    source "$ACTIVATE" && pip3 install --upgrade pip

    echo .
    echo Pip upgraded
    echo .
else
    source "$ACTIVATE"
fi

# Install requirements if they are not already installed
if [ ! -d "$PYQT5" ]; then
    pip3 install -r requirements.txt

    echo .
    echo Dependencies installed
    echo .
fi

# RUN PROGRAM
python3 "$MAIN"
