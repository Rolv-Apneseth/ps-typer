from PyQt5 import QtCore, QtWidgets

from source_ui import stats_window


class StatsWindow(QtWidgets.QWidget, stats_window.Ui_statsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = StatsWindow()
    window.show()

    app.exec_()
