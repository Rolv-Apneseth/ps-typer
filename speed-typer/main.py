import os
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtGui import QIcon
from pathlib import Path
from typing import Any

from source_ui import main_window
from type_test import highscores, settings, statistics, type_test

# PATHS
BASE_FOLDER = Path(__file__).parents[0]
ASSETS_FOLDER = BASE_FOLDER / "assets"
DATA_FOLDER = BASE_FOLDER / "data"
ICON_PATH = ASSETS_FOLDER / "icon.png"
SOUND_FOLDER = ASSETS_FOLDER / "sounds"
SETTINGS_FILE = DATA_FOLDER / "saved_settings.json"


class MainWindow(QtWidgets.QWidget, main_window.Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Multiple inheritance allows us to have the ui and window together so
        # setupui can be given self in for a window
        self.setupUi(self)

        self.ICON = QIcon(str(ICON_PATH))
        self.setWindowIcon(self.ICON)

        self.buttonStart.clicked.connect(self.on_clicked_start)
        self.buttonSettings.clicked.connect(self.on_clicked_settings)
        self.buttonStatistics.clicked.connect(self.on_clicked_statistics)

        # Initialize highscores handler
        self.highscore = highscores.Highscores()
        self.update_highscores()

        # Settings - items: 0. Play key sound
        #                   1. Name of sound file to play
        #                   2. Stylesheet for all windows
        #                   3. Dark mode (True or False)
        #                   4. Colours for graph (dict)
        #                   5. Rich text colours (dict[list])
        #
        # Load setings file from data folder if it exists, otherwise
        # set it to default settings
        if self.exists_settings_file():
            self.load_settings_from_file()
        else:
            self.settings = [
                False,
                "key_4.wav",
                self.styleSheet(),
                True,
                settings.DARK_GRAPH,
                settings.RICH_TEXT_COLOURS[True],
            ]

        # Sound played on keystroke, if sounds are turned on
        self.set_key_sound(self.settings[1])
        # Stylesheet is set in the main program after instantiation

    # Button methods
    def on_clicked_start(self) -> None:
        self.make_mode_window(str(self.comboBoxSelectMode.currentText()))

        self.mode_window.show()
        self.mode_window.setStyleSheet(self.settings[2])
        self.mode_window.set_colours(self.settings[5])

        self.hide()

    def on_clicked_main_menu(self, window: QtWidgets.QWidget) -> None:
        self.update_highscores()
        self.show()

        window.close()
        del window

    def on_clicked_settings(self) -> None:
        self.make_settings_window()

        self.settings_window.show()
        self.settings_window.setStyleSheet(self.settings[2])

        self.hide()

    def on_clicked_apply(self) -> None:
        """Executed when apply button in settings window is clicked."""

        self.settings = self.settings_window.get_settings()

        # Key sound
        self.set_key_sound(self.settings[1])

        # Stylesheet
        self.settings_window.setStyleSheet(self.settings[2])
        self.setStyleSheet(self.settings[2])

        # Save settings
        self.save_settings_to_file()

    def on_clicked_statistics(self) -> None:
        self.make_stats_window()

        self.stats_window.show()
        self.stats_window.setStyleSheet(self.settings[2])

        self.hide()

    def on_clicked_reset_daily(self) -> None:
        """
        To be executed when 'Reset today's highscore' is pressed in the stats window.
        """

        self.highscore.delete_daily_highscore()

        self.update_highscores()
        self.update_stats_highscores()

    def on_clicked_reset_all_time(self) -> None:
        """
        To be executed when 'Reset all-time highscore' is pressed in the stats window.
        """

        self.highscore.delete_all_time_highscore()

        self.update_highscores()
        self.update_stats_highscores()

    def on_clicked_reset_all(self) -> None:
        """
        To be executed when 'Reset all highscores' is pressed in the stats window.
        """

        self.highscore.delete_all_highscores()

        self.update_highscores()
        self.update_stats_highscores()

    # Helper Methods
    def make_mode_window(self, mode: str) -> None:
        self.mode_window = type_test.TypingWindow(self.highscore)
        self.mode_window.set_mode(mode)

        self.mode_window.setWindowIcon(self.ICON)

        self.mode_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(self.mode_window)
        )

        # Sets key sound if option is set to True in self.settings
        if self.settings[0]:
            self.mode_window.set_key_sound(self.key_sound)

    def make_settings_window(self) -> None:
        self.settings_window = settings.SettingsWindow()

        self.settings_window.setWindowIcon(self.ICON)

        self.settings_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(self.settings_window)
        )
        self.settings_window.buttonApply.clicked.connect(self.on_clicked_apply)

        # Sound radio buttons
        if self.settings[0]:
            self.settings_window.radioKeystrokeOn.setChecked(True)
        else:
            self.settings_window.radioKeystrokeOff.setChecked(True)

        # Mode radio buttons
        if self.settings[3]:
            self.settings_window.radioDarkMode.setChecked(True)
        else:
            self.settings_window.radioLightMode.setChecked(True)

        self.set_settings_sounds_options()
        self.set_selected_sound_option(self.settings[1])

    def make_stats_window(self) -> None:
        self.stats_window = statistics.StatsWindow()

        self.stats_window.setWindowIcon(self.ICON)

        # Update labels
        self.update_stats_highscores()
        self.update_stats_days_ago()

        # Set up graph
        self.stats_window.set_up_graph(
            self.highscore.get_stats_dailies(), self.settings[4]
        )

        # Connect buttons
        self.stats_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(self.stats_window)
        )
        self.stats_window.buttonResetDaily.clicked.connect(self.on_clicked_reset_daily)
        self.stats_window.buttonResetAllTime.clicked.connect(
            self.on_clicked_reset_all_time
        )
        self.stats_window.buttonResetAll.clicked.connect(self.on_clicked_reset_all)

    def update_highscores(self) -> None:
        self.highscore._load_data()
        self.today_wpm, self.all_time_wpm = self.highscore.get_wpm()

        self.labelTodayScore.setText(f"{self.today_wpm} WPM")
        self.labelAlltimeScore.setText(f"{self.all_time_wpm} WPM")

    def exists_settings_file(self) -> bool:
        """Returns boolean value representing whether a saved settings file exists."""

        return os.path.exists(SETTINGS_FILE)

    def delete_settings(self) -> None:
        """Deletes saved settings file in the data folder."""

        os.remove(SETTINGS_FILE)

    def save_settings_to_file(self) -> None:
        """Saves self.settings into a .json file in the data folder."""

        # Deletes file if it already exists
        if self.exists_settings_file():
            self.delete_settings()

        with open(SETTINGS_FILE, "w") as settings_file:
            settings_file.write(json.dumps(self.settings))

    def load_settings_from_file(self) -> None:
        """Sets self.settings to the values saved on the saved settings file."""

        with open(SETTINGS_FILE, "r") as settings_file:
            self.settings = json.load(settings_file)

    def get_sounds_list(self) -> list:
        """Returns a list of the sound files present in the sounds folder."""

        return os.listdir(SOUND_FOLDER)

    def set_settings_sounds_options(self) -> None:
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

    def update_stats_highscores(self) -> None:
        """Updates highscores displayed in the stats window."""

        self.stats_window.labelTodayScore.setText(f"{self.today_wpm} WPM")
        self.stats_window.labelAllTimeScore.setText(f"{self.all_time_wpm} WPM")

    def update_stats_days_ago(self) -> None:
        """
        Updates the labelDaysAgo element in the stats window with the
        number of days since the all-time highscore was set.
        """

        self.stats_window.update_days_ago(self.highscore.days_since_set())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    # Stylesheet must be changed after window is shown
    window.setStyleSheet(window.settings[2])

    app.exec_()
