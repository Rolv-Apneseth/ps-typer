from PyQt5 import QtCore, QtWidgets

from source_ui import typing_window


class TypingWindow(QtWidgets.QWidget, typing_window.Ui_typingWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Multiple inheritance allows us to have the ui and window together so
        # setupui can be given self in for a window
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = TypingWindow()
    window.show()

    app.exec_()
