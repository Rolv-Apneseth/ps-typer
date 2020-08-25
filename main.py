from PyQt5 import QtCore, QtGui, QtWidgets
import time

from typeTest import TypeTest
import mainWindow
import easyWindow
import mediumWindow
import hardWindow
import scoreWindow


class Main(mainWindow.Ui_MainWindow):


    timer_start = 0
    type_test = TypeTest()

    def initial_highscores(self):
        self.today_highscore.setText("".join([str(self.type_test.get_today_highscore()), " wpm"]))
        self.all_time_highscore.setText("".join([str(self.type_test.get_highscore()), " wpm"]))


    #Window Functionality Functions
    def get_time(self):
        print(self.ui.timer_start)


    def onPressed(self):
        """Starts timer when editor is clicked"""

        self.timer_start = time.time()


    def easy_onTextChanged(self):
        """
        Will update the colour of the given word to red if one or all letters have been typed incorrectly, and green if everything is correct so far.
        Brings up the score pop up upon completion.
        """

        text1 = self.easy_ui.easy_label.text()
        text2 = self.easy_ui.easyLineEdit.text()

        if not self.type_test.check_text(text1, text2):
            self.easy_ui.easy_label.setStyleSheet("color: red;")
        else:
            self.easy_ui.easy_label.setStyleSheet("color: green;")

        if text1 == text2:
            words = self.type_test.get_words(text1)
            seconds = time.time() - self.timer_start
            wpm = str(self.type_test.wpm_calc(text1, seconds))

            self.easy_window.close()
            self.score_pop_up()
            self.score_ui.you_typed_label.setText(f"You typed {words} word(s) in {round(seconds)} second(s) and your score was {wpm} w.p.m.!")
            self.highscore(int(wpm))


    def medium_onTextChanged(self):
        """
        Will update the colour of the given phrase to red if one or all letters have been typed incorrectly, and green if everything is correct so far.
        Brings up the score pop up upon completion.
        """

        text1 = self.medium_ui.medium_label.text()
        text2 = self.medium_ui.mediumLineEdit.text()

        if not self.type_test.check_text(text1, text2):
            self.medium_ui.medium_label.setStyleSheet("color: red;")
        else:
            self.medium_ui.medium_label.setStyleSheet("color: green;")

        if text1 == text2:
            words = self.type_test.get_words(text1)
            seconds = time.time() - self.timer_start
            wpm = str(self.type_test.wpm_calc(text1, seconds))

            self.medium_window.close()
            self.score_pop_up()
            self.score_ui.you_typed_label.setText(f"You typed {words} word(s) in {round(seconds)} second(s) and your score was {wpm} w.p.m.!")
            self.highscore(int(wpm))


    def hard_onTextChanged(self):
        """
        Will update the colour of the given paragraph to red if one or all letters have been typed incorrectly, and green if everything is correct so far.
        Brings up the score pop up upon completion.
        """

        text1 = self.hard_ui.hard_label.toPlainText()
        text2 = self.hard_ui.hard_textEdit.toPlainText()

        if not self.type_test.check_text(text1, text2):
            self.hard_ui.hard_textEdit.setStyleSheet("color: red;")
        else:
            self.hard_ui.hard_textEdit.setStyleSheet("color: green;")

        if text1 == text2:
            words = self.type_test.get_words(text1)
            seconds = time.time() - self.timer_start
            wpm = str(self.type_test.wpm_calc(text1, seconds))

            self.hard_window.close()
            self.score_pop_up()
            self.score_ui.you_typed_label.setText(f"You typed {words} word(s) in {round(seconds)} second(s) and your score was {wpm} w.p.m.!")
            self.highscore(int(wpm))


    def easy_restart(self):
        """Resets the timer and gives a new word to be typed out"""

        self.easy_ui.easy_label.setText(self.type_test.easy_choice())
        self.timer_start = time.time()
        self.easy_ui.easyLineEdit.setText("")


    def medium_restart(self):
        """Resets the timer and gives a new phrase to be typed out"""

        self.medium_ui.medium_label.setText(self.type_test.medium_choice())
        self.timer_start = time.time()
        self.medium_ui.mediumLineEdit.setText("")


    def hard_restart(self):
        """Resets the timer and gives a new paragraph to be typed out"""

        self.hard_ui.hard_label.setText(self.type_test.hard_choice())
        self.timer_start = time.time()
        self.hard_ui.hard_textEdit.setText("")


    def ok_click(self):
        self.score_window.close()
        MainWindow.show()

    def highscore(self, wpm):
        if self.type_test.check_day_highscore(wpm):
            self.type_test.set_day_highscore(wpm)
            self.score_ui.outcome_label.setText("You set today's highscore!")
            self.today_highscore.setText("".join([str(wpm), " wpm"]))


            if self.type_test.check_highscore(wpm):
                self.type_test.set_highscore(wpm)
                self.score_ui.outcome_label.setText("You set an all time highscore!")
                self.all_time_highscore.setText("".join([str(wpm), " wpm"]))


    #Pop up Functions
    def score_pop_up(self):
        """Score window displayed after typing of any difficulty is completed"""

        self.score_window = QtWidgets.QMainWindow()
        self.score_ui = scoreWindow.Ui_scoreWindow()
        self.score_ui.setupUi(self.score_window)
        self.score_ui.ok_button.clicked.connect(lambda: self.ok_click())
        self.score_window.show()


    def easy_pop_up(self):
        """
        Easy difficulty pop up window.
        To be typed: one popular english word
        """

        self.easy_window = QtWidgets.QMainWindow()
        self.easy_ui = easyWindow.Ui_EasyWindow()
        self.easy_ui.setupUi(self.easy_window)
        self.easy_ui.easyLineEdit.mousePressedEvent = self.onPressed()
        self.easy_ui.easy_label.setText(self.type_test.easy_choice())
        self.easy_ui.easyLineEdit.textChanged.connect(self.easy_onTextChanged)
        self.easy_ui.easy_restart.clicked.connect(lambda: self.easy_restart())
        self.easy_window.show()


    def medium_pop_up(self):
        """
        Medium difficulty pop up window.
        To be typed: one popular english phrase or saying
        """

        self.medium_window = QtWidgets.QMainWindow()
        self.medium_ui = mediumWindow.Ui_MediumWindow()
        self.medium_ui.setupUi(self.medium_window)
        self.medium_ui.mediumLineEdit.mousePressedEvent = self.onPressed()
        self.medium_ui.medium_label.setText(self.type_test.medium_choice())
        self.medium_ui.mediumLineEdit.textChanged.connect(self.medium_onTextChanged)
        self.medium_ui.medium_restart.clicked.connect(lambda: self.medium_restart())
        self.medium_window.show()


    def hard_pop_up(self):
        """
        Hard difficulty pop up window.
        To be typed: a quote or paragraph from a book
        """
        self.hard_window = QtWidgets.QMainWindow()
        self.hard_ui = hardWindow.Ui_HardWindow()
        self.hard_ui.setupUi(self.hard_window)
        self.hard_ui.hard_textEdit.mousePressedEvent = self.onPressed()
        self.hard_ui.hard_label.setText(self.type_test.hard_choice())
        self.hard_ui.hard_textEdit.textChanged.connect(self.hard_onTextChanged)
        self.hard_ui.hard_restart.clicked.connect(self.hard_restart)
        self.hard_window.show()


    #Button Functions
    def begin(self, easy_chk, med_chk):
        """Uses pop up functions begin the typing test of the chosen difficulty."""

        MainWindow.hide()
        if easy_chk:
            self.easy_pop_up()
        elif med_chk:
            self.medium_pop_up()
        else:
            self.hard_pop_up()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    ui.initial_highscores()
    MainWindow.show()
    sys.exit(app.exec_())
