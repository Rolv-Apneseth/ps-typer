from PyQt5 import QtCore, QtWidgets
from time import perf_counter

from source_ui import typing_window
from assets import texts, results, highscores


# Constants
GREEN = "rgb(0, 75, 0)"
RED = "rgb(125, 0, 0)"


class TypingWindow(QtWidgets.QWidget, typing_window.Ui_typingWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Multiple inheritance allows us to have the ui and window together so
        # setupui can be given self in for a window
        self.setupUi(self)

        self.lineInput.textChanged.connect(self.on_input_text_changed)
        self.buttonNewText.clicked.connect(self.on_clicked_new)

        # timer
        self.start_time = None

        # Object to handle saving and updating of highscore values
        self.highscore = highscores.Highscores()

    # Helper Functions
    def set_mode(self, mode):
        self.mode = mode

        if mode == "Common Phrases":
            self.labelMainText.setAlignment(QtCore.Qt.AlignCenter)

        self.text = texts._translate[mode]()
        self.labelMainText.setText(self.text)

    def set_stats(self, input_text):
        correct = 0
        for i, character in enumerate(input_text):
            if character == self.text[i]:
                correct += 1

        self.accuracy = int(correct / len(self.text) * 100)

        seconds = perf_counter() - self.start_time
        self.wpm = int((len(self.text) / 5) / (seconds / 60))

    def display_highscore_result(self):
        _translate_result = {
            "all-time": "New all-time highscore set! Congratulations!",
            "daily": "New daily highscore set! Good job!",
            "none": "No new highscore set. Don't give up!",
        }

        self.highscore_result = self.highscore.update(self.wpm)
        self.results_window.labelHighscoreSet.setText(
            _translate_result[self.highscore_result]
        )

    def make_results_window(self):
        self.results_window = results.ResultsWindow()

        self.results_window.labelAccuracy.setText(f"Accuracy: {str(self.accuracy)}%")
        self.results_window.labelSpeed.setText(f"Speed:    {str(self.wpm)}wpm!")
        self.display_highscore_result()

        self.results_window.buttonNext.clicked.connect(self.on_clicked_next)

        # Apply same functionality as for the self.buttonMainMenu, which
        # is set in main.py
        self.results_window.buttonMainMenu.clicked.connect(self.buttonMainMenu.click)

    def on_finished(self, input_text):
        self.set_stats(input_text)

        self.make_results_window()

        self.hide()
        self.results_window.show()

    # Button Functions
    def on_clicked_restart(self):
        self.start_time = None
        self.lineInput.clear()

    def on_clicked_new(self):
        self.on_clicked_restart()
        self.set_mode(self.mode)

    def on_clicked_next(self):
        self.show()
        self.on_clicked_new()

        self.results_window.close()
        del self.results_window

    def on_input_text_changed(self, input_text: str) -> None:
        """Updates background of each letter as user types and calls a function when
        the user is finished.
        """
        if not self.start_time:
            self.start_time = perf_counter()

        typed_text = []
        rest_of_text = self.text[len(input_text) :]

        for i, character in enumerate(input_text):
            if self.text[i] == character:
                typed_text.append(
                    f'<span style="background-color:{GREEN};">{self.text[i]}</span>'
                )
            else:
                typed_text.append(
                    f'<span style="background-color:{RED};">{self.text[i]}</span>'
                )

        rich_text = (
            "<html><head/><body><p>"
            f'{"".join(typed_text)}'
            f"{rest_of_text}</p></body></html>"
        )
        self.labelMainText.setText(rich_text)

        if len(input_text) == len(self.text):
            self.on_finished(input_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = TypingWindow()
    window.show()

    app.exec_()