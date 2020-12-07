from PyQt5 import QtCore, QtWidgets

from source_ui import typing_window
from assets import texts


class TypingWindow(QtWidgets.QWidget, typing_window.Ui_typingWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Multiple inheritance allows us to have the ui and window together so
        # setupui can be given self in for a window
        self.setupUi(self)

        self.lineInput.textChanged.connect(self.on_input_text_changed)

    # Helper Functions
    def set_mode(self, mode):
        self.mode = mode

        if mode == "Common Phrases":
            self.labelMainText.setAlignment(QtCore.Qt.AlignCenter)

        self.text = texts._translate[mode]()
        self.labelMainText.setText(self.text)

    # def keyPressEvent(self, event):
    #     if event.key():
    #         print(event.key())

    # Button Functions
    def on_input_text_changed(self, input_text):
        print(input_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = TypingWindow()
    window.show()

    app.exec_()
