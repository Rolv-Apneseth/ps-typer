from PyQt5 import QtWidgets

from ps_typer.source_ui import result_window


class ResultsWindow(QtWidgets.QWidget, result_window.Ui_resultWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.buttonNext.setFocus()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = ResultsWindow()
    window.show()

    app.exec_()
