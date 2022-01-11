#!/bin/bash
# ------------------------------------------------------------------
# Author:
#   Rolv Apneseth <rolv.apneseth@gmail.com>
# 
# Description:
#   This is a script used to:
#       1. Initialise a virtual environment for PS Typer using
#          venv
#       2. Install any dependencies PS Typer needs into this
#          virtual environment
#       3. Launch the program with the virtual environment
#
#   Note that environment and dependencies set up will only happen
#   if certain files are not found so effectively it will only
#   install dependencies once and won't try to do so on every 
#   launch. 
# ------------------------------------------------------------------


# PATHS
# This extremely useful one-liner was found here: https://stackoverflow.com/a/246128/14316282
# Note that this will not work with symlinks
BIN_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PYTHON3="$BIN_FOLDER/python3"

CONTAINING_FOLDER="$(dirname "$BIN_FOLDER")"
REQUIREMENTS="$CONTAINING_FOLDER/requirements.txt"
MAIN="$CONTAINING_FOLDER/ps-typer/main.py"

# SETUP
# Create venv if one does not exist. Also upgrades venv pip version
if [ ! -f "$PYTHON3" ]; then
    python3 -m venv "$CONTAINING_FOLDER"
    printf "\nVirtual environment created\n\n"

    "$PYTHON3" -m pip install --upgrade pip
    printf "\nPip upgraded\n"
fi

# Install requirements if they are not already installed
if ! "$PYTHON3" -m pip list | grep "PyQt5"; then
    "$PYTHON3" -m pip install -r "$REQUIREMENTS"
    printf "\nDependencies installed\n"
fi

# RUN PROGRAM
"$PYTHON3" "$MAIN"
