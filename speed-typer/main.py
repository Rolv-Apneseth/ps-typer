from PyQt5 import QtCore, QtWidgets

import type_test
from source_ui import main_window


class MainWindow(QtWidgets.QWidget, main_window.Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Multiple inheritance allows us to have the ui and window together so
        # setupui can be given self in for a window
        self.setupUi(self)

        self.buttonStart.clicked.connect(self.on_clicked_start)

    # Button Functions
    def on_clicked_start(self):
        self.make_mode_window(str(self.comboBoxSelectMode.currentText()))

        self.mode_window.show()

        self.hide()

    def on_clicked_back(self):
        self.show()

        self.mode_window.close()
        del self.mode_window

    # Helper Functions
    def make_mode_window(self, mode):
        self.mode_window = type_test.TypingWindow()

        self.mode_window.buttonBack.clicked.connect(self.on_clicked_back)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
