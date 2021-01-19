from PyQt5 import QtWidgets

from source_ui import settings_window


# CONSTANTS
# Note: Do not make any colours the same value
# since these will be changed using a .replace method
DARK_BUTTON = "rgb(70, 70, 70)"
DARK_BUTTON_HOVER = "rgb(90, 90, 90)"
DARK_BACKGROUND = "rgb(50, 50, 50)"
DARK_TEXT = "rgb(235, 235, 235)"


LIGHT_BUTTON = "rgb(200, 200, 200)"
LIGHT_BUTTON_HOVER = "rgb(215, 215, 215)"
LIGHT_BACKGROUND = "rgb(220, 220, 220)"
LIGHT_TEXT = "rgb(0, 0, 0)"

# Graph colours
DARK_GRAPH = {
    "background": (20, 20, 20),
    "axes": (235, 235, 235),
    "curve": (0, 170, 0),
}

LIGHT_GRAPH = {
    "background": (170, 190, 220),
    "axes": (20, 20, 20),
    "curve": (24, 135, 92),
}


class SettingsWindow(QtWidgets.QWidget, settings_window.Ui_settingsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.DEFAULT_STYLE = self.styleSheet()
        self.current_stylesheet = self.styleSheet()

    # Helper methods
    def get_values(self):
        """Gets values entered by user for the different settings."""

        self.dark_mode = self.radioDarkMode.isChecked()  # False means light mode

        self.graph_colours = DARK_GRAPH if self.dark_mode else LIGHT_GRAPH

        self.play_key_sound = (
            self.radioKeystrokeOn.isChecked()
        )  # False means key sound off

        self.key_sound = str(
            self.comboSelectSound.currentText()
        )  # Sound to play on keystroke

    def replace_colour(self, c1: str, c2: str) -> None:
        """Replaces a colour in the current stylesheet with another."""

        self.current_stylesheet = self.current_stylesheet.replace(c1, c2)

    def set_dark_mode(self):
        """Sets the style sheet to be in dark mode (changes colours)."""

        self.replace_colour(LIGHT_BACKGROUND, DARK_BACKGROUND)
        self.replace_colour(LIGHT_BUTTON, DARK_BACKGROUND)
        self.replace_colour(LIGHT_BUTTON_HOVER, DARK_BUTTON_HOVER)
        self.replace_colour(LIGHT_TEXT, DARK_TEXT)

    def set_light_mode(self):
        """Sets the style sheet to be in light mode (changes colours)."""

        self.replace_colour(DARK_BACKGROUND, LIGHT_BACKGROUND)
        self.replace_colour(DARK_BUTTON, LIGHT_BUTTON)
        self.replace_colour(DARK_BUTTON_HOVER, LIGHT_BUTTON_HOVER)
        self.replace_colour(DARK_TEXT, LIGHT_TEXT)

    def get_style_sheet(self) -> str:
        """
        Changes the current_stylesheet variable and returns the new stylesheet.

        The stylesheet returned is to be used in main.py to set the styling for all windows.
        """

        if self.dark_mode:
            self.set_dark_mode()
        else:
            self.set_light_mode()

        return self.current_stylesheet

    def get_settings(self):
        """Returns a list of settings variables which control various attributes."""

        self.get_values()

        self.style_sheet = self.get_style_sheet()

        return [
            self.play_key_sound,
            self.key_sound,
            self.style_sheet,
            self.dark_mode,
            self.graph_colours,
        ]


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = SettingsWindow()
    window.show()

    app.exec_()
