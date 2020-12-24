import os
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QSoundEffect

import type_test
from source_ui import main_window
from assets import highscores, settings


FILE_PATH = os.path.dirname(os.path.abspath(__file__))
SOUND_FOLDER = os.path.join(FILE_PATH, "assets", "sounds")
SETTINGS_FILE = os.path.join(FILE_PATH, "assets", "saved_settings.json")


class MainWindow(QtWidgets.QWidget, main_window.Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Multiple inheritance allows us to have the ui and window together so
        # setupui can be given self in for a window
        self.setupUi(self)

        self.buttonStart.clicked.connect(self.on_clicked_start)
        self.buttonSettings.clicked.connect(self.on_clicked_settings)

        # Initialize highscores handler
        self.highscore = highscores.Highscores()
        self.update_highscores()

        # Default stylesheet if settings are not changed
        self.style_sheet = self.styleSheet()

        # Settings - items: 0. Play key sound
        #                   1. Name of sound file to play
        #
        # Load setings file from assets folder if it exists, otherwise
        # set it to default settings
        if self.exists_settings_file():
            self.load_settings_from_file()
        else:
            self.settings = [False, "key_4.wav"]

        # Sound played on keystroke, if sounds are turned on
        self.set_key_sound(self.settings[1])

    # Button methods
    def on_clicked_start(self):
        self.make_mode_window(str(self.comboBoxSelectMode.currentText()))

        self.mode_window.show()
        self.mode_window.setStyleSheet(self.style_sheet)

        self.hide()

    def on_clicked_main_menu(self, window):
        self.update_highscores()
        self.show()

        window.close()
        del window

    def on_clicked_settings(self):
        self.make_settings_window()

        self.settings_window.show()
        self.settings_window.setStyleSheet(self.style_sheet)

        self.hide()

    def on_clicked_apply(self):
        self.settings = self.settings_window.get_settings()
        self.style_sheet = self.settings_window.get_style_sheet()

        self.settings_window.setStyleSheet(self.style_sheet)
        self.setStyleSheet(self.style_sheet)

        self.set_key_sound(self.settings[1])

        self.save_settings_to_file()

    # Helper Methods
    def make_mode_window(self, mode):
        self.mode_window = type_test.TypingWindow()
        self.mode_window.set_mode(mode)

        self.mode_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(self.mode_window)
        )

        # Sets key sound if option is set to True in self.settings
        if self.settings[0]:
            self.mode_window.set_key_sound(self.key_sound)

    def make_settings_window(self):
        self.settings_window = settings.SettingsWindow()

        self.settings_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(self.settings_window)
        )
        self.settings_window.buttonApply.clicked.connect(self.on_clicked_apply)

        self.set_settings_sounds_options()
        self.set_selected_sound_option(self.settings[1])

    def update_highscores(self):
        self.highscore.load_data()
        self.today_wpm, self.all_time_wpm = self.highscore.get_wpm()

        self.labelTodayScore.setText(f"{self.today_wpm} WPM")
        self.labelAlltimeScore.setText(f"{self.all_time_wpm} WPM")

    def exists_settings_file(self) -> bool:
        """Returns boolean value representing whether a saved settings file exists."""

        return os.path.exists(SETTINGS_FILE)

    def delete_settings(self):
        """Deletes saved settings file in the assets folder."""

        os.remove(SETTINGS_FILE)

    def save_settings_to_file(self):
        """Saves self.settings into a .json file in the assets folder."""

        # Deletes file if it already exists
        if self.exists_settings_file():
            self.delete_settings()

        with open(SETTINGS_FILE, "w") as settings_file:
            settings_file.write(json.dumps(self.settings))

    def load_settings_from_file(self):
        """Sets self.settings to the values saved on the saved settings file."""

        with open(SETTINGS_FILE, "r") as settings_file:
            self.settings = json.load(settings_file)

    def get_sounds_list(self) -> list:
        """Returns a list of the sound files present in the sounds folder."""

        return os.listdir(SOUND_FOLDER)

    def set_settings_sounds_options(self):
        """
        Sets up options for the dropdown menu to select keystroke sounds in the
        settings menu.
        """

        for sound_file in self.get_sounds_list():
            # Add sound file name to dropdown menu
            self.settings_window.comboSelectSound.addItem(sound_file)

    def find_sound_file_index(self, sound_file: str) -> int:
        """
        Returns the index of the given file name within the settings window
        comboSelectSound object.
        """

        return self.settings_window.comboSelectSound.findText(
            sound_file, QtCore.Qt.MatchFixedString
        )

    def set_selected_sound_option(self, sound_file: str) -> None:
        """
        Sets the selected option for sound file from the settings window's
        comboSelectSound object to the given sound file name.
        """

        index: int = self.find_sound_file_index(sound_file)

        if index >= 0:
            self.settings_window.comboSelectSound.setCurrentIndex(index)

    def set_key_sound(self, sound_file: str) -> None:
        """
        Sets the given sound file to a QSoundEffect object which will be played on each
        keystroke in the mode window.
        """

        self.key_sound_path = os.path.join(SOUND_FOLDER, sound_file)
        self.key_sound_url = QtCore.QUrl.fromLocalFile(self.key_sound_path)

        self.key_sound = QSoundEffect()
        self.key_sound.setSource(self.key_sound_url)
        self.key_sound.setVolume(0.5)
        self.key_sound.setLoopCount(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
