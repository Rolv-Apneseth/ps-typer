from PyQt5 import QtCore, QtWidgets

from source_ui import typing_window
from assets import texts


# Constants
GREEN = "rgb(0, 75, 0)"
RED = "rgb(125, 0, 0)"


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

    def on_finished(self, input_text):
        pass

    # def keyPressEvent(self, event):
    #     if event.key():
    #         print(event.key())

    # Button Functions
    def on_input_text_changed(self, input_text: str) -> None:
        """Updates background of each letter as user types and calls a function when
        the user is finished.
        """

        typed_text = []
        rest_of_text = self.text[len(input_text) :]

        for i, character in enumerate(input_text):
            if self.text[i] == character:
                typed_text.append(
                    f'<span style="background-color:{GREEN};">{self.text[i]}</span>'
                )
            else:
                typed_text.append(
                    f'<span style="background-color:{RED};">{self.text[i]}</span>'
                )

        rich_text = (
            "<html><head/><body><p>"
            f'{"".join(typed_text)}'
            f"{rest_of_text}</p></body></html>"
        )
        self.labelMainText.setText(rich_text)

        if len(input_text) == len(self.text):
            self.on_finished(input_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = TypingWindow()
    window.show()

    app.exec_()
