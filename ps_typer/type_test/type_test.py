from time import perf_counter
from typing import List

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QSoundEffect

from ps_typer.source_ui import typing_window
from ps_typer.type_test import highscores, results, texts

# Constants
DEFAULT_COLOURS = ["rgb(0, 100, 0)", "rgb(100, 0, 0)"]
_TRANSLATE_RESULT = {
    "all-time": "New all-time highscore set! Congratulations!",
    "daily": "New daily highscore set! Good job!",
    "none": "No new highscore set. Don't give up!",
}


class TypingWindow(QtWidgets.QWidget, typing_window.Ui_typingWindow):
    def __init__(self, highscore_obj: highscores.Highscores, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Multiple inheritance allows us to have the ui and window together so
        # setupui can be given self in for a window
        self.setupUi(self)

        self.lineInput.textChanged.connect(self._on_input_text_changed)
        self.buttonNewText.clicked.connect(self.on_clicked_new)
        self.buttonRestart.clicked.connect(self.on_clicked_restart)

        # time and timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._update_time)
        self.timer.setInterval(100)
        self._reset_time()

        # Object to handle saving and updating of highscore values
        self.highscore = highscore_obj

        # Defaults
        self.key_sound = QSoundEffect()
        self.set_colours(DEFAULT_COLOURS)

    # Public Methods
    def set_mode(self, mode: str) -> None:
        """
        Sets the mode for the typing window, by getting a specific generator
        from texts.py and setting a title for the window.
        """

        self.mode = mode

        self.labelTitle.setText(mode)

        if mode == "Common Phrases":
            self.labelMainText.setAlignment(QtCore.Qt.AlignCenter)

        self.text_generator = texts._translate[mode]()
        self._set_main_text()

    def set_colours(self, colours: List[str]) -> None:
        """
        Sets the colours to be used for rich text formatting.

        Dictionary provided should be in the order:
            [green_colour, red_colour]
        """

        self.colours = colours

    def set_key_sound(self, key_sound: QSoundEffect) -> None:
        """
        Set the sound to be played on a keystroke (should be a QSoundEffect object).
        """

        self.key_sound = key_sound

    # Private methods
    def _set_main_text(self) -> None:
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

    def _calculate_score(self, accuracy: int) -> int:
        """Returns wpm score after calculations including accuracy."""
        self.start_time: float

        seconds: float = perf_counter() - self.start_time

        return round(((len(self.text) / 5) / (seconds / 60)) * accuracy / 100)

    def _calculate_accuracy(self, input_text: str) -> int:
        """Returns accuracy as an int between 1-100 representing a percentage."""

        correct: int = 0
        for i, character in enumerate(input_text):
            if character == self.text[i]:
                correct += 1

        return int(correct / len(self.text) * 100)

    def _set_stats(self, input_text: str) -> None:
        """Sets instance variables for wpm score and accuracy."""

        self.accuracy = self._calculate_accuracy(input_text)
        self.wpm = self._calculate_score(self.accuracy)

    def _display_highscore_result(self) -> None:
        """
        Updates the highscore in the highscore object and displays the result.
        """

        self.highscore_result = self.highscore.update(self.wpm)
        self.results_window.labelHighscoreSet.setText(
            _TRANSLATE_RESULT[self.highscore_result]
        )

    def _get_rich_text(self, input_text: str) -> str:
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

    def _update_time(self) -> None:
        """
        Updates the displayed time on self.labelTime in
        seconds since self.start_time.
        """

        self.labelTime.setText(str(int(perf_counter() - self.start_time)))

    def _reset_time(self) -> None:
        """Resets self.timer, self.start_time and self.labelTime."""

        self.start_time = 0.0
        self.timer.stop()
        self.labelTime.setText("0")

    def _make_results_window(self) -> None:
        """Generates the results window."""

        self.results_window = results.ResultsWindow()

        self.results_window.setWindowIcon(self.windowIcon())

        self.results_window.labelAccuracy.setText(f"{str(self.accuracy)}%")
        self.results_window.labelSpeed.setText(f"{str(self.wpm)} WPM")

        self._display_highscore_result()

        self.results_window.buttonNext.clicked.connect(self.on_clicked_next)

        # Apply same functionality as for the self.buttonMainMenu, which
        # is set in main.py
        self.results_window.buttonMainMenu.clicked.connect(
            self.on_clicked_results_main_menu
        )

    def _on_finished(self, input_text: str) -> None:
        """
        Opens the results window, and is called when the user has typed
        out all the given text.
        """

        self._set_stats(input_text)

        self._make_results_window()

        self.hide()
        self.results_window.show()
        if self.isMaximized():
            self.results_window.setWindowState(QtCore.Qt.WindowMaximized)

        # stylesheet for results window must be set after the window is shown
        self.results_window.setStyleSheet(self.styleSheet())

    def _on_input_text_changed(self, input_text: str) -> None:
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
        self.key_sound.play()

        # Set label text to rich text so typed characters are highlighted
        # based on whether they match self.text
        rich_text = self._get_rich_text(input_text)
        self.labelMainText.setText(rich_text)

        if len(input_text) >= len(self.text):
            self._on_finished(input_text)

    # BUTTON METHODS
    def on_clicked_restart(self) -> None:
        self.lineInput.clear()
        self._reset_time()

    def on_clicked_new(self) -> None:
        self.on_clicked_restart()
        self._set_main_text()

    def on_clicked_next(self) -> None:
        self.show()
        self.on_clicked_new()

        self.results_window.close()
        del self.results_window

    def on_clicked_results_main_menu(self) -> None:
        """
        Clicks the typing window's main menu button and closes the results window.

        This is done because the functionality for the main menu button is given
        in main.py.
        """

        self.buttonMainMenu.click()
        self.results_window.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = TypingWindow(highscores.Highscores())
    window.show()

    app.exec_()
