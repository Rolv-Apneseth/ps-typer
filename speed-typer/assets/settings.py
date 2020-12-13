from PyQt5 import QtCore, QtWidgets

from source_ui import settings_window


class SettingsWindow(QtWidgets.QWidget, settings_window.Ui_settingsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = SettingsWindow()
    window.show()

    app.exec_()
