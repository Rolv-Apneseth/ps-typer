from PyQt5 import QtCore, QtWidgets

import type_test
from source_ui import main_window
from assets import highscores, settings


class MainWindow(QtWidgets.QWidget, main_window.Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Multiple inheritance allows us to have the ui and window together so
        # setupui can be given self in for a window
        self.setupUi(self)

        self.buttonStart.clicked.connect(self.on_clicked_start)

        # Initialize highscores handler
        self.highscore = highscores.Highscores()
        self.update_highscores()

    # Button Functions
    def on_clicked_start(self):
        self.make_mode_window(str(self.comboBoxSelectMode.currentText()))

        self.mode_window.show()

        self.hide()

    def on_clicked_main_menu(self):
        self.update_highscores()
        self.show()

        self.mode_window.close()
        del self.mode_window

    # Helper Functions
    def make_mode_window(self, mode):
        self.mode_window = type_test.TypingWindow()
        self.mode_window.set_mode(mode)

        self.mode_window.buttonMainMenu.clicked.connect(self.on_clicked_main_menu)

    def update_highscores(self):
        self.highscore.load_data()
        self.today_wpm, self.all_time_wpm = self.highscore.get_wpm()

        self.labelTodayScore.setText(f"{self.today_wpm} WPM")
        self.labelAlltimeScore.setText(f"{self.all_time_wpm} WPM")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
