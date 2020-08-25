from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_scoreWindow(object):
    def setupUi(self, scoreWindow):

        scoreWindow.setObjectName("scoreWindow")
        scoreWindow.resize(550, 130)
        self.centralwidget = QtWidgets.QWidget(scoreWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)

        self.score_frame1 = QtWidgets.QFrame(self.centralwidget)
        self.score_frame1.setGeometry(QtCore.QRect(15, 10, 521, 51))
        self.score_frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.score_frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.score_frame1.setObjectName("score_frame1")

        self.you_typed_label = QtWidgets.QLabel(self.score_frame1)
        self.you_typed_label.setGeometry(QtCore.QRect(10, 10, 491, 30))
        self.you_typed_label.setFont(font)
        self.you_typed_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.you_typed_label.setObjectName("you_typed_label")

        self.score_frame2 = QtWidgets.QFrame(self.centralwidget)
        self.score_frame2.setGeometry(QtCore.QRect(15, 70, 410, 40))
        self.score_frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.score_frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.score_frame2.setObjectName("score_frame2")

        self.outcome_label = QtWidgets.QLabel(self.score_frame2)
        self.outcome_label.setGeometry(QtCore.QRect(10, 10, 390, 20))
        self.outcome_label.setFont(font)
        self.outcome_label.setObjectName("outcome_label")

        self.score_frame3 = QtWidgets.QFrame(self.centralwidget)
        self.score_frame3.setGeometry(QtCore.QRect(435, 70, 100, 40))
        self.score_frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.score_frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.score_frame3.setObjectName("score_frame3")

        self.ok_button = QtWidgets.QPushButton(self.score_frame3)
        self.ok_button.setGeometry(QtCore.QRect(10, 5, 80, 30))
        self.ok_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_button.setObjectName("ok_button")

        scoreWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(scoreWindow)
        self.statusbar.setObjectName("statusbar")
        scoreWindow.setStatusBar(self.statusbar)

        self.retranslateUi(scoreWindow)
        QtCore.QMetaObject.connectSlotsByName(scoreWindow)

    def retranslateUi(self, scoreWindow):
        _translate = QtCore.QCoreApplication.translate
        scoreWindow.setWindowTitle(_translate("scoreWindow", "MainWindow"))
        self.you_typed_label.setText(_translate("scoreWindow", "You typed (x) words in (y) second(s) and your score was (z) w.p.m.!"))
        self.outcome_label.setText(_translate("scoreWindow", "No highscore was set. Better luck next time!"))
        self.ok_button.setStatusTip(_translate("scoreWindow", "Brings you back to the main menu"))
        self.ok_button.setText(_translate("scoreWindow", "OK"))

#Can run to look at ui layout but fucntionality is included in main.py
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    scoreWindow = QtWidgets.QMainWindow()
    ui = Ui_scoreWindow()
    ui.setupUi(scoreWindow)
    scoreWindow.show()
    sys.exit(app.exec_())
