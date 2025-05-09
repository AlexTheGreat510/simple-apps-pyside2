#! /usr/bin/python3


import sys
import requests
import subprocess
from PySide2 import QtGui, QtCore, QtWidgets


class SimpleTictactoe(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SimpleTictactoe, self).__init__(parent)

        # GAME-INFO

        self.player1 = 'X'
        self.player2 = 'O'
        self.player1Score = 0
        self.player2Score = 0
        self.currentPlayer = self.player1

        # GAME-STYLES

        self.setStyleSheet("""* {
                                    font-size: 25pt;
                              }

                              QLabel {
                                    margin: 25px 0px;
                                    font-weight: bold;
                              }

                              QPushButton {
                                    color: gray;
                                    padding: 50px;
                              }""")

        # GAME-TITLE

        self.setWindowTitle("Simple Tictactoe")

        # GAME-FIXEDSIZE

        self.setFixedSize(QtCore.QSize(399, 690))

        # GAME-ICON

        self.setWindowIcon(QtGui.QIcon("icons/simple-search.png"))

        # GAME-LAYOUT

        self.mainLayout = QtWidgets.QGridLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

        # GAME-MENU-ACTION

        exit = QtWidgets.QAction("&Exit", self)
        fontsize1 = QtWidgets.QAction("&10", self)
        fontsize2 = QtWidgets.QAction("&15", self)
        fontsize3 = QtWidgets.QAction("&20", self)
        fontsize4 = QtWidgets.QAction("&25", self)
        restart = QtWidgets.QAction("&Restart", self)
        resetAll = QtWidgets.QAction("Reset All", self)
        chooseFont = QtWidgets.QAction("&Choose Font", self)
        resetScores = QtWidgets.QAction("Reset Scores", self)
        resetButtons = QtWidgets.QAction("Reset Buttons", self)
        centerWindow = QtWidgets.QAction("Center Window", self)
        resetPlayer1Score = QtWidgets.QAction("Reset Player1 Scores", self)
        resetPlayer2Score = QtWidgets.QAction("Reset Player2 Scores", self)

        # GAME-MENU-TRIGGERED

        exit.triggered.connect(self.exitApp)
        restart.triggered.connect(self.restartApp)
        resetAll.triggered.connect(self.resetGameAll)
        chooseFont.triggered.connect(self.selectFont)
        centerWindow.triggered.connect(self.centerWindow)
        resetScores.triggered.connect(self.resetGameScores)
        resetButtons.triggered.connect(self.resetGameButtons)
        fontsize1.triggered.connect(lambda : self.setFontSize(10))
        fontsize2.triggered.connect(lambda : self.setFontSize(15))
        fontsize3.triggered.connect(lambda : self.setFontSize(20))
        fontsize4.triggered.connect(lambda : self.setFontSize(25))
        resetPlayer1Score.triggered.connect(self.resetPlayer1Score)
        resetPlayer2Score.triggered.connect(self.resetPlayer2Score)

        # GAME-MENUBAR

        self.gameMenu = self.menuBar()

        # GAME-MENU-ADD

        self.fileMenu = self.gameMenu.addMenu("&File")
        self.fileMenu.addAction(exit)
        self.fileMenu.addAction(restart)
        self.settingsMenu = self.gameMenu.addMenu("&Settings")
        self.resetMenu = self.settingsMenu.addMenu("&Reset")
        self.resetMenu.addAction(resetAll)
        self.resetMenu.addAction(resetScores)
        self.resetMenu.addAction(resetButtons)
        self.resetMenu.addAction(resetPlayer1Score)
        self.resetMenu.addAction(resetPlayer2Score)
        self.fontSizeMenu = self.settingsMenu.addMenu("&Font Size")
        self.fontSizeMenu.addAction(fontsize1)
        self.fontSizeMenu.addAction(fontsize2)
        self.fontSizeMenu.addAction(fontsize3)
        self.fontSizeMenu.addAction(fontsize4)
        self.settingsMenu.addAction(chooseFont)
        self.settingsMenu.addAction(centerWindow)

        # GAME-LABEL

        self.gameLabel = QtWidgets.QLabel(self)
        self.gameLabel.setText("Tic Tac Toe")
        self.gameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.gameLabel, 0, 0, 1, 3)

        # GAME-BUTTONS-1

        self.gameButton1 = QtWidgets.QPushButton("~")
        self.gameButton2 = QtWidgets.QPushButton("~")
        self.gameButton3 = QtWidgets.QPushButton("~")

        self.gameButton1.clicked.connect(self.updateGameButton)
        self.gameButton2.clicked.connect(self.updateGameButton)
        self.gameButton3.clicked.connect(self.updateGameButton)

        self.gameButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gameButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gameButton3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.mainLayout.addWidget(self.gameButton1, 1, 0)
        self.mainLayout.addWidget(self.gameButton2, 1, 1)
        self.mainLayout.addWidget(self.gameButton3, 1, 2)

        # GAME-BUTTONS-2

        self.gameButton4 = QtWidgets.QPushButton("~")
        self.gameButton5 = QtWidgets.QPushButton("~")
        self.gameButton6 = QtWidgets.QPushButton("~")

        self.gameButton4.clicked.connect(self.updateGameButton)
        self.gameButton5.clicked.connect(self.updateGameButton)
        self.gameButton6.clicked.connect(self.updateGameButton)

        self.gameButton4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gameButton5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gameButton6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.mainLayout.addWidget(self.gameButton4, 2, 0)
        self.mainLayout.addWidget(self.gameButton5, 2, 1)
        self.mainLayout.addWidget(self.gameButton6, 2, 2)

        # GAME-BUTTONS-3

        self.gameButton7 = QtWidgets.QPushButton("~")
        self.gameButton8 = QtWidgets.QPushButton("~")
        self.gameButton9 = QtWidgets.QPushButton("~")

        self.gameButton7.clicked.connect(self.updateGameButton)
        self.gameButton8.clicked.connect(self.updateGameButton)
        self.gameButton9.clicked.connect(self.updateGameButton)

        self.gameButton7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gameButton8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gameButton9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.mainLayout.addWidget(self.gameButton7, 3, 0)
        self.mainLayout.addWidget(self.gameButton8, 3, 1)
        self.mainLayout.addWidget(self.gameButton9, 3, 2)

        # GAME-STATUS

        self.gamePlayer1 = QtWidgets.QLabel(self.player1)
        self.gamePlayer2 = QtWidgets.QLabel(self.player2)
        self.gamePlayerScores = QtWidgets.QLabel(f"{self.player1Score} vs {self.player2Score}")

        self.gamePlayer1.setStyleSheet("color: gray")
        self.gamePlayer2.setStyleSheet("color: gray")

        self.gamePlayer1.setAlignment(QtCore.Qt.AlignCenter)
        self.gamePlayer2.setAlignment(QtCore.Qt.AlignCenter)
        self.gamePlayerScores.setAlignment(QtCore.Qt.AlignCenter)

        self.mainLayout.addWidget(self.gamePlayer1, 4, 0)
        self.mainLayout.addWidget(self.gamePlayerScores, 4, 1)
        self.mainLayout.addWidget(self.gamePlayer2, 4, 2)

        # GAME-CENTER

        self.centerWindow()

    # GAME-FUNCTIONS

    def exitApp(self):

        # EXIT-APP

        sys.exit(0)

    def restartApp(self):

        # RESTART-APP

        subprocess.run(["setsid", "-f", "python3", "simple-tictactoe.py"])
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

    def updateLabels(self):

        # UPDATE_PAYER-LABEL

        self.updatePlayerLabel()

        # UPDATE-SCORE-LABEL

        self.gamePlayerScores.setText(f"{self.player1Score} vs {self.player2Score}")

    def updatePlayerLabel(self):

        # UPDATE-STYLE

        if self.player1Score > self.player2Score:
            self.gamePlayer2.setStyleSheet("color: gray; text-decoration: none")
            self.gamePlayer1.setStyleSheet("color: gray; text-decoration: underline")

        elif self.player2Score > self.player1Score:
            self.gamePlayer1.setStyleSheet("color: gray; text-decoration: none")
            self.gamePlayer2.setStyleSheet("color: gray; text-decoration: underline")

        elif self.player1Score == self.player1Score:
            self.gamePlayer1.setStyleSheet("color: gray; text-decoration: none")
            self.gamePlayer2.setStyleSheet("color: gray; text-decoration: none")

    def updateGameButton(self):

        # UPDATE-BUTTON

        if (self.sender().text() == "~"):

            self.sender().setText(self.currentPlayer)
            self.sender().setStyleSheet("color: white")

            self.checkGameWinner()

            if (self.currentPlayer == self.player1):
                self.currentPlayer = self.player2

            elif (self.currentPlayer == self.player2):
                self.currentPlayer = self.player1

    def tieMessage(self):

        # TIE-DIALOG

        tieDialog = QtWidgets.QMessageBox.information(self, "Player1 is the winner!", f"Tie between players! ({self.player1Score}) vs ({self.player2Score})")

    def winnerMessage(self):

        # PLAYER1-WINNER-DIALOG

        if (self.currentPlayer == self.player1):
            player1WinnerDialogTitle = "Player1 is the winner!"
            player1WinnerDialogMessage = f"Player1 is the winner! ({self.player1Score})"
            player1WinnerDialog = QtWidgets.QMessageBox.information(self, player1WinnerDialogTitle, player1WinnerDialogMessage)

        # PLAYER2-WINNER-DIALOG

        elif (self.currentPlayer == self.player2):
            player2WinnerDialogTitle = "Player2 is the winner!"
            player2WinnerDialogMessage = f"Player2 is the winner! ({self.player2Score})"
            player2WinnerDialog = QtWidgets.QMessageBox.information(self, player2WinnerDialogTitle, player2WinnerDialogMessage)

    def declareWinner(self):

        # PLAYER-1-WINNER

        if self.currentPlayer == self.player1:
            self.player1Score += 1
            self.updateLabels()
            self.winnerMessage()
            self.resetGameButtons()

        # PLAYER-2-WINNER

        elif self.currentPlayer == self.player2:
            self.player2Score += 1
            self.updateLabels()
            self.winnerMessage()
            self.resetGameButtons()

    def checkGameWinner(self):

        # CHECK-ROWS

        if self.gameButton1.text() == self.currentPlayer and self.gameButton2.text() == self.currentPlayer and self.gameButton3.text() == self.currentPlayer:
            self.declareWinner()

        elif self.gameButton4.text() == self.currentPlayer and self.gameButton5.text() == self.currentPlayer and self.gameButton6.text() == self.currentPlayer:
            self.declareWinner()

        elif self.gameButton7.text() == self.currentPlayer and self.gameButton8.text() == self.currentPlayer and self.gameButton9.text() == self.currentPlayer:
            self.declareWinner()

        # CHECK-COLUMNS

        if self.gameButton1.text() == self.currentPlayer and self.gameButton4.text() == self.currentPlayer and self.gameButton7.text() == self.currentPlayer:
            self.declareWinner()

        elif self.gameButton2.text() == self.currentPlayer and self.gameButton5.text() == self.currentPlayer and self.gameButton8.text() == self.currentPlayer:
            self.declareWinner()

        elif self.gameButton3.text() == self.currentPlayer and self.gameButton6.text() == self.currentPlayer and self.gameButton9.text() == self.currentPlayer:
            self.declareWinner()

        # CHECK-CROSS

        if self.gameButton1.text() == self.currentPlayer and self.gameButton5.text() == self.currentPlayer and self.gameButton9.text() == self.currentPlayer:
            self.declareWinner()

        elif self.gameButton3.text() == self.currentPlayer and self.gameButton5.text() == self.currentPlayer and self.gameButton7.text() == self.currentPlayer:
            self.declareWinner()

        # CHECK-TIE

        if  self.gameButton1.text() != "~" and self.gameButton2.text() != "~" and self.gameButton3.text() != "~" and \
            self.gameButton4.text() != "~" and self.gameButton5.text() != "~" and self.gameButton6.text() != "~" and \
            self.gameButton7.text() != "~" and self.gameButton8.text() != "~" and self.gameButton9.text() != "~":
            self.tieMessage()
            self.resetGameButtons()

    def resetGameButtons(self):

        # GAME-BUTTONS-1

        self.gameButton1.setText("~")
        self.gameButton2.setText("~")
        self.gameButton3.setText("~")
        self.gameButton1.setStyleSheet("color: gray")
        self.gameButton2.setStyleSheet("color: gray")
        self.gameButton3.setStyleSheet("color: gray")

        # GAME-BUTTONS-2

        self.gameButton4.setText("~")
        self.gameButton5.setText("~")
        self.gameButton6.setText("~")
        self.gameButton4.setStyleSheet("color: gray")
        self.gameButton5.setStyleSheet("color: gray")
        self.gameButton6.setStyleSheet("color: gray")

        # GAME-BUTTONS-3

        self.gameButton7.setText("~")
        self.gameButton8.setText("~")
        self.gameButton9.setText("~")
        self.gameButton7.setStyleSheet("color: gray")
        self.gameButton8.setStyleSheet("color: gray")
        self.gameButton9.setStyleSheet("color: gray")

    def resetPlayer1Score(self):

        # RESET-SCORE

        self.player1Score = 0
        self.updateLabels()

    def resetPlayer2Score(self):

        # RESET-SCORE

        self.player2Score = 0
        self.updateLabels()

    def resetGameScores(self):

        # RESET-SCORES

        self.resetPlayer1Score()
        self.resetPlayer2Score()

    def resetGameAll(self):
        
        # RESET-ALL

        self.resetGameScores()
        self.resetGameButtons()
        self.currentPlayer = self.player1


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleTictactoe = SimpleTictactoe()
    simpleTictactoe.show()

    sys.exit(app.exec_())
