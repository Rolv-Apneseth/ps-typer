# ps-typer

![Linux](https://img.shields.io/badge/-Linux-grey?logo=linux)
![OSX](https://img.shields.io/badge/-OSX-black?logo=apple)
![Windows](https://img.shields.io/badge/-Windows-blue?logo=windows)
![Python](https://img.shields.io/badge/Python-v3.9%5E-green?logo=python)
![Version](https://img.shields.io/github/v/tag/rolv-apneseth/ps-typer?label=version)
[![PyPi](https://img.shields.io/pypi/v/ps-typer?label=pypi)](https://pypi.org/project/ps-typer/)
![Black](https://img.shields.io/badge/code%20style-black-000000.svg)

![PS-Typer demo](https://user-images.githubusercontent.com/69486699/161395389-247c75fd-c2b6-4a63-bf03-258c5046b1be.png)

## Description

A Python program built on the PyQt5 GUI framework, used for practicing your typing skills and keeping track of your progress.

## Index

-   [Dependencies](#dependencies)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Modes](#modes)
-   [W.P.M.](#wpm)
-   [Statistics](#statistics)
-   [License](#license)

## Dependencies

-   [Python3](https://www.python.org/downloads/) (v3.9 or later)
    -   [DateTime](https://pypi.org/project/DateTime/)
    -   [PyQt5](https://pypi.org/project/PyQt5/)
    -   [PyQtGraph](https://pypi.org/project/pyqtgraph/)

## Installation

Using `pip` (if you're on Windows, replace `python3` with just `python` down below):

```bash
python3 -m pip install ps-typer
```

Then, launch the program by running the command:

```bash
ps-typer
```

Note that if the command does not work you may need to configure your system `PATH` variable (check out some Stack Overflow answers linked below).

-   [Windows](https://stackoverflow.com/a/36160069/14316282)
-   [Linux or Mac](https://stackoverflow.com/a/62823029/14316282)

## Usage

1. Select a [mode](#modes) from the dropdown menu (My recommendation is always `Random Text: Brown`)
2. Click on begin and start typing! Characters typed correctly are highlighted green and characters typed incorrectly are highlighted red.
3. When finished, a window will appear displaying your accuracy, average w.p.m and whether or not you set a daily or all-time high score.
4. Check out the [Statistics](#statistics) section below

## Modes

Select one of the following options to choose what you will be typing out:

-   Common Phrases

-   Facts

-   Famous Literature Excerpts

-   Famous Quotes

-   Random Text Options
    -   These 3 options are achieved using corpora from nltk, for which documentation can be found [here](https://www.nltk.org/book/ch02.html). The corpora included are:
    1.  Brown, which is the first million-word electronic corpus of English.
    2.  Gutenberg, which is a small selection of texts from the Project Gutenberg electronic text archive, which contains some 25,000 free electronic books, hosted [here](http://www.gutenberg.org/).
    3.  Webtext, a collection of web text includes content from a Firefox discussion forum, conversations overheard in New York, the movie script of Pirates of the Carribean, personal advertisements, and wine reviews, for more informal text.
    -   To reduce the number of dependencies, as well as the processing that needs to be done for formatting the text, the corpora are already processed into plain text files stored in the `assets/texts/` directory, along with the python script used to generate them.

## W.P.M.

Your typing speed is measured by your average wpm, multiplied by your accuracy.

Wpm is calculated as words per minute (w.p.m) using `(characters typed/5)/minutes` This gives a more fair w.p.m calculation since longer words would be worth more than short words. This figure is then multiplied by your accuracy percentage.

Accuracy is taken into account to incentivise you to type all the text out correctly and not enforce bad habits.

## Statistics

The program will save all of your daily high scores and keep track of your all-time highscore. This data is then visualised in the `Statistics` window using a graph of wpm over time so you can get a sense of how you're progressing.

From here you can also reset your highscores if you so wish.

**Please note:** All the (very limited) data this program stores can be found in the `ps_typer/data/` directory

## License

[MIT](https://github.com/Rolv-Apneseth/ps-typer/blob/master/LICENSE)
