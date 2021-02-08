from PyQt5 import QtWidgets

from source_ui import settings_window


# CONSTANTS
# Note: Do not make any colours in these 2 dictionaries the same value
# since these will be changed using a .replace method
DARK_COLOURS = {
    "button": "rgb(70, 70, 70)",
    "hover": "rgb(90, 90, 90)",
    "background": "rgb(18, 18, 18)",
    "frame": "rgb(31, 26, 31)",
    "text": "rgb(230, 230, 230)",
}

LIGHT_COLOURS = {
    "button": "#cfe3e6",
    "hover": "#defaff",
    "background": "#94f0ff",
    "frame": "#e2f3f5",
    "text": "#0e153a",
}

# Colours for rich text highlighting
RICH_TEXT_COLOURS = {
    True: ["rgb(0, 100, 0)", "rgb(140, 0, 0)"],
    False: ["rgb(0, 215, 0)", "rgb(230, 0, 0)"],
}

# Graph colours
DARK_GRAPH = {
    "background": (20, 20, 20),
    "axes": (235, 235, 235),
    "curve": (0, 170, 0),
}

LIGHT_GRAPH = {
    "background": (34, 209, 238),
    "axes": (14, 21, 58),
    "curve": (12, 153, 28),
}


class SettingsWindow(QtWidgets.QWidget, settings_window.Ui_settingsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

    # Helper methods

    def get_values(self):
        """Gets values entered by user for the different settings."""

        self.dark_mode = self.radioDarkMode.isChecked()  # False means light mode

        self.graph_colours = DARK_GRAPH if self.dark_mode else LIGHT_GRAPH

        self.rich_text_colours = (
            RICH_TEXT_COLOURS[True] if self.dark_mode else RICH_TEXT_COLOURS[False]
        )

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

        self.current_stylesheet = self.styleSheet()
        for option in LIGHT_COLOURS:
            self.replace_colour(LIGHT_COLOURS[option], DARK_COLOURS[option])

    def set_light_mode(self):
        """Sets the style sheet to be in light mode (changes colours)."""

        self.current_stylesheet = self.styleSheet()
        for option in DARK_COLOURS:
            self.replace_colour(DARK_COLOURS[option], LIGHT_COLOURS[option])

    def get_style_sheet(self) -> str:
        """
        Changes the current_stylesheet variable and returns the new stylesheet.

        The stylesheet returned is to be used in main.py to set the
        styling for all windows.
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
            self.rich_text_colours,
        ]


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = SettingsWindow()
    window.show()

    app.exec_()
