import os
import pickle
import sys
from pathlib import Path

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtMultimedia import QSoundEffect

from ps_typer.type_test import highscores, main_menu, settings, statistics, type_test

# PATHS
BASE_FOLDER = Path(__file__).parents[0]
ASSETS_FOLDER = BASE_FOLDER / "assets"
DATA_FOLDER = BASE_FOLDER / "data"
ICON_PATH = ASSETS_FOLDER / "icon.png"
FONT_PATH = ASSETS_FOLDER / "InconsolataBold.ttf"
SOUND_FOLDER = ASSETS_FOLDER / "sounds"
DATA_FILE = DATA_FOLDER / "data.pkl"


class MainWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ICON = QIcon(str(ICON_PATH))
        self.setWindowIcon(self.ICON)

        self.stacked_widget = QtWidgets.QStackedWidget()

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

        self.main_menu_window = main_menu.MainMenu()
        self.main_menu_window.setWindowIcon(self.ICON)
        self.stacked_widget.insertWidget(0, self.main_menu_window)

        # BUTTONS
        self.main_menu_window.buttonStart.clicked.connect(self.on_clicked_start)
        self.main_menu_window.buttonSettings.clicked.connect(self.on_clicked_settings)
        self.main_menu_window.buttonStatistics.clicked.connect(
            self.on_clicked_statistics
        )
        self.main_menu_window.buttonExit.clicked.connect(
            QtWidgets.QApplication.instance().quit
        )
        self.main_menu_window.comboBoxSelectMode.currentIndexChanged.connect(
            self.on_change_mode
        )

        # HIGHSCORES HANDLER
        self.highscore = highscores.Highscores()
        self.update_highscores()

        # DATA AND SETTINGS
        if DATA_FILE.is_file():
            self.load_data_from_file()
        else:
            self.data = settings.DEFAULT_DATA

        self.main_menu_window.comboBoxSelectMode.setCurrentIndex(
            self.data.get("selected_mode", 0)
        )

        # SOUND
        self.set_key_sound(self.get_setting("sound_filename"))

        # FONT
        self.inconsolata_bold = self.load_custom_font(str(FONT_PATH))

        # Stylesheet is set in the main program after instantiation

    def switch_focused_window(self, window: any) -> None:
        self.stacked_widget.insertWidget(1, window)
        self.stacked_widget.setCurrentIndex(1)

    # Button methods
    def on_clicked_start(self) -> None:
        mode_window = self.create_mode_window(
            str(self.main_menu_window.comboBoxSelectMode.currentText())
        )

        self.switch_focused_window(mode_window)

        self.show_window(mode_window, self.isMaximized())

        mode_window.setStyleSheet(self.get_setting("stylesheet"))
        mode_window.set_colours(self.get_setting("rich_text_colours"))

    def on_clicked_main_menu(self, window: QtWidgets.QWidget) -> None:
        #
        #
        # self.show_window(self, window.isMaximized())

        # window.close()
        self.stacked_widget.removeWidget(window)
        del window

        self.stacked_widget.setCurrentIndex(0)

    def on_clicked_settings(self) -> None:
        self.create_settings_window()

        self.switch_focused_window(self.settings_window)

        self.show_window(self.settings_window, self.isMaximized())
        self.settings_window.setStyleSheet(self.get_setting("stylesheet"))

    def on_clicked_apply(self) -> None:
        """Executed when apply button in settings window is clicked."""

        self.data["settings"] = self.settings_window.get_settings()

        # Key sound
        self.set_key_sound(self.get_setting("sound_filename"))

        # Stylesheet
        self.settings_window.setStyleSheet(self.get_setting("stylesheet"))
        self.setStyleSheet(self.get_setting("stylesheet"))

        # Save
        self.save_data_to_file()

    def on_clicked_statistics(self) -> None:
        self.create_stats_window()

        self.switch_focused_window(self.stats_window)

        self.show_window(self.stats_window, self.isMaximized())
        self.stats_window.setStyleSheet(self.get_setting("stylesheet"))

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

    def on_change_mode(self):
        """
        Saves the selected mode to self.data and pickles self.data so the selection is
        remembered.
        """

        self.data[
            "selected_mode"
        ] = self.main_menu_window.comboBoxSelectMode.currentIndex()
        self.save_data_to_file()

    # Helper Methods
    def get_setting(self, setting: str):
        """
        Convenience method for getting a specific setting from self.data, or a
        default value.
        """

        return self.data["settings"].get(setting, settings.DEFAULT_SETTINGS.get(setting))

    def load_custom_font(self, font: str) -> int:
        """Adds custom font to QFontDatabase, and returns its corresponding font id."""

        return QFontDatabase.addApplicationFont(font)

    def show_window(self, window: QtWidgets.QWidget, fullscreen: bool) -> None:
        """
        Used to show windows, with the option to have them maximised provided.
        """

        window.show()
        if fullscreen:
            window.setWindowState(QtCore.Qt.WindowMaximized)

    def create_mode_window(self, mode: str) -> type_test.TypingWindow:
        mode_window = type_test.TypingWindow(self.highscore, self.stacked_widget)
        mode_window.set_mode(mode)

        mode_window.setWindowIcon(self.ICON)

        mode_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(mode_window)
        )

        # Sets key sound if enabled
        if self.get_setting("play_sound"):
            mode_window.set_key_sound(self.key_sound)

        return mode_window

    def create_settings_window(self) -> settings.SettingsWindow:
        self.settings_window = settings.SettingsWindow()

        self.settings_window.setWindowIcon(self.ICON)

        self.settings_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(self.settings_window)
        )
        self.settings_window.buttonApply.clicked.connect(self.on_clicked_apply)

        # Keystroke sound toggle
        if self.get_setting("play_sound"):
            self.settings_window.toggleKeystrokeSound.setChecked(True)

        # Dark mode toggle
        if self.get_setting("dark_mode"):
            self.settings_window.toggleDarkMode.setChecked(True)

        self.set_settings_sounds_options()
        self.set_selected_sound_option(self.get_setting("sound_filename"))

    def create_stats_window(self) -> None:
        self.stats_window = statistics.StatsWindow()

        self.stats_window.setWindowIcon(self.ICON)

        # Update labels
        self.update_stats_highscores()
        self.update_stats_days_ago()

        # Set up graph
        self.stats_window.set_up_graph(
            self.highscore.get_stats_dailies(), self.get_setting("graph_colours")
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
        self.today_wpm, self.all_time_wpm = self.highscore.get_wpm()

    def save_data_to_file(self) -> None:
        """Pickles self.data into a file in the data folder."""

        with open(DATA_FILE, "wb") as data_pickle:
            pickle.dump(self.data, data_pickle)

    def load_data_from_file(self) -> None:
        """Sets self.data to the values saved on the data.pkl file."""

        with open(DATA_FILE, "rb") as data_pickle:
            self.data = pickle.load(data_pickle)

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


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()

    # Stylesheet set after window is shown
    main_window.show()
    main_window.setStyleSheet(main_window.get_setting("stylesheet"))

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
