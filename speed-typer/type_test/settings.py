from PyQt5 import QtWidgets

from source_ui import settings_window


# CONSTANTS
DARK_COLOURS = {
    "bg": "hsl(217, 90, 20)",
    "bg_lighter": "hsl(217, 90, 45)",
    "text": "hsl(0, 0, 205)",
    "text_button": "hsl(0, 0, 160)",
}

LIGHT_COLOURS = {
    "bg": "hsl(217, 90, 210)",
    "bg_lighter": "hsl(217, 90, 235)",
    "text": "hsl(0, 0, 50)",
    "text_button": "hsl(0, 0, 120)",
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
def _get_style_sheet_(bg="", bg_lighter="", text="", text_button=""):
    """
    Returns a string representing the style sheet.

    Usage: _get_style_sheet(**DARK_COLOURS) or _get_style_sheet(**LIGHT_COLOURS)
    """

    try:
        return f"""QWidget {{
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 {bg}, stop:0.807107 {bg_lighter}
                );
                color: {text}; font-size: 24pt;
                font-weight: bold; font-family: "Inconsolata Nerd Font"
            }}
            QPushButton, QComboBox {{
                background: transparent; font-size: 25pt; border-radius: 5;
                padding: 8px; text-align: left; color: {text_button}
            }}
            QPushButton::hover, QComboBox::hover, QPushButton::focus, QComboBox::focus {{
                background: transparent; color: {text}; outline: none;
            }}
            QComboBox::down-arrow {{
                background: transparent;
            }}
            QComboBox::item {{
                background: {bg_lighter};
            }}
            QComboBox::item:selected {{
                color: {text};
            }}
            QLabel, QRadioButton {{
                background: transparent; border: none;
            }}
            #labelMainMenu {{
            font-size: 50pt;
            }}"""

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
