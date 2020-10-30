from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EasyWindow(object):
    """Pop up for an easy type test"""

    # GUI Functions
    def setupUi(self, EasyWindow):
        # fonts
        font1 = QtGui.QFont()
        font1.setFamily("Arial")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)

        font2 = QtGui.QFont()
        font2.setFamily("Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setUnderline(True)
        font2.setWeight(75)

        font3 = QtGui.QFont()
        font3.setFamily("Arial")
        font3.setPointSize(26)
        font3.setBold(True)
        font3.setWeight(75)

        # UI
        EasyWindow.setObjectName("EasyWindow")
        EasyWindow.resize(460, 260)
        self.centralwidget = QtWidgets.QWidget(EasyWindow)
        self.centralwidget.setObjectName("centralwidget")

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("assets/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        EasyWindow.setWindowIcon(icon)

        self.easy_input_frame = QtWidgets.QFrame(self.centralwidget)
        self.easy_input_frame.setGeometry(QtCore.QRect(10, 10, 440, 180))
        self.easy_input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.easy_input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.easy_input_frame.setObjectName("easy_input_frame")

        self.easy_label = QtWidgets.QLabel(self.easy_input_frame)
        self.easy_label.setGeometry(QtCore.QRect(10, 40, 420, 40))
        self.easy_label.setFont(font1)
        self.easy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.easy_label.setObjectName("easy_label")
        self.easy_label.setStyleSheet("color: green;")

        self.easy_title_label = QtWidgets.QLabel(self.easy_input_frame)
        self.easy_title_label.setGeometry(QtCore.QRect(20, 10, 400, 20))
        self.easy_title_label.setFont(font2)
        self.easy_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.easy_title_label.setObjectName("easy_title_label")

        self.easyLineEdit = QtWidgets.QLineEdit(self.easy_input_frame)
        self.easyLineEdit.setGeometry(QtCore.QRect(5, 90, 430, 80))
        self.easyLineEdit.setFont(font3)
        self.easyLineEdit.setInputMethodHints(
            QtCore.Qt.ImhLowercaseOnly
            | QtCore.Qt.ImhNoAutoUppercase
            | QtCore.Qt.ImhNoPredictiveText
        )
        self.easyLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.easyLineEdit.setObjectName("easyLineEdit")

        self.easy_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.easy_button_frame.setGeometry(QtCore.QRect(10, 200, 440, 40))
        self.easy_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.easy_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.easy_button_frame.setObjectName("easy_button_frame")

        self.easy_restart = QtWidgets.QPushButton(self.easy_button_frame)
        self.easy_restart.setGeometry(QtCore.QRect(350, 10, 75, 25))
        self.easy_restart.setObjectName("easy_restart")

        EasyWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EasyWindow)
        self.statusbar.setObjectName("statusbar")
        EasyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EasyWindow)
        QtCore.QMetaObject.connectSlotsByName(EasyWindow)

    def retranslateUi(self, EasyWindow):
        _translate = QtCore.QCoreApplication.translate
        EasyWindow.setWindowTitle(_translate("EasyWindow", "Typing Speed Test- Easy"))
        self.easy_label.setText(_translate("EasyWindow", "Placeholder Text"))
        self.easy_title_label.setText(
            _translate("EasyWindow", "Type out the following word down below:")
        )
        self.easy_restart.setText(_translate("EasyWindow", "Restart"))


# Can run to look at ui layout but fucntionality is included in main.py
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    EasyWindow = QtWidgets.QMainWindow()
    ui = Ui_EasyWindow()
    ui.setupUi(EasyWindow)
    EasyWindow.show()
    sys.exit(app.exec_())
