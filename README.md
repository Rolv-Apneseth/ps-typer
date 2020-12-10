# speed-typer

A program to test the speed at which you can type. Choose a mode, type out the text and be told your average w.p.m. and your accuracy. The program can also keep track of your daily and all-time highscores.

## What I learned

- Building GUI's using PyQt5 and Qt Designer
- Making the GUI resizeable
- Pickling of data to save, load and set new highscores
- Use of OOP to handle the use of different windows and functionality
- Use of the time module to time actions/functions
- Rich text manipulation so the text typed is coloured

## Installation

1. Requires python 3.6+ to run. Python can be installed from [here](https://www.python.org/downloads/)
2. To download, click on 'Code' to the top right, then download as a zip file. You can unzip using your preferred program.
   - You can also clone the repository using: `git clone https://github.com/Rolv-Apneseth/speed-typer.git`
3. Install the requirements for the program.
   - In your terminal, navigate to the cloned directory and run: `python3 -m pip install -r requirements.txt`
4. To run the actual program, navigate further into the speed-typer folder and run: `python3 main.py`

## Usage

1. Select a mode from the dropdown menu
2. Click on begin and start typing! Characters typed correctly are highlighted green and characters typed incorrectly are highlighted red.
3. When finished, a window will appear displaying your accuracy, average w.p.m and whether or not you set a daily or all-time highscore.
   - Note: The highscores are stored in the assets folder in data.pkl and backup_data.pkl and can be deleted if you want to reset your highscore.
     - Please take care not to delete other files in the assets folder as they are required for the program to function.

## Modes

Select one of the following options to choose what you will be typing out:

- Common Phrases

- Facts

- Famous Novel Excerpts

- Famous Quotes

- Randomly Generated Text
  - This is generated using nltk.corpus.brown which is the first million-word electronic corpus of English. A snippet of this corpus is chosen at random each time. [Source](https://www.nltk.org/book/ch02.html)

## W.P.M.

Your typing speed is measured by your average wpm. Wpm is calculated as words per minute (w.p.m) using `(characters typed/5)/minutes` This gives a more fair w.p.m calculation since longer words would be worth more than short words.

Highscores can be set both daily or as an all-time highscore. Both values are displayed in the main menu and saved for future sessions.
