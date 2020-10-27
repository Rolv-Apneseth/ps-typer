# speed-typer

A program to test the speed at which you can type. Choose a difficulty, type out the word, sentence or paragraph and be told how long you took to do it and your average w.p.m. The program can also keep track of your daily and lifetime highscores.

## What I learned

- Building GUI's using PyQt5 and Qt Designer
- File i/o, both to get text for the user to write and to save highscores
- Use of OOP
- Use of the time module to time actions/functions

## Installation

1. Requires python 3.6+ to run. Python can be installed from [here](https://www.python.org/downloads/)
2. To download, click on 'Code' to the top right, then download as a zip file. You can unzip using your preferred program.
   - You can also clone the repository using: `git clone https://github.com/Rolv-Apneseth/speed-typer.git`
3. Install the requirements for the program.
   - In your terminal, navigate to the cloned directory and run: `python3 -m pip install -r requirements.txt`
4. To run the actual program, navigate further into the speed-typer folder and run: `python3 main.py`

## Usage

1. Select a difficulty by clicking on it's respective radio button
2. Click on begin test
3. Depending on your selection of difficulty, you will be shown:
   - Easy: A commonly used English word
   - Medium: A commonly used English phrase/expression
   - Hard: A paragraph from a book or a famous quote (high degree of variation in length)
4. Type out the word/phrase/paragraph. Your text will remain green while all characters are correct and turn red when you type a wrong character.
   - If you want a different word/phrase/paragraph, simply click the restart button. This will also restart your timer so don't worry
5. When finished, a window will come up and tell you whether you have set a new daily/all time highscore. These highscores are then displayed on the main window
   - Note: The highscores are stored in the assets folder in today.txt and highscore.txt (generated on startup if they don't exist) and can be deleted if you want to reset your highscore (or look at a record of your daily highscores).
     - Please take care not to delete the other text files as they hold the text that you are asked to type out so the program will not work without them

Scores are calculated as words per minute (w.p.m) using `(characters typed/5)/minutes` This gives a more fair w.p.m calculation since longer words would be worth more than short words. This also means, however, that it would still be hard to get high w.p.m scores on easy and medium difficulties.
