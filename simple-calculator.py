#! /usr/bin/python3


import sys
import subprocess
from PySide2 import QtGui, QtCore, QtWidgets


class SimpleCalculator(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SimpleCalculator, self).__init__(parent)

        # CALC-STYLE

        self.setStyleSheet("* { font-size: 15pt }")

        # CALC-TITLE

        self.setWindowTitle("Simple Calculator")

        # CALC-FIXEDSIZE

        self.setFixedSize(QtCore.QSize(400, 382))

        # CALC-ICON

        self.setWindowIcon(QtGui.QIcon("icons/simple-calculator.png"))

        # CALC-LAYOUT

        self.mainLayout = QtWidgets.QGridLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

        # CALC-MENU

        exit = QtWidgets.QAction("&Exit", self)
        restart = QtWidgets.QAction("&Restart", self)

        fontsize1 = QtWidgets.QAction("&10", self)
        fontsize2 = QtWidgets.QAction("&15", self)
        fontsize3 = QtWidgets.QAction("&20", self)
        fontsize4 = QtWidgets.QAction("&25", self)
        chooseFont = QtWidgets.QAction("&Choose Font", self)
        centerWindow = QtWidgets.QAction("Center Window", self)
        resetHistory = QtWidgets.QAction("&Reset History", self)

        self.calcMenu = self.menuBar()

        exit.triggered.connect(self.exitApp)
        restart.triggered.connect(self.restartApp)

        chooseFont.triggered.connect(self.selectFont)
        centerWindow.triggered.connect(self.centerWindow)
        resetHistory.triggered.connect(self.resetCalcHistory)
        fontsize1.triggered.connect(lambda : self.setFontSize(10))
        fontsize2.triggered.connect(lambda : self.setFontSize(15))
        fontsize3.triggered.connect(lambda : self.setFontSize(20))
        fontsize4.triggered.connect(lambda : self.setFontSize(25))

        self.fileMenu = self.calcMenu.addMenu("&File")
        self.fileMenu.addAction(exit)
        self.fileMenu.addAction(restart)

        self.settingsMenu = self.calcMenu.addMenu("&Settings")
        self.fontSizeMenu = self.settingsMenu.addMenu("&Font Size")
        self.fontSizeMenu.addAction(fontsize1)
        self.fontSizeMenu.addAction(fontsize2)
        self.fontSizeMenu.addAction(fontsize3)
        self.fontSizeMenu.addAction(fontsize4)

        self.calcHistory = []
        self.calcHistoryCount = 0
        self.calcHistoryLimit = 10
        self.historyMenu = self.settingsMenu.addMenu("&History")
        self.settingsMenu.addAction(chooseFont)
        self.settingsMenu.addAction(resetHistory)
        self.settingsMenu.addAction(centerWindow)

        # CALC-ICON

        self.calcIcon = QtWidgets.QLabel("")
        self.calcIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.calcIcon.setPixmap(QtGui.QPixmap("icons/simple-calculator.png"))
        self.mainLayout.addWidget(self.calcIcon, 0, 0, 1, 4)

        # CALC-LABEL

        self.calcLabel = QtWidgets.QLabel("Simple Calculator")
        self.calcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.calcLabel.setStyleSheet("margin: 25px 0px; font-weight: bold;")
        self.mainLayout.addWidget(self.calcLabel, 1, 0, 1, 4)

        # CALC-INPUT

        self.calcInput = QtWidgets.QLineEdit()
        self.calcInput.setPlaceholderText("Expression")
        self.calcInput.setAlignment(QtCore.Qt.AlignCenter)
        self.calcInput.textChanged.connect(self.updateCalcAnswer)
        self.calcInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.calcInput, 2, 0, 1, 4)

        # CALC-BUTTONS-1

        self.calcButton1 = QtWidgets.QPushButton("1")
        self.calcButton2 = QtWidgets.QPushButton("2")
        self.calcButton3 = QtWidgets.QPushButton("3")
        self.calcButtonClear = QtWidgets.QPushButton("C")

        self.calcButton1.clicked.connect(self.addCalcInput)
        self.calcButton2.clicked.connect(self.addCalcInput)
        self.calcButton3.clicked.connect(self.addCalcInput)
        self.calcButtonClear.clicked.connect(self.addCalcInput)

        self.calcButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButton3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButtonClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.mainLayout.addWidget(self.calcButton1, 3, 0)
        self.mainLayout.addWidget(self.calcButton2, 3, 1)
        self.mainLayout.addWidget(self.calcButton3, 3, 2)
        self.mainLayout.addWidget(self.calcButtonClear, 3, 3)

        # CALC-BUTTONS-2

        self.calcButton4 = QtWidgets.QPushButton("4")
        self.calcButton5 = QtWidgets.QPushButton("5")
        self.calcButton6 = QtWidgets.QPushButton("6")
        self.calcButtonPlus = QtWidgets.QPushButton("+")

        self.calcButton4.clicked.connect(self.addCalcInput)
        self.calcButton5.clicked.connect(self.addCalcInput)
        self.calcButton6.clicked.connect(self.addCalcInput)
        self.calcButtonPlus.clicked.connect(self.addCalcInput)

        self.calcButton4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButton5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButton6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButtonPlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.mainLayout.addWidget(self.calcButton4, 4, 0)
        self.mainLayout.addWidget(self.calcButton5, 4, 1)
        self.mainLayout.addWidget(self.calcButton6, 4, 2)
        self.mainLayout.addWidget(self.calcButtonPlus, 4, 3)

        # CALC-BUTTONS-3

        self.calcButton7 = QtWidgets.QPushButton("7")
        self.calcButton8 = QtWidgets.QPushButton("8")
        self.calcButton9 = QtWidgets.QPushButton("9")
        self.calcButtonMinus = QtWidgets.QPushButton("-")

        self.calcButton7.clicked.connect(self.addCalcInput)
        self.calcButton8.clicked.connect(self.addCalcInput)
        self.calcButton9.clicked.connect(self.addCalcInput)
        self.calcButtonMinus.clicked.connect(self.addCalcInput)

        self.calcButton7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButton8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButton9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButtonMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.mainLayout.addWidget(self.calcButton7, 5, 0)
        self.mainLayout.addWidget(self.calcButton8, 5, 1)
        self.mainLayout.addWidget(self.calcButton9, 5, 2)
        self.mainLayout.addWidget(self.calcButtonMinus, 5, 3)

        # CALC-BUTTONS-4

        self.calcButton0 = QtWidgets.QPushButton("0")
        self.calcButtonDivide = QtWidgets.QPushButton("/")
        self.calcButtonMultiply = QtWidgets.QPushButton("*")
        self.calcButtonRemainder = QtWidgets.QPushButton("%")

        self.calcButton0.clicked.connect(self.addCalcInput)
        self.calcButtonDivide.clicked.connect(self.addCalcInput)
        self.calcButtonMultiply.clicked.connect(self.addCalcInput)
        self.calcButtonRemainder.clicked.connect(self.addCalcInput)

        self.calcButton0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButtonDivide.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButtonMultiply.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calcButtonRemainder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.mainLayout.addWidget(self.calcButtonDivide, 6, 0)
        self.mainLayout.addWidget(self.calcButtonRemainder, 6, 1)
        self.mainLayout.addWidget(self.calcButtonMultiply, 6, 2)
        self.mainLayout.addWidget(self.calcButton0, 6, 3)

        # CALC-ANSWER

        self.calcAnswer = QtWidgets.QLineEdit()
        self.calcAnswer.setReadOnly(True)
        self.calcAnswer.setPlaceholderText("0")
        self.calcAnswer.setAlignment(QtCore.Qt.AlignCenter)
        self.calcAnswer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.calcAnswer, 7, 0, 1, 2)

        # CALC-EQUAL-BTN

        self.calcButtonEqual = QtWidgets.QPushButton("=")
        self.calcButtonEqual.clicked.connect(self.addCalcInput)
        self.calcButtonEqual.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.calcButtonEqual, 7, 2, 1, 2)

        # CALC-CENTER

        self.centerWindow()

    # ┏━╸╻ ╻┏┓╻┏━╸╺┳╸╻┏━┓┏┓╻┏━┓
    # ┣╸ ┃ ┃┃┗┫┃   ┃ ┃┃ ┃┃┗┫┗━┓
    # ╹  ┗━┛╹ ╹┗━╸ ╹ ╹┗━┛╹ ╹┗━┛

    def exitApp(self):
        sys.exit(0)

    def restartApp(self):
        subprocess.run(["setsid", "-f", "python3", "simple-calculator.py"])
        self.exitApp()

    def setFontSize(self, fontSize):
        self.setStyleSheet(" * { font-size: " + str(fontSize) + "pt } ")

    def resetCalcHistory(self):
        self.calcHistory.clear()
        self.historyMenu.clear()

    def updateCalcAnswer(self):

        # CALC-TEXT

        calcText = self.calcInput.text()

        # UPDATE-CALC-ANSWER

        if calcText:
            self.calcAnswer.setText(str(eval(calcText)))

    def selectFont(self):

        # FONT-DIALOG

        (ok, font) = QtWidgets.QFontDialog.getFont(QtGui.QFont("Ubuntu Mono", 10), self)

        # SET-CHOSEN-FONT

        if ok:
            for widget in self.findChildren(QtWidgets.QWidget):
                widget.setFont(font)

    def centerWindow(self):

        # CENTER-WINDOW

        centerPoint = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        fg = self.frameGeometry()
        fg.moveCenter(centerPoint)
        self.move(fg.topLeft())

    def addCalcHistory(self):

        # ADD-CALC-HISTORY

        if (self.calcHistoryLimit>=self.calcHistoryCount):
            history = self.calcInput.text()

            if history and history not in self.calcHistory:
                self.calcHistory.append(history)
                self.historyAction = QtWidgets.QAction(history, self)
                self.historyAction.triggered.connect(lambda: self.calcInput.setText(history))
                self.historyMenu.addAction(self.historyAction)

        # UPDATE-CALC-HISTORY-COUNT

        self.calcHistoryCount += 1

    def addCalcInput(self):

        # BUTTON-TEXT

        buttonText = self.sender().text()

        # UPDATE-CALC-INPUT

        if (buttonText == '+' or buttonText == '-' or buttonText == '*' or buttonText == '/' or buttonText == '%'):
            self.calcInput.setText(self.calcInput.text() + ' ' + buttonText + ' ')

        elif (buttonText == 'C'):
            self.calcInput.setText('')

        elif (buttonText == '='):
            self.addCalcHistory()
            self.calcInput.setText(str(eval(self.calcInput.text())))

        else:
            self.calcInput.setText(self.calcInput.text() + buttonText)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleCalculator = SimpleCalculator()
    simpleCalculator.show()

    sys.exit(app.exec_())
