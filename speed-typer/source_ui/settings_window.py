# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsWindow(object):
    def setupUi(self, settingsWindow):
        settingsWindow.setObjectName("settingsWindow")
        settingsWindow.resize(730, 437)
        settingsWindow.setStyleSheet("QWidget {\n"
"    background: rgb(50, 50, 50);\n"
"    color: rgb(235, 235, 235);\n"
"    font-size: 24pt;\n"
"}\n"
"\n"
"QFrame {    \n"
"    border: 1px solid rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton, QComboBox {    \n"
"    background: rgb(70, 70, 70);\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton::hover, QComboBox::hover {\n"
"    background: rgb(90, 90, 90)\n"
"}\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame[frameShape=\"4\"] {\n"
"    background-color: rgb(235, 235, 235);\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(settingsWindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.frameDisplay = QtWidgets.QFrame(settingsWindow)
        self.frameDisplay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDisplay.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDisplay.setObjectName("frameDisplay")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameDisplay)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelDisplay = QtWidgets.QLabel(self.frameDisplay)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelDisplay.setFont(font)
        self.labelDisplay.setStyleSheet("font-weight: bold; font-size: 28pt;")
        self.labelDisplay.setObjectName("labelDisplay")
        self.verticalLayout.addWidget(self.labelDisplay)
        self.line = QtWidgets.QFrame(self.frameDisplay)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioDarkMode = QtWidgets.QRadioButton(self.frameDisplay)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.radioDarkMode.setFont(font)
        self.radioDarkMode.setChecked(True)
        self.radioDarkMode.setAutoExclusive(True)
        self.radioDarkMode.setObjectName("radioDarkMode")
        self.horizontalLayout.addWidget(self.radioDarkMode)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.radioLightMode = QtWidgets.QRadioButton(self.frameDisplay)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.radioLightMode.setFont(font)
        self.radioLightMode.setAutoExclusive(True)
        self.radioLightMode.setObjectName("radioLightMode")
        self.horizontalLayout.addWidget(self.radioLightMode)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frameDisplay)
        self.frameAudio = QtWidgets.QFrame(settingsWindow)
        self.frameAudio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAudio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAudio.setObjectName("frameAudio")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameAudio)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelAudio = QtWidgets.QLabel(self.frameAudio)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelAudio.setFont(font)
        self.labelAudio.setStyleSheet("font-weight: bold; font-size: 28pt;")
        self.labelAudio.setObjectName("labelAudio")
        self.verticalLayout_2.addWidget(self.labelAudio)
        self.line_2 = QtWidgets.QFrame(self.frameAudio)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelKeystrokeSounds = QtWidgets.QLabel(self.frameAudio)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelKeystrokeSounds.setFont(font)
        self.labelKeystrokeSounds.setObjectName("labelKeystrokeSounds")
        self.horizontalLayout_3.addWidget(self.labelKeystrokeSounds)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.radioKeystrokeOn = QtWidgets.QRadioButton(self.frameAudio)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.radioKeystrokeOn.setFont(font)
        self.radioKeystrokeOn.setChecked(True)
        self.radioKeystrokeOn.setObjectName("radioKeystrokeOn")
        self.horizontalLayout_3.addWidget(self.radioKeystrokeOn)
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.radioKeystrokeOff = QtWidgets.QRadioButton(self.frameAudio)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.radioKeystrokeOff.setFont(font)
        self.radioKeystrokeOff.setObjectName("radioKeystrokeOff")
        self.horizontalLayout_3.addWidget(self.radioKeystrokeOff)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelSelectSound = QtWidgets.QLabel(self.frameAudio)
        self.labelSelectSound.setObjectName("labelSelectSound")
        self.horizontalLayout_2.addWidget(self.labelSelectSound)
        self.comboSelectSound = QtWidgets.QComboBox(self.frameAudio)
        self.comboSelectSound.setObjectName("comboSelectSound")
        self.horizontalLayout_2.addWidget(self.comboSelectSound)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem10)
        self.verticalLayout_3.addWidget(self.frameAudio)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonMainMenu = QtWidgets.QPushButton(settingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonMainMenu.sizePolicy().hasHeightForWidth())
        self.buttonMainMenu.setSizePolicy(sizePolicy)
        self.buttonMainMenu.setObjectName("buttonMainMenu")
        self.horizontalLayout_4.addWidget(self.buttonMainMenu)
        self.buttonApply = QtWidgets.QPushButton(settingsWindow)
        self.buttonApply.setDefault(True)
        self.buttonApply.setObjectName("buttonApply")
        self.horizontalLayout_4.addWidget(self.buttonApply)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)

        self.retranslateUi(settingsWindow)
        QtCore.QMetaObject.connectSlotsByName(settingsWindow)

    def retranslateUi(self, settingsWindow):
        _translate = QtCore.QCoreApplication.translate
        settingsWindow.setWindowTitle(_translate("settingsWindow", "Settings"))
        self.labelDisplay.setText(_translate("settingsWindow", "Display"))
        self.radioDarkMode.setText(_translate("settingsWindow", "Dark Mode"))
        self.radioLightMode.setText(_translate("settingsWindow", "Light Mode"))
        self.labelAudio.setText(_translate("settingsWindow", "Audio"))
        self.labelKeystrokeSounds.setText(_translate("settingsWindow", "Keystroke sounds: "))
        self.radioKeystrokeOn.setText(_translate("settingsWindow", "On"))
        self.radioKeystrokeOff.setText(_translate("settingsWindow", "Off"))
        self.labelSelectSound.setText(_translate("settingsWindow", "Select sound "))
        self.buttonMainMenu.setText(_translate("settingsWindow", "Main Menu"))
        self.buttonApply.setText(_translate("settingsWindow", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settingsWindow = QtWidgets.QWidget()
    ui = Ui_settingsWindow()
    ui.setupUi(settingsWindow)
    settingsWindow.show()
    sys.exit(app.exec_())
