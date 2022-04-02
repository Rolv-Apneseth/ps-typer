# ps-typer

![PS-Typer](https://user-images.githubusercontent.com/69486699/161395389-247c75fd-c2b6-4a63-bf03-258c5046b1be.png)


## Description

A Python program built on the PyQt5 GUI framework, used for practicing your typing skills and keeping track of your progress.

## Index

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Modes](#modes)
- [W.P.M.](#wpm)
- [Statistics](#statistics)
- [License](#license)

## Dependencies

- [Python3](https://www.python.org/downloads/) (v3.6 or later)
- All Python packages required are listed in `requirements.txt` and are installed automatically with the default installation process (including [PyQt5](https://pypi.org/project/PyQt5/) and [PyQtGraph](https://pypi.org/project/pyqtgraph/))

## Installation

To download this program, click on `Code` at the top right of this page, then download as a zip file. You can unzip using your preferred program.

Alternatively, clone the repository using `git`:

```bash
git clone https://github.com/Rolv-Apneseth/ps-typer.git
```

### Linux

Navigate to the project's home directory and run the command:

```bash
sudo make install
```

- This will place a script for easy launching at `/usr/local/ps-typer`

To launch the program, run the command:

```bash
ps-typer
```

- This runs the `run_program.sh` script (located in the `bin` directory) which will create a virtual envirionment, install all required Python packages and then launch the program.

### Windows

Navigate to the project's `bin` directory and double click on `run_program.bat`

- This will create a virtual envirionment, install all required Python packages and then launch the program.

### Manual

Navigate to the project's home directory and run the command:

```bash
python3 -m pip install -r requirements.txt
```

To launch the program, navigate into the `ps-typer` directory and run the command:

```bash
python3 main.py
```

Windows users, replace `python3` with just `python` in the above commands

## Usage

1. Select a mode from the dropdown menu (Default on first start is Common Phrases)
2. Click on begin and start typing! Characters typed correctly are highlighted green and characters typed incorrectly are highlighted red.
3. When finished, a window will appear displaying your accuracy, average w.p.m and whether or not you set a daily or all-time high score.
   - Note: The high scores are stored in the assets folder in `highscores.pkl` and `backup_highscores.pkl` and can be deleted if you want to reset your high score.
     - There are however GUI options for resetting high scores in the Statistics window

## Modes

Select one of the following options to choose what you will be typing out:

- Common Phrases

- Facts

- Famous Literature Excerpts

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

High scores can be set both daily or as an all-time high score. Both values are displayed in the main menu and saved for future sessions.

The program will save all of your daily high scores. This data is then visualised in the statistics window using a graph of wpm over time so you can get a sense of how you're progressing.

## License

[MIT](https://github.com/Rolv-Apneseth/ps-typer/blob/master/LICENSE)
