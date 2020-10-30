from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Fonts
        font1 = QtGui.QFont()
        font1.setFamily("Arial Black")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)

        font2 = QtGui.QFont()
        font2.setFamily("Arial")
        font2.setPointSize(10)

        font3 = QtGui.QFont()
        font3.setFamily("Arial")
        font3.setPointSize(10)
        font3.setUnderline(True)

        font4 = QtGui.QFont()
        font4.setFamily("Arial")

        font5 = QtGui.QFont()
        font5.setFamily("Arial Black")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setUnderline(True)
        font5.setWeight(75)

        # UI
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 189)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("assets/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)

        # HIGHSCORE FRAME
        self.highscore_frame = QtWidgets.QFrame(self.centralwidget)
        self.highscore_frame.setGeometry(QtCore.QRect(20, 30, 170, 120))
        self.highscore_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.highscore_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.highscore_frame.setObjectName("highscore_frame")

        self.highscore_label = QtWidgets.QLabel(self.highscore_frame)
        self.highscore_label.setGeometry(QtCore.QRect(20, 0, 141, 41))

        self.highscore_label.setFont(font1)
        self.highscore_label.setScaledContents(False)
        self.highscore_label.setAlignment(QtCore.Qt.AlignCenter)
        self.highscore_label.setObjectName("highscore_label")

        self.all_time_highscore = QtWidgets.QLabel(self.highscore_frame)
        self.all_time_highscore.setGeometry(QtCore.QRect(85, 80, 50, 20))

        self.all_time_highscore.setFont(font2)
        self.all_time_highscore.setAlignment(QtCore.Qt.AlignCenter)
        self.all_time_highscore.setObjectName("all_time_highscore")

        self.today_label = QtWidgets.QLabel(self.highscore_frame)
        self.today_label.setGeometry(QtCore.QRect(40, 45, 40, 20))

        self.today_label.setFont(font3)
        self.today_label.setStatusTip("")
        self.today_label.setAlignment(QtCore.Qt.AlignCenter)
        self.today_label.setObjectName("today_label")

        self.today_highscore = QtWidgets.QLabel(self.highscore_frame)
        self.today_highscore.setGeometry(QtCore.QRect(80, 45, 50, 20))
        self.today_highscore.setFont(font2)
        self.today_highscore.setAlignment(QtCore.Qt.AlignCenter)
        self.today_highscore.setObjectName("today_highscore")

        self.all_time_label = QtWidgets.QLabel(self.highscore_frame)
        self.all_time_label.setGeometry(QtCore.QRect(35, 80, 50, 20))
        self.all_time_label.setFont(font3)
        self.all_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.all_time_label.setObjectName("all_time_label")

        # DIFFICULTY FRAME
        self.difficulty_frame = QtWidgets.QFrame(self.centralwidget)
        self.difficulty_frame.setGeometry(QtCore.QRect(210, 30, 300, 120))
        self.difficulty_frame.setStatusTip("")
        self.difficulty_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.difficulty_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.difficulty_frame.setObjectName("difficulty_frame")

        self.choose_label = QtWidgets.QLabel(self.difficulty_frame)
        self.choose_label.setGeometry(QtCore.QRect(70, 10, 170, 20))
        self.choose_label.setFont(font5)
        self.choose_label.setObjectName("choose_label")

        # Buttons
        self.begin_button = QtWidgets.QPushButton(self.difficulty_frame)
        self.begin_button.setGeometry(QtCore.QRect(100, 80, 100, 30))
        self.begin_button.setFont(font4)
        self.begin_button.setObjectName("begin_button")
        self.begin_button.clicked.connect(
            lambda: self.begin(
                self.easy_radio.isChecked(), self.medium_radio.isChecked()
            )
        )

        self.hard_radio = QtWidgets.QRadioButton(self.difficulty_frame)
        self.hard_radio.setGeometry(QtCore.QRect(220, 45, 41, 18))
        self.hard_radio.setFont(font4)
        self.hard_radio.setObjectName("hard_radio")

        self.medium_radio = QtWidgets.QRadioButton(self.difficulty_frame)
        self.medium_radio.setGeometry(QtCore.QRect(120, 45, 61, 18))
        self.medium_radio.setFont(font4)
        self.medium_radio.setChecked(True)
        self.medium_radio.setObjectName("medium_radio")

        self.easy_radio = QtWidgets.QRadioButton(self.difficulty_frame)
        self.easy_radio.setGeometry(QtCore.QRect(30, 45, 45, 20))
        self.easy_radio.setFont(font4)
        self.easy_radio.setChecked(False)
        self.easy_radio.setObjectName("easy_radio")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typing Speed Tester"))
        self.highscore_label.setText(_translate("MainWindow", "Highscores:"))
        self.all_time_highscore.setText(_translate("MainWindow", "00 wpm"))
        self.today_label.setText(_translate("MainWindow", "Today:"))
        self.today_highscore.setText(_translate("MainWindow", "00 wpm"))
        self.all_time_label.setStatusTip(
            _translate("MainWindow", "Can be reset by deleting All_Time.txt")
        )
        self.all_time_label.setText(_translate("MainWindow", "All time:"))
        self.begin_button.setStatusTip(
            _translate("MainWindow", "Pops up a new window with the actual typing test")
        )
        self.begin_button.setText(_translate("MainWindow", "Begin Speed Test"))
        self.hard_radio.setStatusTip(
            _translate(
                "MainWindow",
                "Type out long paragraphs, either paragraphs from famous books or famous quotes",
            )
        )
        self.hard_radio.setText(_translate("MainWindow", "Hard"))
        self.medium_radio.setStatusTip(
            _translate("MainWindow", "Type some common English expressions/sayings")
        )
        self.medium_radio.setText(_translate("MainWindow", "Medium"))
        self.easy_radio.setStatusTip(
            _translate("MainWindow", "Type some of the most common English words")
        )
        self.easy_radio.setText(_translate("MainWindow", "Easy"))
        self.choose_label.setText(_translate("MainWindow", "Choose a difficulty"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
