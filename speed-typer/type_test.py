from PyQt5 import QtCore, QtWidgets
from time import perf_counter

from source_ui import typing_window
from assets import texts, results


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
        self.buttonNewText.clicked.connect(self.on_clicked_new)

        # timer
        self.start_time = None

    # Helper Functions
    def set_mode(self, mode):
        self.mode = mode

        if mode == "Common Phrases":
            self.labelMainText.setAlignment(QtCore.Qt.AlignCenter)

        self.text = texts._translate[mode]()
        self.labelMainText.setText(self.text)

    def set_stats(self, input_text):
        correct = 0
        for i, character in enumerate(input_text):
            if character == self.text[i]:
                correct += 1

        self.accuracy = int(correct / len(self.text) * 100)

        seconds = perf_counter() - self.start_time
        self.wpm = int((len(self.text) / 5) / (seconds / 60))

    def make_results_window(self):
        self.results_window = results.ResultsWindow()

        self.results_window.labelAccuracy.setText(f"Accuracy: {str(self.accuracy)}%")
        self.results_window.labelSpeed.setText(f"Speed:    {str(self.wpm)}wpm!")

    def on_finished(self, input_text):
        self.set_stats(input_text)

        self.make_results_window()

        self.hide()
        self.results_window.show()

    # def keyPressEvent(self, event):
    #     if event.key():
    #         print(event.key())

    # Button Functions
    def on_clicked_new(self):
        self.start_time = None
        self.set_mode(self.mode)
        self.lineInput.clear()

    def on_input_text_changed(self, input_text: str) -> None:
        """Updates background of each letter as user types and calls a function when
        the user is finished.
        """
        if not self.start_time:
            self.start_time = perf_counter()

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
