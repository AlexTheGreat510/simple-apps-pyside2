#! /usr/bin/python3


import sys
import random
import requests
import subprocess


from PySide2 import QtGui, QtCore, QtWidgets


class SimplePassword(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SimplePassword, self).__init__(parent)

        # APP-STYLE

        self.setStyleSheet("* { font-size: 15pt }")

        # APP-TITLE

        self.setWindowTitle("Simple Password")

        # APP-FIXEDSIZE

        self.setFixedSize(QtCore.QSize(500, 232))

        # APP-ICON

        self.setWindowIcon(QtGui.QIcon("icons/simple-password.png"))

        # APP-LAYOUT

        self.mainLayout = QtWidgets.QGridLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

        # APP-MENU-ACTION

        exit = QtWidgets.QAction("&Exit", self)
        restart = QtWidgets.QAction("&Restart", self)
        fontsize1 = QtWidgets.QAction("&10", self)
        fontsize2 = QtWidgets.QAction("&15", self)
        fontsize3 = QtWidgets.QAction("&20", self)
        fontsize4 = QtWidgets.QAction("&25", self)
        chooseFont = QtWidgets.QAction("&Choose Font", self)
        centerWindow = QtWidgets.QAction("Center Window", self)

        self.includeNumbers = QtWidgets.QAction("&Numbers", self)
        self.includeLChars = QtWidgets.QAction("&Lowercase Chars", self)
        self.includeUChars = QtWidgets.QAction("&Uppercase Chars", self)
        self.includeUFruits = QtWidgets.QAction("&Uppercase Fruits", self)

        # APP-MENU-TRIGGERED

        exit.triggered.connect(self.exitApp)
        restart.triggered.connect(self.restartApp)
        chooseFont.triggered.connect(self.selectFont)
        centerWindow.triggered.connect(self.centerWindow)

        fontsize1.triggered.connect(lambda : self.setFontSize(10))
        fontsize2.triggered.connect(lambda : self.setFontSize(15))
        fontsize3.triggered.connect(lambda : self.setFontSize(20))
        fontsize4.triggered.connect(lambda : self.setFontSize(25))

        self.includeLChars.triggered.connect(self.generatePassword)
        self.includeUChars.triggered.connect(self.generatePassword)
        self.includeNumbers.triggered.connect(self.generatePassword)
        self.includeUFruits.triggered.connect(self.generatePassword)

        # APP-MENU-CHECK

        self.includeLChars.setCheckable(True)
        self.includeUChars.setCheckable(True)
        self.includeNumbers.setCheckable(True)
        self.includeUFruits.setCheckable(True)
        self.includeLChars.setChecked(True)
        self.includeNumbers.setChecked(True)

        # APP-MENUBAR

        self.appMenu = self.menuBar()

        # APP-MENU-ADD

        self.fileMenu = self.appMenu.addMenu("&File")
        self.fileMenu.addAction(exit)
        self.fileMenu.addAction(restart)
        self.settingsMenu = self.appMenu.addMenu("&Settings")
        self.includeMenu = self.settingsMenu.addMenu("&Include")
        self.includeMenu.addAction(self.includeNumbers)
        self.includeMenu.addAction(self.includeLChars)
        self.includeMenu.addAction(self.includeUChars)
        self.includeMenu.addAction(self.includeUFruits)

        self.fontSizeMenu = self.settingsMenu.addMenu("&Font Size")
        self.fontSizeMenu.addAction(fontsize1)
        self.fontSizeMenu.addAction(fontsize2)
        self.fontSizeMenu.addAction(fontsize3)
        self.fontSizeMenu.addAction(fontsize4)
        self.settingsMenu.addAction(chooseFont)
        self.settingsMenu.addAction(centerWindow)

        # APP-ICON

        self.appIcon = QtWidgets.QLabel("")
        self.appIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.appIcon.setPixmap(QtGui.QPixmap("icons/simple-password.png"))
        self.mainLayout.addWidget(self.appIcon, 0, 0, 1, 2)

        # APP-LABEL

        self.appLabel = QtWidgets.QLabel("Simple Password")
        self.appLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appLabel.setStyleSheet("margin: 25px 0px; font-weight: bold")
        self.mainLayout.addWidget(self.appLabel, 1, 0, 1, 2)

        # APP-INPUT

        self.appInput = QtWidgets.QLineEdit()
        self.appInput.setReadOnly(True)
        self.appInput.setPlaceholderText("Password")
        self.appInput.setAlignment(QtCore.Qt.AlignCenter)
        self.appInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.appInput, 2, 0, 1, 2)

        # APP-SLIDER

        self.appSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.appSlider.setValue(30)
        self.appSlider.setMinimum(10)
        self.appSlider.setMaximum(100)
        self.appSlider.setTickInterval(10)
        self.appSlider.valueChanged.connect(self.generatePassword)
        self.appSlider.valueChanged.connect(self.updateSliderLabel)
        self.appSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.mainLayout.addWidget(self.appSlider, 3, 0)

        # APP-SLIDER-LABEL

        self.appSliderLabel = QtWidgets.QLabel(str(self.appSlider.value()))
        self.appSliderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.appSliderLabel, 3, 1)

        # APP-CENTER

        self.centerWindow()

        # APP-FUNCTION-RUN

        self.generatePassword()

    # APP-FUNCTIONS

    def exitApp(self):

        # EXIT-APP

        sys.exit(0)

    def restartApp(self):

        # RESTART-APP

        subprocess.run(["setsid", "-f", "python3", "simple-password.py"])
        self.exitApp()

    def centerWindow(self):

        # CENTER-WINDOW

        centerPoint = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        fg = self.frameGeometry()
        fg.moveCenter(centerPoint)
        self.move(fg.topLeft())

    def setFontSize(self, fontSize):

        # SET-FONT-SIZE

        self.setStyleSheet(" * { font-size: " + str(fontSize) + "pt } ")

    def selectFont(self):

        # FONT-DIALOG

        (ok, font) = QtWidgets.QFontDialog.getFont(QtGui.QFont("Ubuntu Mono", 10), self)

        # SET-CHOSEN-FONT

        if ok:
            for widget in self.findChildren(QtWidgets.QWidget):
                widget.setFont(font)

    def updateSliderLabel(self):

        # UPDATE-SLIDER-LABEL

        self.appSliderLabel.setText(str(self.appSlider.value()))

    def generatePassword(self):
        
        # PASS-INFO

        password = ""
        passChars = []
        passLength = self.appSlider.value()

        # NUMBERS

        if self.includeNumbers.isChecked():
            passChars += ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # LOWERCASE-CHARACTERS

        if self.includeLChars.isChecked():
            passChars += ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        # UPPERCASE-CHARACTERS

        if self.includeUChars.isChecked():
            passChars += ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        # UPPERCASE-FRUITS

        if self.includeUFruits.isChecked():
            passChars += ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi", "Lemon", "Mango", "Orange"]

        # IF-PASSCHAR-EMPTY

        if not passChars:
            self.appInput.setText("")
            return

        # GENERATE-PASSWORD

        for i in range(1, passLength):
            password += random.choice(passChars)

        # UPDATE-PASSINPUT

        self.appInput.setText(password)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simplePassword = SimplePassword()
    simplePassword.show()

    sys.exit(app.exec_())
