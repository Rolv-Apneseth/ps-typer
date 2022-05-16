import os
import sqlite3
import sys
from typing import Any, Generator

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtMultimedia import QSoundEffect

from ps_typer.data import style, utils
from ps_typer.data.highscores_data_handler import HighscoreDataHandler
from ps_typer.data.user_preferences_handler import UserPreferencesDataHandler
from ps_typer.data.utils import PATH_SOUNDS, get_today
from ps_typer.type_test import main_menu, results, settings, statistics, type_test


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
        self.setMinimumSize(1080, 800)

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
        self.main_menu_window.buttonExit.clicked.connect(self.on_clicked_exit)
        self.main_menu_window.comboBoxSelectMode.currentIndexChanged.connect(
            self.on_change_mode
        )

        self.update_highscores()

        # DATA AND SETTINGS
        self.main_menu_window.comboBoxSelectMode.setCurrentIndex(
            self.get_preference("selected_mode")
        )

        # FONT
        self.inconsolata_bold = self.load_custom_font(str(utils.PATH_FONTS))

        # Stylesheet is set in the main program after instantiation

    def switch_focused_window(
        self,
        window: type_test.TypingWindow
        | settings.SettingsWindow
        | results.ResultsWindow
        | statistics.StatsWindow,
    ) -> None:
        self.stacked_widget.insertWidget(1, window)
        self.stacked_widget.setCurrentIndex(1)

    # Button methods
    def on_clicked_exit(self) -> None:
        instance: QtCore.QCoreApplication | None = QtWidgets.QApplication.instance()
        if instance:
            instance.quit()

    def on_clicked_start(self) -> None:
        typing_window = self.create_typing_window(
            str(self.main_menu_window.comboBoxSelectMode.currentText())
        )

        self.switch_focused_window(typing_window)

        typing_window.show()

        typing_window.setStyleSheet(self.stylesheet)

    def on_clicked_main_menu(self, window: QtWidgets.QWidget) -> None:
        self.stacked_widget.removeWidget(window)
        del window

        self.stacked_widget.setCurrentIndex(0)

    def on_clicked_settings(self) -> None:
        settings_window: settings.SettingsWindow = self.create_settings_window()

        self.switch_focused_window(settings_window)

        settings_window.show()
        settings_window.setStyleSheet(self.stylesheet)

    def on_clicked_statistics(self) -> None:
        self.create_stats_window()

        self.switch_focused_window(self.stats_window)

        self.stats_window.show()
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
    def get_preference(self, preference: str) -> Any:
        """
        Convenience method for getting a specific preference from
        self.user_preferences_handler.preferences
        """

        return getattr(self.user_preferences_handler.preferences, preference)

    def set_stylesheet(self) -> None:
        colours: dict[str, dict[str, str]] = self.get_preference("colours")
        self.stylesheet: str = style.get_style_sheet(**colours["base"])

    def load_custom_font(self, font: str) -> int:
        """Adds custom font to QFontDatabase, and returns its corresponding font id."""

        return QFontDatabase.addApplicationFont(font)

    def create_typing_window(self, mode: str) -> type_test.TypingWindow:
        typing_window = type_test.TypingWindow(
            self.highscore_handler, self.stacked_widget, self.get_key_sounds_rotator()
        )
        typing_window.set_mode(mode)
        typing_window.setWindowIcon(self.ICON)
        typing_window.set_rich_text_colours(self.get_preference("colours")["rich_text"])

        typing_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(typing_window)
        )

        return typing_window

    def create_settings_window(self) -> settings.SettingsWindow:
        settings_window = settings.SettingsWindow(self.user_preferences_handler)

        settings_window.setWindowIcon(self.ICON)

        settings_window.buttonMainMenu.clicked.connect(
            lambda: self.on_clicked_main_menu(settings_window)
        )

        def on_clicked_apply() -> None:
            """Executed when apply button in settings window is clicked."""

            settings_window.apply_settings()
            self.set_stylesheet()
            self.setStyleSheet(self.stylesheet)
            settings_window.setStyleSheet(self.stylesheet)

        settings_window.buttonApply.clicked.connect(on_clicked_apply)

        return settings_window

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

    def _get_key_sound(self) -> QSoundEffect:
        """
        Gets QSoundEffect object from the sound_filename preference which is to be played
        on each keystroke in the typing window.
        """

        key_sound_path = PATH_SOUNDS / self.get_preference("sound_filename")
        key_sound_url = QtCore.QUrl.fromLocalFile(str(key_sound_path))

        key_sound = QSoundEffect()
        key_sound.setSource(key_sound_url)
        key_sound.setVolume(0.4)
        key_sound.setLoopCount(1)
        return key_sound

    def _get_key_sounds_list(self) -> list[QSoundEffect]:
        """Returns a list of QSoundEffect objects."""

        if not self.get_preference("play_sound"):
            return [QSoundEffect()]

        return [self._get_key_sound() for _ in range(10)]

    def get_key_sounds_rotator(self) -> Generator[QSoundEffect, None, None]:
        """
        Returns a generator which will rotate through a list of QSoundEffect objects
        which are the sounds to be played on each user keystroke.

        This is necessary for faster typing speeds because the .play() method is static
        so the sound will not play on every keystroke like intended.
        """
        i = 0
        keysounds = self._get_key_sounds_list()
        length = len(keysounds)

        while True:
            i += 1
            if i == length:
                i = 0

            yield keysounds[i]

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
        main_window.showMaximized()
        main_window.setStyleSheet(main_window.stylesheet)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
