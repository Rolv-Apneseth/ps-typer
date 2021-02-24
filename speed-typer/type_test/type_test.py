from PyQt5 import QtCore, QtWidgets
from time import perf_counter
from typing import List

from source_ui import typing_window
from type_test import texts, results, highscores

# Constants
DEFAULT_COLOURS = ["rgb(0, 100, 0)", "rgb(100, 0, 0)"]
_TRANSLATE_RESULT = {
    "all-time": "New all-time highscore set! Congratulations!",
    "daily": "New daily highscore set! Good job!",
    "none": "No new highscore set. Don't give up!",
}


class TypingWindow(QtWidgets.QWidget, typing_window.Ui_typingWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Multiple inheritance allows us to have the ui and window together so
        # setupui can be given self in for a window
        self.setupUi(self)

        self.lineInput.textChanged.connect(self.on_input_text_changed)
        self.buttonNewText.clicked.connect(self.on_clicked_new)
        self.buttonRestart.clicked.connect(self.on_clicked_restart)

        # time and timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.setInterval(100)
        self.reset_time()

        # Object to handle saving and updating of highscore values
        self.highscore = highscores.Highscores()

        # Defaults
        self.key_sound = None
        self.set_colours(DEFAULT_COLOURS)

    # Helper Methods
    def set_mode(self, mode):
        self.mode = mode

        self.labelTitle.setText(mode)

        if mode == "Common Phrases":
            self.labelMainText.setAlignment(QtCore.Qt.AlignCenter)

        self.text_generator = texts._translate[mode]()
        self.set_main_text()

    def set_colours(self, colours: List[str]) -> None:
        """
        Sets the colours to be used for rich text formatting.

        Dictionary provided should be in the order:
            [green_colour, red_colour]
        """

        self.colours = colours

    def set_main_text(self):
        """
        Sets the text to be typed out by the user by getting a value
        from self.text_generator.

        If the list of strings from self.text_generator is already
        exhausted, a default warning string is set instead.
        """

        try:
            self.text = next(self.text_generator)
        except StopIteration:
            self.text = "You have typed all the texts in this category!"

        self.labelMainText.setText(self.text)

    def calculate_score(self, accuracy: int) -> int:
        """Returns wpm score after calculations including accuracy."""

        seconds: float = perf_counter() - self.start_time
        return int(((len(self.text) / 5) / (seconds / 60)) * accuracy / 100)

    def calculate_accuracy(self, input_text: str) -> int:
        """Returns accuracy as an int between 1-100 representing a percentage."""

        correct: int = 0
        for i, character in enumerate(input_text):
            if character == self.text[i]:
                correct += 1

        return int(correct / len(self.text) * 100)

    def set_stats(self, input_text: str) -> None:
        """Sets instance variables for wpm score and accuracy."""

        self.accuracy = self.calculate_accuracy(input_text)
        self.wpm = self.calculate_score(self.accuracy)

    def display_highscore_result(self):
        self.highscore_result = self.highscore.update(self.wpm)
        self.results_window.labelHighscoreSet.setText(
            _TRANSLATE_RESULT[self.highscore_result]
        )

    def set_key_sound(self, key_sound):
        self.key_sound = key_sound

    def get_rich_text(self, input_text):
        """
        Returns the rich text to be displayed so characters typed correctly are
        highlighted green while incorrect characters are highlighted red.
        """

        typed_text = []
        rest_of_text = self.text[len(input_text) :]

        for i, character in enumerate(input_text):
            if self.text[i] == character:
                typed_text.append(
                    f'<span style="background-color:{self.colours[0]};">{self.text[i]}</span>'
                )
            else:
                typed_text.append(
                    f'<span style="background-color:{self.colours[1]};">{self.text[i]}</span>'
                )

        rich_text = (
            "<html><head/><body><p>"
            f'{"".join(typed_text)}'
            f"{rest_of_text}</p></body></html>"
        )

        return rich_text

    def update_time(self):
        """
        Updates the displayed time on self.labelTime in
        seconds since self.start_time.
        """

        self.labelTime.setText(str(int(perf_counter() - self.start_time)))

    def reset_time(self):
        """Resets self.timer, self.start_time and self.labelTime."""

        self.start_time = None
        self.timer.stop()
        self.labelTime.setText("0")

    def make_results_window(self):
        self.results_window = results.ResultsWindow()

        self.results_window.setWindowIcon(self.windowIcon())

        self.results_window.labelAccuracy.setText(f"Accuracy: {str(self.accuracy)}%")
        self.results_window.labelSpeed.setText(f"Speed:    {str(self.wpm)} wpm!")
        self.display_highscore_result()

        self.results_window.buttonNext.clicked.connect(self.on_clicked_next)

        # Apply same functionality as for the self.buttonMainMenu, which
        # is set in main.py
        self.results_window.buttonMainMenu.clicked.connect(
            self.on_clicked_results_main_menu
        )

    def on_finished(self, input_text):
        self.set_stats(input_text)

        self.make_results_window()

        self.hide()
        self.results_window.show()

        # stylesheet for results window must be set after the window is shown
        self.results_window.setStyleSheet(self.styleSheet())

    # Button Methods
    def on_clicked_restart(self):
        self.lineInput.clear()
        self.reset_time()

    def on_clicked_new(self):
        self.on_clicked_restart()
        self.set_main_text()

    def on_clicked_next(self):
        self.show()
        self.on_clicked_new()

        self.results_window.close()
        del self.results_window

    def on_clicked_results_main_menu(self):
        """
        Clicks the typing window's main menu button and closes the results window.

        This is done because the functinality for the main menu button is given
        in main.py.
        """

        self.buttonMainMenu.click()
        self.results_window.close()

    def on_input_text_changed(self, input_text: str) -> None:
        """
        Updates background of each letter as user types and calls a function when
        the user is finished.
        """

        # Break out of function if the text characters are exceeded
        # This is required to avoid an error if the user spams keys
        # right at the end of the text they are typing
        if len(input_text) > len(self.text):
            return None

        # Update displayed time or start timer
        if not self.start_time:
            self.timer.start()
            self.start_time = perf_counter()

        # Try to play key sound effect, if it exists
        try:
            self.key_sound.play()
        except AttributeError:
            pass

        # Set label text to rich text so typed characters are highlighted
        # based on whether they match self.text
        rich_text = self.get_rich_text(input_text)
        self.labelMainText.setText(rich_text)

        if len(input_text) == len(self.text):
            self.on_finished(input_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = TypingWindow()
    window.show()

    app.exec_()
