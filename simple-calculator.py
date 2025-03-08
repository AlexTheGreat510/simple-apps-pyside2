from PySide2 import QtCore, QtWidgets


class SimpleCalculator(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SimpleCalculator, self).__init__(parent)

        # CALC-TITLE
        self.setWindowTitle("Simple Calculator")

        # CALC-LAYOUT
        self.mainLayout = QtWidgets.QGridLayout()
        self.setLayout(self.mainLayout)

        # CALC-INPUT
        self.calcInput = QtWidgets.QLineEdit()
        self.calcInput.setReadOnly(True)
        self.calcInput.setPlaceholderText("EXPRESSION")
        self.calcInput.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.calcInput, 0, 0, 1, 4)

        # CALC-BUTTONS-1

        self.calcButton1 = QtWidgets.QPushButton("1")
        self.calcButton2 = QtWidgets.QPushButton("2")
        self.calcButton3 = QtWidgets.QPushButton("3")
        self.calcButtonClear = QtWidgets.QPushButton("C")

        self.calcButton1.clicked.connect(self.addCalcInput)
        self.calcButton2.clicked.connect(self.addCalcInput)
        self.calcButton3.clicked.connect(self.addCalcInput)
        self.calcButtonClear.clicked.connect(self.addCalcInput)

        self.mainLayout.addWidget(self.calcButton1, 1, 0)
        self.mainLayout.addWidget(self.calcButton2, 1, 1)
        self.mainLayout.addWidget(self.calcButton3, 1, 2)
        self.mainLayout.addWidget(self.calcButtonClear, 1, 3)

        # CALC-BUTTONS-2

        self.calcButton4 = QtWidgets.QPushButton("4")
        self.calcButton5 = QtWidgets.QPushButton("5")
        self.calcButton6 = QtWidgets.QPushButton("6")
        self.calcButtonPlus = QtWidgets.QPushButton("+")

        self.calcButton4.clicked.connect(self.addCalcInput)
        self.calcButton5.clicked.connect(self.addCalcInput)
        self.calcButton6.clicked.connect(self.addCalcInput)
        self.calcButtonPlus.clicked.connect(self.addCalcInput)

        self.mainLayout.addWidget(self.calcButton4, 2, 0)
        self.mainLayout.addWidget(self.calcButton5, 2, 1)
        self.mainLayout.addWidget(self.calcButton6, 2, 2)
        self.mainLayout.addWidget(self.calcButtonPlus, 2, 3)

        # CALC-BUTTONS-3

        self.calcButton1 = QtWidgets.QPushButton("7")
        self.calcButton2 = QtWidgets.QPushButton("8")
        self.calcButton3 = QtWidgets.QPushButton("9")
        self.calcButtonMinus = QtWidgets.QPushButton("-")

        self.calcButton1.clicked.connect(self.addCalcInput)
        self.calcButton2.clicked.connect(self.addCalcInput)
        self.calcButton3.clicked.connect(self.addCalcInput)
        self.calcButtonMinus.clicked.connect(self.addCalcInput)

        self.mainLayout.addWidget(self.calcButton1, 3, 0)
        self.mainLayout.addWidget(self.calcButton2, 3, 1)
        self.mainLayout.addWidget(self.calcButton3, 3, 2)
        self.mainLayout.addWidget(self.calcButtonMinus, 3, 3)

        # CALC-BUTTONS-4

        self.calcButtonDivide = QtWidgets.QPushButton("/")
        self.calcButtonRemainder = QtWidgets.QPushButton("%")
        self.calcButtonMultiply = QtWidgets.QPushButton("*")
        self.calcButtonEqual = QtWidgets.QPushButton("=")

        self.calcButtonDivide.clicked.connect(self.addCalcInput)
        self.calcButtonRemainder.clicked.connect(self.addCalcInput)
        self.calcButtonMultiply.clicked.connect(self.addCalcInput)
        self.calcButtonEqual.clicked.connect(self.addCalcInput)

        self.mainLayout.addWidget(self.calcButtonDivide, 4, 0)
        self.mainLayout.addWidget(self.calcButtonRemainder, 4, 1)
        self.mainLayout.addWidget(self.calcButtonMultiply, 4, 2)
        self.mainLayout.addWidget(self.calcButtonEqual, 4, 3)

    def addCalcInput(self):
        buttonText = self.sender().text()

        if (buttonText == '+' or buttonText == '-' or buttonText == '*' or buttonText == '/' or buttonText == '%'):
            self.calcInput.setText(self.calcInput.text() + ' ' + buttonText + ' ')

        elif (buttonText == '='):
            self.calcInput.setText(str(eval(self.calcInput.text())))

        elif (buttonText == 'C'):
            self.calcInput.setText('')

        else:
            self.calcInput.setText(self.calcInput.text() + buttonText)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleCalculator = SimpleCalculator()
    simpleCalculator.show()

    sys.exit(app.exec_())
