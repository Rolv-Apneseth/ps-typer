from PyQt5 import QtWidgets

from source_ui import settings_window


# CONSTANTS
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
    "symbols": (170, 0, 170),
}

LIGHT_GRAPH = {
    "background": (34, 209, 238),
    "axes": (14, 21, 58),
    "curve": (12, 153, 28),
    "symbols": (238, 63, 34),
}


# DEFAULT STYLESHEET AND SETTINGS
def _get_style_sheet_(background="", text="", frame="", hover="", button=""):
    """
    Returns a string representing the style sheet.

    Usage: _get_style_sheet(**DARK_COLOURS) or _get_style_sheet(**LIGHT_COLOURS)
    """

    try:
        return (
            "QWidget {\n"
            f"  background: {background}; color: {text}; font-size: 24pt;"
            "\n}\n"
            "QFrame {\n"
            f"  background: {frame}; border: 1px solid {text}; border-radius: 5;"
            "\n}\n"
            "QPushButton, QComboBox {\n"
            f"  background: {button}; font-size: 16pt; border-radius: 5;"
            "\n}\n"
            "QPushButton::hover, QComboBox::hover {\n"
            f"	background: {hover};"
            "\n}\n"
            "QLabel, QRadioButton {\n"
            "	background: transparent; border: none;"
            "\n}\n"
            'QFrame[frameShape="4"] {\n'
            f"    background-color: {text}; border-color: {text};"
            "\n}"
        )
    except NameError as e:
        print(e)
        raise NameError(
            "Pass in either DARK_COLOURS or LIGHT_COLOURS dictionaries as unpacked"
            " kwargs i.e. _get_style_sheet(**DARK_COLOURS)"
        )


BASE_STYLE_SHEET = _get_style_sheet_(**DARK_COLOURS)

DEFAULT_SETTINGS = [
    False,  # Play key sound (True or False)
    "key_4.wav",  # Name of sound file to play (str)
    BASE_STYLE_SHEET,  # Stylesheet for all windows (list)
    True,  # Dark mode (True or False)
    DARK_GRAPH,  # Colours for graph (dict)
    RICH_TEXT_COLOURS[True],  # Rich text colours (dict[list])
]


class SettingsWindow(QtWidgets.QWidget, settings_window.Ui_settingsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

    # Helper methods
    def _get_values(self) -> None:
        """Updates all relevant settings into instance variables."""

        self.is_dark_mode = self.radioDarkMode.isChecked()  # False means light mode

        self.graph_colours = DARK_GRAPH if self.is_dark_mode else LIGHT_GRAPH

        self.rich_text_colours = (
            RICH_TEXT_COLOURS[True] if self.is_dark_mode else RICH_TEXT_COLOURS[False]
        )

        self.play_key_sound = (
            self.radioKeystrokeOn.isChecked()
        )  # False means key sound off

        self.key_sound = str(
            self.comboSelectSound.currentText()
        )  # Sound to play on keystroke

        self.style_sheet = self._get_style_sheet()

    def _get_style_sheet(self) -> str:
        """
        Returns a string representing the stylesheet.

        The stylesheet returned is to be used in main.py to set the
        styling for all windows.
        """

        colours = DARK_COLOURS if self.is_dark_mode else LIGHT_COLOURS

        return _get_style_sheet_(**colours)

    # Public Method
    def get_settings(self) -> list:
        """Returns a list of settings variables which control various attributes."""

        self._get_values()

        return [
            self.play_key_sound,
            self.key_sound,
            self.style_sheet,
            self.is_dark_mode,
            self.graph_colours,
            self.rich_text_colours,
        ]


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = SettingsWindow()
    window.show()

    app.exec_()
