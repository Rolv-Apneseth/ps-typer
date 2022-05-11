from PyQt5 import QtWidgets

from ps_typer.ui import results_window


class ResultsWindow(QtWidgets.QWidget, results_window.Ui_resultWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
