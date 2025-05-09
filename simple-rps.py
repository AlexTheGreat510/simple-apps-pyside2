#! /usr/bin/python3


import sys
import random
import subprocess


from PySide2 import QtGui, QtCore, QtWidgets


class SimpleRPS(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SimpleRPS, self).__init__(parent)

        # GAME-INFO

        self.rpsTurns = 0
        self.rpsPlayer1Score = 0
        self.rpsPlayer2Score = 0
        self.rpsChoices = ["rock", "paper", "sizzor"]

        # GAME-STYLE

        self.setStyleSheet("* { font-size: 15pt }")

        # GAME-FIXEDSIZE

        self.setFixedSize(QtCore.QSize(600, 245))

        # GAME-TITLE

        self.setWindowTitle(f"Simple RPS ({self.rpsTurns})")

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
        chooseFont = QtWidgets.QAction("&Choose Font", self)
        resetScores = QtWidgets.QAction("Player Scores", self)
        self.alwaysWin = QtWidgets.QAction("Always Win", self)
        centerWindow = QtWidgets.QAction("Center Window", self)
        self.preventTie = QtWidgets.QAction("Prevent Tie", self)
        self.alwaysLoose = QtWidgets.QAction("Always Loose", self)
        resetPlayer1Score = QtWidgets.QAction("Player1 Score", self)
        resetPlayer2Score = QtWidgets.QAction("Player2 Score", self)

        # GAME-MENU-TRIGGERED

        exit.triggered.connect(self.exitApp)
        restart.triggered.connect(self.restartApp)
        chooseFont.triggered.connect(self.selectFont)
        resetScores.triggered.connect(self.resetScores)
        centerWindow.triggered.connect(self.centerWindow)
        fontsize1.triggered.connect(lambda : self.setFontSize(10))
        fontsize2.triggered.connect(lambda : self.setFontSize(15))
        fontsize3.triggered.connect(lambda : self.setFontSize(20))
        fontsize4.triggered.connect(lambda : self.setFontSize(25))
        resetPlayer1Score.triggered.connect(self.resetPlayer1Score)
        resetPlayer2Score.triggered.connect(self.resetPlayer2Score)

        # GAME-MENU-CHECK

        self.preventTie.setCheckable(True)
        self.preventTie.setChecked(True)
        self.alwaysWin.setCheckable(True)
        self.alwaysLoose.setCheckable(True)

        # GAME-MENUBAR

        self.rpsMenu = self.menuBar()

        # GAME-MENU-ADD

        self.fileMenu = self.rpsMenu.addMenu("&File")
        self.fileMenu.addAction(exit)
        self.fileMenu.addAction(restart)
        self.settingsMenu = self.rpsMenu.addMenu("&Settings")
        self.settingsMenu.addAction(self.preventTie)
        self.settingsMenu.addAction(self.alwaysWin)
        self.settingsMenu.addAction(self.alwaysLoose)
        self.resetMenu = self.settingsMenu.addMenu("&Reset")
        self.resetMenu.addAction(resetScores)
        self.resetMenu.addAction(resetPlayer1Score)
        self.resetMenu.addAction(resetPlayer2Score)
        self.fontSizeMenu = self.settingsMenu.addMenu("&Font Size")
        self.fontSizeMenu.addAction(fontsize1)
        self.fontSizeMenu.addAction(fontsize2)
        self.fontSizeMenu.addAction(fontsize3)
        self.fontSizeMenu.addAction(fontsize4)
        self.settingsMenu.addAction(chooseFont)
        self.settingsMenu.addAction(centerWindow)

        # GAME-ICON

        self.rpsIcon = QtWidgets.QLabel("")
        self.rpsIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.rpsIcon.setPixmap(QtGui.QPixmap("icons/simple-search.png"))
        self.mainLayout.addWidget(self.rpsIcon, 0, 0, 1, 3)

        # GAME-LABEL

        self.rpsLabel = QtWidgets.QLabel("Simple RPS")
        self.rpsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rpsLabel.setStyleSheet("margin: 25px 0px; font-weight: bold")
        self.mainLayout.addWidget(self.rpsLabel, 1, 0, 1, 3)

        # GAME-PLAYER-1

        self.rpsPlayer1ComboBox = QtWidgets.QComboBox()
        self.rpsPlayer1ComboBox.setEditable(True)
        self.rpsPlayer1ComboBox.addItems(self.rpsChoices)
        self.rpsPlayer1ComboBox.lineEdit().setReadOnly(True)
        self.rpsPlayer1ComboBox.activated.connect(self.checkWinner)
        self.rpsPlayer1ComboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.rpsPlayer1ComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.rpsPlayer1ComboBox, 2, 0)

        # GAME-VS-LABEL

        self.vsLabel = QtWidgets.QLabel("vs")
        self.vsLabel.setStyleSheet("color: gray")
        self.vsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.vsLabel, 2, 1)

        # GAME-PLAYER-2

        self.rpsPlayer2ComboBox = QtWidgets.QComboBox()
        self.rpsPlayer2ComboBox.setEditable(True)
        self.rpsPlayer2ComboBox.addItems(self.rpsChoices)
        self.rpsPlayer2ComboBox.lineEdit().setReadOnly(True)
        self.rpsPlayer2ComboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.rpsPlayer2ComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.rpsPlayer2ComboBox, 2, 2)

        # GAME-STATS

        self.rpsPlayer1Label = QtWidgets.QLabel("PLAYER-1")
        self.rpsPlayer1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.rpsPlayer1Label.setStyleSheet("color: gray; font-weight: bold; margin-top: 25px")
        self.mainLayout.addWidget(self.rpsPlayer1Label, 3, 0)

        self.rpsScore = QtWidgets.QLabel(f"{self.rpsPlayer1Score} vs {self.rpsPlayer2Score}")
        self.rpsScore.setAlignment(QtCore.Qt.AlignCenter)
        self.rpsScore.setStyleSheet("margin-top: 25px; font-weight: bold")
        self.mainLayout.addWidget(self.rpsScore, 3, 1)

        self.rpsPlayer2Label = QtWidgets.QLabel("PLAYER-2")
        self.rpsPlayer2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.rpsPlayer2Label.setStyleSheet("color: gray; font-weight: bold; margin-top: 25px")
        self.mainLayout.addWidget(self.rpsPlayer2Label, 3, 2)
        
        # GAME-CENTER

        self.centerWindow()

    # GAME-FUNCTIONS

    def exitApp(self):

        # EXIT-APP

        sys.exit(0)

    def restartApp(self):

        # RESTART-APP

        subprocess.run(["setsid", "-f", "python3", "simple-rps.py"])
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

    def updateWindowTitle(self):

        # UPDATE-TITLE

        self.setWindowTitle(f"Simple RPS ({self.rpsTurns})")

    def updateScores(self):

        # UPDATE-SCORE-LABEL

        self.rpsScore.setText(f"{self.rpsPlayer1Score} vs {self.rpsPlayer2Score}")


    def resetTurns(self):

        # RESET-TURNS

        self.resetTurns = 0

        # UPDATE-TITLE

        self.updateWindowTitle()

    def resetPlayer1Score(self):

        # RESET-SCORE

        self.rpsPlayer1Score = 0

        # UPDATE-SCORE-LABEL

        self.updateScores()

        # CHECK-SCORES

        self.checkScores()

    def resetPlayer2Score(self):

        # RESET-SCORE

        self.rpsPlayer2Score = 0

        # UPDATE-SCORE-LABEL

        self.updateScores()

        # CHECK-SCORES

        self.checkScores()

    def resetScores(self):

        # RESET-PLAYER-SCORES

        self.resetPlayer1Score()
        self.resetPlayer2Score()

        # CHECK-SCORES

        self.checkScores()

    def checkScores(self):

        # PLAYER-1-SCORE

        if self.rpsPlayer1Score > self.rpsPlayer2Score:
            self.rpsPlayer1Label.setStyleSheet("color: gray; font-weight: bold; margin-top: 25px; text-decoration: underline")
            self.rpsPlayer2Label.setStyleSheet("color: gray; font-weight: bold; margin-top: 25px; text-decoration: none")

        # PLAYER-2-SCORE

        elif self.rpsPlayer2Score > self.rpsPlayer1Score:
            self.rpsPlayer2Label.setStyleSheet("color: gray; font-weight: bold; margin-top: 25px; text-decoration: underline")
            self.rpsPlayer1Label.setStyleSheet("color: gray; font-weight: bold; margin-top: 25px; text-decoration: none")

        # PLAYER-EQUAL-SCORES

        elif self.rpsPlayer1Score == self.rpsPlayer2Score:
            self.rpsPlayer1Label.setStyleSheet("color: gray; font-weight: bold; margin-top: 25px; text-decoration: none")
            self.rpsPlayer2Label.setStyleSheet("color: gray; font-weight: bold; margin-top: 25px; text-decoration: none")

    def updatePlayer2Choice(self):

        # PLAYER1-CHOICE

        player1Choice = self.rpsPlayer1ComboBox.currentText()

        # ALWAYS-WIN

        if self.alwaysWin.isChecked():

            match(player1Choice):

                case "rock":
                    player2Choice = "sizzor"

                case "paper":
                    player2Choice = "rock"

                case "sizzor":
                    player2Choice = "paper"

        # ALWAYS-LOOSE

        elif self.alwaysLoose.isChecked():

            match(player1Choice):

                case "rock":
                    player2Choice = "paper"

                case "paper":
                    player2Choice = "sizzor"

                case "sizzor":
                    player2Choice = "rock"

        # FIGHT

        else:

            # WITHOUT-TIE

            if not self.preventTie.isChecked():

                # RANDOMLY-CHOOSE

                player2Choice = random.choice(self.rpsChoices)

            # WITH-TIE

            elif self.preventTie.isChecked():

                # UPDATED-CHOICES

                rpsUpdatedChoices = self.rpsChoices.copy()
                rpsUpdatedChoices.remove(self.rpsPlayer1ComboBox.currentText())

                # RANDOMLY-CHOOSE

                player2Choice = random.choice(rpsUpdatedChoices)

        # UPDATE-COMBOBOX

        self.rpsPlayer2ComboBox.setCurrentText(player2Choice)

    def isWinner(self, rpsWinner):

        # UPDATE-TURNS

        self.rpsTurns += 1

        # UPDATE-TITLE

        self.updateWindowTitle()

        # CHECK-SCORES

        self.checkScores()

        # CHECK-TIE

        if rpsWinner == "tie":

            # SHOW-TIE-DIALOG

            tieDialogTitle = "Tie between players!"
            tieDialogMessage = f"Tie between players! ({self.rpsPlayer1Score} vs {self.rpsPlayer2Score})"
            tieDialog = QtWidgets.QMessageBox.information(self, tieDialogTitle, tieDialogMessage)

        # CHECK-PLAYER-1

        if rpsWinner == "player1":

            # UPDATE-SCORE

            self.rpsPlayer1Score += 1
            self.updateScores()
            self.checkScores()

            # SHOW-WINNER-DIALOG

            player1WinnerDialogTitle = "Player1 is the winner!"
            player1WinnerDialogMessage = f"Player1 is the winner! ({self.rpsPlayer1Score})"
            player1WinnerDialog = QtWidgets.QMessageBox.information(self, player1WinnerDialogTitle, player1WinnerDialogMessage)

        # CHECK-PLAYER-2

        elif rpsWinner == "player2":

            # UPDATE-SCORE

            self.rpsPlayer2Score += 1
            self.updateScores()
            self.checkScores()

            # SHOW-WINNER-DIALOG

            player2WinnerDialogTitle = "Player2 is the winner!"
            player2WinnerDialogMessage = f"Player2 is the winner! ({self.rpsPlayer2Score})"
            player2WinnerDialog = QtWidgets.QMessageBox.information(self, player2WinnerDialogTitle, player2WinnerDialogMessage)

    def checkWinner(self):

        # PLAYER2-CHOICE

        self.updatePlayer2Choice()

        # PLAYER-CHOICES

        player1Choice = self.rpsPlayer1ComboBox.currentText()
        player2Choice = self.rpsPlayer2ComboBox.currentText()

        # CHECK-TIE

        if player1Choice == player2Choice:
            self.isWinner("tie")

        # CHECK-PLAYER-1

        if player1Choice == "rock" and player2Choice == "sizzor" or \
           player1Choice == "paper" and player2Choice == "rock" or \
           player1Choice == "sizzor" and player2Choice == "paper":

           self.isWinner("player1")

        # CHECK-PLAYER-2

        elif player2Choice == "rock" and player1Choice == "sizzor" or \
             player2Choice == "paper" and player1Choice == "rock" or \
             player2Choice == "sizzor" and player1Choice == "paper":

           self.isWinner("player2")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleRPS = SimpleRPS()
    simpleRPS.show()

    sys.exit(app.exec_())
