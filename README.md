# speed-typer

A program to test the speed at which you can type. Choose a mode, type out the text and be told your average w.p.m. and your accuracy. The program can also keep track of your daily and all-time highscores. Have a look at the statistics window after a couple of days and see on a graph how you're progressing in terms of wpm.

## What I learned

- Using issues, branches and pull requests to keep track of work on the project
- Building GUIs using PyQt5 and Qt Designer
- Making the GUI resizeable and configurable (for example light and dark modes are available)
- Intricate use of OOP to handle the different windows and functionality for each window
- Plotting data with pyqtgraph, and styling of the graph so it has the desired layout and appearance
- Using .pkl and .json files to save data and load it when the program is run, for saving of highscores and remembering user settings.
- Rich text manipulation so the text typed is coloured based on whether it is correct/incorrect

## Installation

1. Requires python 3.6+ to run. Python can be installed from [here](https://www.python.org/downloads/)
2. To download, click on 'Code' to the top right, then download as a zip file. You can unzip using your preferred program.
   - You can also clone the repository using: `git clone https://github.com/Rolv-Apneseth/speed-typer.git`
3. Install the requirements for the program.
   - In your terminal, navigate to the cloned directory and run: `python3 -m pip install -r requirements.txt`
4. To run the actual program, navigate further into the speed-typer folder and run: `python3 main.py`

Alternatively to steps 3 and 4, you can navigate to the bin folder and run one of the scripts included there, i.e. if you're on windows, double-click the `run_program.bat` file. This will create a virtual environment, install all required dependencies to that virtual environment, then run `main.py`. Note that this will of course take a while the first time it is run.

## Usage

1. Select a mode from the dropdown menu
2. Click on begin and start typing! Characters typed correctly are highlighted green and characters typed incorrectly are highlighted red.
3. When finished, a window will appear displaying your accuracy, average w.p.m and whether or not you set a daily or all-time highscore.
   - Note: The highscores are stored in the assets folder in highscores.pkl and backup_highscores.pkl and can be deleted if you want to reset your highscore.
     - There are however GUI options for resetting highscores in the Statistics window

## Modes

Select one of the following options to choose what you will be typing out:

- Common Phrases

- Facts

- Famous Novel Excerpts

- Famous Quotes

- Random Text Options
  - These 3 options are achieved using corpora from nltk, for which documentation can be found [here](https://www.nltk.org/book/ch02.html). The corpora included are:
  1.  Brown, which is the first million-word electronic corpus of English.
  2.  Gutenberg, which is a small selection of texts from the Project Gutenberg electronic text archive, which contains some 25,000 free electronic books, hosted [here](http://www.gutenberg.org/).
  3.  Webtext, a collection of web text includes content from a Firefox discussion forum, conversations overheard in New York, the movie script of Pirates of the Carribean, personal advertisements, and wine reviews, for more informal text.
  - To reduce the number of dependencies, as well as the processing that needs to be done for formatting the text, the corpora are already processed into plain text files stored in the `assets/texts/` directory, along with the python script used to generate them.

## W.P.M.

Your typing speed is measured by your average wpm, multiplied by your accuracy.

Wpm is calculated as words per minute (w.p.m) using `(characters typed/5)/minutes` This gives a more fair w.p.m calculation since longer words would be worth more than short words. This figure is then multiplied by your accuracy percentage.

Accuracy is taken into account to incentivise you to type all the text out correctly and not enforce bad habits.

## Statistics

Highscores can be set both daily or as an all-time highscore. Both values are displayed in the main menu and saved for future sessions.

The program will save all of your daily highscores. This data is then visualised in the statistics window using a graph of wpm over time so you can get a sense of how you're progressing.
