import os
import random
import time
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets


class TypeTest:
    today = datetime.today()
    date = "".join([str(today.day), "/", str(today.month), "/", str(today.year)])

    def __init__(self):
        """Creates Highscore files and gives them default values if the do not exist and assigns path variables to every file used."""
        self.FOLDER = os.path.dirname(os.path.abspath(__file__))

        self.t_path = os.path.join(self.FOLDER, "today.txt")
        self.h_path = os.path.join(self.FOLDER, "highscore.txt")

        self.easy_path = os.path.join(self.FOLDER, "Easy.txt")
        self.med_path = os.path.join(self.FOLDER, "Medium.txt")
        self.hard_path = os.path.join(self.FOLDER, "Hard.txt")

        if not os.path.exists(self.t_path):
            with open(self.t_path, "w") as today_txt:
                today_txt.write("".join([self.date, " : 0"]))

        if not os.path.exists(self.h_path):
            with open(self.h_path, "w") as highscore_txt:
                highscore_txt.write("0")

    def easy_choice(self):
        """Returns a random common word"""

        with open(self.easy_path, "r") as easy:
            lines = easy.readlines()

        return random.choice(lines).replace("\n", "")

    def medium_choice(self):
        """Returns a random common phrase"""

        with open(self.med_path, "r") as med:
            lines = med.readlines()

        return random.choice(lines).replace("\n", "")

    def hard_choice(self):
        """Returns a random paragraph from a book or a quote (in one line)"""

        with open(self.hard_path, "r") as hard:
            lines = hard.readlines()

        return (random.choice(lines)).replace("\n", "")

    def check_text(self, text1, text2):
        return text1.startswith(text2)

    def get_words(self, text):
        return len(text.split())

    def wpm_calc(self, text, seconds):
        minutes = seconds / 60
        entries = len(text)

        return round((entries / 5) / minutes)

    def get_today_highscore(self):
        with open(self.t_path, "r") as today_text:
            today_highscore_line = today_text.readlines()[-1]
        if today_highscore_line.startswith(self.date):
            today_highscore = int(today_highscore_line.split()[-1])
        else:
            today_highscore = 0

        return today_highscore

    def check_day_highscore(self, wpm):
        return self.get_today_highscore() < wpm

    def get_highscore(self):
        with open(self.h_path, "r") as highscore_text:
            highscore = int(highscore_text.read())
        return highscore

    def check_highscore(self, wpm):
        return self.get_highscore() < wpm

    def set_day_highscore(self, wpm):
        with open(self.t_path, "a") as today_text:
            today_text.write("".join(["\n", self.date, " : ", str(wpm)]))

    def set_highscore(self, wpm):
        with open(self.h_path, "w") as highscore_text:
            highscore_text.write(str(wpm))


if __name__ == "__main__":
    test = TypeTest()
    test.easy_choice()
    text = test.hard_choice()
    print(text)
    print(test.wpm_calc(text, 120))
    print(test.get_words(text))
    print(test.date)
    print(test.check_highscore(12))
    print(test.check_highscore(1))
