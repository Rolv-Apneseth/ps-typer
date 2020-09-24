from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MediumWindow(object):
    """Pop up for a medium type test"""

    def setupUi(self, MediumWindow):

        #fonts
        font1 = QtGui.QFont()
        font1.setFamily("Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setUnderline(True)

        font2 = QtGui.QFont()
        font2.setFamily("Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)

        #UI
        MediumWindow.setObjectName("MediumWindow")
        MediumWindow.resize(460, 260)
        self.centralwidget = QtWidgets.QWidget(MediumWindow)
        self.centralwidget.setObjectName("centralwidget")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MediumWindow.setWindowIcon(icon)

        self.medium_input_frame = QtWidgets.QFrame(self.centralwidget)
        self.medium_input_frame.setGeometry(QtCore.QRect(10, 10, 440, 180))
        self.medium_input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.medium_input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.medium_input_frame.setObjectName("medium_input_frame")

        self.medium_title_label = QtWidgets.QLabel(self.medium_input_frame)
        self.medium_title_label.setGeometry(QtCore.QRect(20, 10, 400, 20))
        self.medium_title_label.setFont(font1)
        self.medium_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.medium_title_label.setObjectName("medium_title_label")

        self.mediumLineEdit = QtWidgets.QLineEdit(self.medium_input_frame)
        self.mediumLineEdit.setGeometry(QtCore.QRect(5, 90, 430, 80))
        self.mediumLineEdit.setFont(font2)
        self.mediumLineEdit.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.mediumLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mediumLineEdit.setObjectName("mediumLineEdit")

        self.medium_label = QtWidgets.QLabel(self.medium_input_frame)
        self.medium_label.setGeometry(QtCore.QRect(10, 40, 420, 40))
        self.medium_label.setFont(font2)
        self.medium_label.setAlignment(QtCore.Qt.AlignCenter)
        self.medium_label.setObjectName("medium_label")
        self.medium_label.setStyleSheet("color: green;")

        self.medium_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.medium_button_frame.setGeometry(QtCore.QRect(10, 200, 440, 40))
        self.medium_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.medium_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.medium_button_frame.setObjectName("medium_button_frame")

        self.medium_restart = QtWidgets.QPushButton(self.medium_button_frame)
        self.medium_restart.setGeometry(QtCore.QRect(350, 10, 75, 25))
        self.medium_restart.setObjectName("medium_restart")

        MediumWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MediumWindow)
        self.statusbar.setObjectName("statusbar")
        MediumWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MediumWindow)
        QtCore.QMetaObject.connectSlotsByName(MediumWindow)

    def retranslateUi(self, MediumWindow):
        _translate = QtCore.QCoreApplication.translate
        MediumWindow.setWindowTitle(_translate("MediumWindow", "Typing Speed Test- Medium"))
        self.medium_label.setText(_translate("MediumWindow", "Placeholder text"))
        self.medium_title_label.setText(_translate("MediumWindow", "Type out the following phrase down below:"))
        self.medium_restart.setText(_translate("MediumWindow", "Restart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MediumWindow = QtWidgets.QMainWindow()
    ui = Ui_MediumWindow()
    ui.setupUi(MediumWindow)
    MediumWindow.show()
    sys.exit(app.exec_())
