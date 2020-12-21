import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QSoundEffect

import type_test
from source_ui import main_window
from assets import highscores, settings


FILE_PATH = os.path.dirname(os.path.abspath(__file__))
SOUND_FOLDER = os.path.join(FILE_PATH, "assets", "sounds")


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

        # Default settings - items: 0. Play key sound
        self.settings = [True]

        # Sound played on keystroke, On by default
        self.set_key_sound("key_1.wav")

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

    def update_highscores(self):
        self.highscore.load_data()
        self.today_wpm, self.all_time_wpm = self.highscore.get_wpm()

        self.labelTodayScore.setText(f"{self.today_wpm} WPM")
        self.labelAlltimeScore.setText(f"{self.all_time_wpm} WPM")

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
