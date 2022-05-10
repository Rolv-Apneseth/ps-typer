import os
import pickle
import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtMultimedia import QSoundEffect

from ps_typer.data import style, utils
from ps_typer.data.highscores_data_handler import HighscoreDataHandler
from ps_typer.data.user_preferences_handler import UserPreferencesDataHandler
from ps_typer.data.utils import PATH_SOUNDS, get_today
from ps_typer.type_test import main_menu, settings, statistics, type_test


class MainWindow(QtWidgets.QWidget):
    def __init__(
        self,
        highscore_handler: HighscoreDataHandler,
        user_preferences_handler: UserPreferencesDataHandler,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self.highscore_handler: HighscoreDataHandler = highscore_handler
        self.user_preferences_handler: UserPreferencesDataHandler = (
            user_preferences_handler
        )
        self.set_stylesheet()

        self.ICON = QIcon(str(utils.PATH_ICONS))
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

        self.update_highscores()

        # DATA AND SETTINGS
        self.main_menu_window.comboBoxSelectMode.setCurrentIndex(
            self.get_preference("selected_mode")
        )

        # SOUND
        self.set_key_sound()

        # FONT
        self.inconsolata_bold = self.load_custom_font(str(utils.PATH_FONTS))

        # Stylesheet is set in the main program after instantiation

    def switch_focused_window(self, window: any) -> None:
        self.stacked_widget.insertWidget(1, window)
        self.stacked_widget.setCurrentIndex(1)

    # Button methods
    def on_clicked_start(self) -> None:
        typing_window = self.create_typing_window(
            str(self.main_menu_window.comboBoxSelectMode.currentText())
        )

        self.switch_focused_window(typing_window)

        self.show_window(typing_window, self.isMaximized())

        typing_window.setStyleSheet(self.stylesheet)

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
        self.settings_window.setStyleSheet(self.stylesheet)

    def on_clicked_apply(self) -> None:
        """Executed when apply button in settings window is clicked."""

        self.settings_window.apply_settings()
        self.set_key_sound()
        self.set_stylesheet()
        self.setStyleSheet(self.stylesheet)
        self.settings_window.setStyleSheet(self.stylesheet)

    def on_clicked_statistics(self) -> None:
        self.create_stats_window()

        self.switch_focused_window(self.stats_window)

        self.show_window(self.stats_window, self.isMaximized())
        self.stats_window.setStyleSheet(self.stylesheet)

    def on_clicked_reset_daily(self) -> None:
        """
        To be executed when 'Reset today's highscore' is pressed in the stats window.
        """

        self.highscore_handler.delete_highscore(get_today())

        self.update_highscores()
        self.update_stats_highscores()

    def on_clicked_reset_all_time(self) -> None:
        """
        To be executed when 'Reset all-time highscore' is pressed in the stats window.
        """

        self.highscore_handler.delete_all_highscores()

        self.update_highscores()
        self.update_stats_highscores()

    def on_clicked_reset_all(self) -> None:
        """
        To be executed when 'Reset all highscores' is pressed in the stats window.
        """

        self.highscore_handler.delete_all_highscores()

        self.update_highscores()
        self.update_stats_highscores()

    def on_change_mode(self):
        """
        Saves the selected mode to self.user_preferences_handler.preferences so the
        selection is remembered.
        """

        self.user_preferences_handler.set_selected_mode(
            self.main_menu_window.comboBoxSelectMode.currentIndex()
        )

    # Helper Methods
    def get_preference(self, preference: str) -> str | bool | int:
        """
        Convenience method for getting a specific preference from
        self.user_preferences_handler.preferences
        """

        return getattr(self.user_preferences_handler.preferences, preference)

    def set_stylesheet(self) -> None:
        self.stylesheet = style.get_style_sheet(**self.get_preference("colours")["base"])

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

    def create_typing_window(self, mode: str) -> type_test.TypingWindow:
        typing_window = type_test.TypingWindow(
            self.highscore_handler, self.stacked_widget
        )
        typing_window.set_mode(mode)
        typing_window.setWindowIcon(self.ICON)
        typing_window.set_rich_text_colours(self.get_preference("colours")["rich_text"])

        typing_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(typing_window)
        )

        # Sets key sound if enabled
        typing_window.set_key_sound(self.key_sound)

        return typing_window

    def create_settings_window(self) -> settings.SettingsWindow:
        self.settings_window = settings.SettingsWindow(self.user_preferences_handler)

        self.settings_window.setWindowIcon(self.ICON)

        self.settings_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(self.settings_window)
        )
        self.settings_window.buttonApply.clicked.connect(self.on_clicked_apply)

        # Keystroke sound toggle
        if self.get_preference("play_sound"):
            self.settings_window.toggleKeystrokeSound.setChecked(True)

        # Dark mode toggle
        if self.get_preference("dark_mode"):
            self.settings_window.toggleDarkMode.setChecked(True)

        self.set_settings_sounds_options()
        self.set_selected_sound_option(self.get_preference("sound_filename"))

    def create_stats_window(self) -> None:
        self.stats_window = statistics.StatsWindow()

        self.stats_window.setWindowIcon(self.ICON)

        # Update labels
        self.update_highscores()
        self.update_stats_highscores()
        self.update_stats_days_ago()

        # Set up graph
        self.stats_window.set_up_graph(
            self.highscore_handler.get_all_highscores(),
            self.get_preference("colours")["graph"],
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
        self.today_wpm, self.all_time_wpm = self.highscore_handler.get_wpm()

    def get_sounds_list(self) -> list:
        """Returns a list of the sound files present in the sounds folder."""

        return os.listdir(PATH_SOUNDS)

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

    def set_key_sound(self) -> None:
        """
        Sets the given sound file to a QSoundEffect object which will be played on each
        keystroke in the mode window.
        """

        if not self.get_preference("play_sound"):
            self.key_sound = QSoundEffect()
            return

        self.key_sound_path = PATH_SOUNDS / self.get_preference("sound_filename")
        self.key_sound_url = QtCore.QUrl.fromLocalFile(str(self.key_sound_path))

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

        self.stats_window.update_days_ago(self.highscore_handler.days_since_set())


def main():
    app = QtWidgets.QApplication(sys.argv)

    with sqlite3.connect(utils.PATH_USER_DATA_DB.absolute()) as conn:
        highscore_handler = HighscoreDataHandler(conn)
        user_preferences_handler = UserPreferencesDataHandler()
        main_window = MainWindow(highscore_handler, user_preferences_handler)

        # Stylesheet set after window is shown
        main_window.show()
        main_window.setStyleSheet(main_window.stylesheet)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
