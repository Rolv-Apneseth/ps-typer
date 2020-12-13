from PyQt5 import QtCore, QtWidgets

from source_ui import settings_window


class SettingsWindow(QtWidgets.QWidget, settings_window.Ui_settingsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

    # Helper functions
    def get_values(self):
        """Gets values entered by user for the different settings."""

        self.dark_mode = self.radioDarkMode.isChecked()  # False means light mode
        self.font_size = self.spinBoxPixel.value()  # Direct font px value
        self.key_sound = self.radioKeystrokeOn.isChecked()  # False means key sound off


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = SettingsWindow()
    window.show()

    app.exec_()
