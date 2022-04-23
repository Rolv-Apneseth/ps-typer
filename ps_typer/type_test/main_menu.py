from PyQt5 import QtWidgets

from ps_typer.ui.main_menu import Ui_mainMenu


class MainMenu(QtWidgets.QWidget, Ui_mainMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
