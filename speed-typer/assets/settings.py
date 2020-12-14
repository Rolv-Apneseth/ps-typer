from PyQt5 import QtCore, QtWidgets

from source_ui import settings_window


# CONSTANTS
DARK_BUTTON = "rgb(70, 70, 70)"
DARK_BACKGROUND = "rgb(50, 50, 50)"
DARK_TEXT = "rgb(235, 235, 235)"

LIGHT_BUTTON = "rgb(200, 200, 200)"
LIGHT_BACKGROUND = "rbg(250, 250, 250)"
LIGHT_TEXT = "rgb(0, 0, 0)"


class SettingsWindow(QtWidgets.QWidget, settings_window.Ui_settingsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.DEFAULT_STYLE = self.styleSheet()
        self.current_stylesheet = self.styleSheet()

        self.buttonApply.clicked.connect(self.on_clicked_apply)

    # Helper methods
    def get_values(self):
        """Gets values entered by user for the different settings."""

        self.dark_mode = self.radioDarkMode.isChecked()  # False means light mode
        self.font_size = self.spinBoxPixel.value()  # Direct font px value
        self.key_sound = self.radioKeystrokeOn.isChecked()  # False means key sound off

    def replace_colour(self, c1: str, c2: str) -> None:
        """Replaces a colour in the current stylesheet with another."""

        self.current_stylesheet = self.current_stylesheet.replace(c1, c2)

    def replace_font(self, f1: str, f2: str) -> None:
        """Replaces a font size in the current stylesheet with another."""

        self.current_stylesheet.replace(f1, f2)

    def set_dark_mode(self):
        """Sets the stylesheet to be in dark mode (changes colours)."""

        self.replace_colour(LIGHT_BACKGROUND, DARK_BACKGROUND)
        self.replace_colour(LIGHT_BUTTON, DARK_BACKGROUND)
        self.replace_colour(LIGHT_TEXT, DARK_TEXT)

    def set_light_mode(self):
        self.replace_colour(DARK_BACKGROUND, LIGHT_BACKGROUND)
        self.replace_colour(DARK_BUTTON, LIGHT_BUTTON)
        self.replace_colour(DARK_TEXT, LIGHT_TEXT)

    def set_font_sizes(self):
        """Sets variables for the different font sizes to be used."""

        self.text_size = self.font_size
        self.title_size = round(self.font_size * 1.15)
        self.button_size = round(self.font_size * 0.7)
        self.typing_size = round(self.font_size * 1.3)

    def get_style_sheet(self):
        """
        Changes the current_stylesheet variable and returns the new stylesheet.

        This is to be used in main.py to set the styling for all windows.
        """

        if self.dark_mode:
            self.set_dark_mode()
        else:
            self.set_light_mode()

        return self.current_stylesheet


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = SettingsWindow()
    window.show()

    app.exec_()
