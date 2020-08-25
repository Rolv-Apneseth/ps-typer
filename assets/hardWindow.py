from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HardWindow(object):

    def setupUi(self, HardWindow):
        #Fonts
        font1 = QtGui.QFont()
        font1.setFamily("Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)

        font2 = QtGui.QFont()
        font2.setFamily("Arial")
        font2.setPointSize(12)

        #UI
        HardWindow.setObjectName("HardWindow")
        HardWindow.resize(980, 740)

        self.centralwidget = QtWidgets.QWidget(HardWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")

        self.hard_title_label = QtWidgets.QLabel(self.centralwidget)
        self.hard_title_label.setFont(font1)
        self.hard_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hard_title_label.setObjectName("hard_title_label")
        self.verticalLayout.addWidget(self.hard_title_label)

        self.hard_label = QtWidgets.QTextBrowser(self.centralwidget)
        self.hard_label.setFont(font2)
        self.hard_label.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.hard_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.hard_label.setObjectName("hard_label")
        self.verticalLayout.addWidget(self.hard_label)

        self.hard_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.hard_textEdit.setFont(font2)
        self.hard_textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.hard_textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.hard_textEdit.setMarkdown("")
        self.hard_textEdit.setPlaceholderText("")
        self.hard_textEdit.setObjectName("hard_textEdit")
        self.verticalLayout.addWidget(self.hard_textEdit)

        self.hard_restart = QtWidgets.QPushButton(self.centralwidget)
        self.hard_restart.setObjectName("hard_restart")
        self.verticalLayout.addWidget(self.hard_restart)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        HardWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HardWindow)
        self.statusbar.setObjectName("statusbar")
        HardWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HardWindow)
        QtCore.QMetaObject.connectSlotsByName(HardWindow)

    def retranslateUi(self, HardWindow):
        _translate = QtCore.QCoreApplication.translate
        HardWindow.setWindowTitle(_translate("HardWindow", "Typing Speed Test- Hard"))
        self.hard_title_label.setText(_translate("HardWindow", "Type out the following paragraph down below:"))
        self.hard_label.setHtml(_translate("HardWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">You think because he doesn’t love you that you are worthless. You think that because he doesn’t want you anymore that he is right — that his judgement and opinion of you are correct. If he throws you out, then you are garbage. You think he belongs to you because you want to belong to him. Don’t. It’s a bad word, ‘belong.’ Especially when you put it with somebody you love. Love shouldn’t be like that. Did you ever see the way the clouds love a mountain? They circle all around it; sometimes you can’t even see the mountain for the clouds. But you know what? You go up top and what do you see? His head. The clouds never cover the head. His head pokes through, beacuse the clouds let him; they don’t wrap him up. They let him keep his head up high, free, with nothing to hide him or bind him. You can’t own a human being. You can’t lose what you don’t own. Suppose you did own him. Could you really love somebody who was absolutely nobody without you? You really want somebody like that? Somebody who falls apart when you walk out the door? You don’t, do you? And neither does he. You’re turning over your whole life to him. Your whole life, girl. And if it means so little to you that you can just give it away, hand it to him, then why should it mean any more to him? He can’t value you more than you value yourself.</span></p></body></html>"))
        self.hard_textEdit.setStatusTip(_translate("HardWindow", "Type out the above paragraph, exactly as it is, here"))
        self.hard_textEdit.setHtml(_translate("HardWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.hard_restart.setText(_translate("HardWindow", "Restart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HardWindow = QtWidgets.QMainWindow()
    ui = Ui_HardWindow()
    ui.setupUi(HardWindow)
    HardWindow.show()
    sys.exit(app.exec_())
