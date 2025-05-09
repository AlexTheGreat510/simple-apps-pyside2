#! /usr/bin/python3


import sys
import requests
import subprocess


from PySide2 import QtGui, QtCore, QtWidgets


class SimpleApps(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SimpleApps, self).__init__(parent)

        # APP-STYLE

        self.setStyleSheet("""* {
                                    font-size: 15pt
                              }
                              
                              QPushButton {
                                    padding: 80px 50px
                              }
                           """)

        # APP-TITLE

        self.setWindowTitle("Simple Apps")

        # APP-FIXEDSIZE

        self.setFixedSize(QtCore.QSize(889, 540))

        # APP-ICON

        self.setWindowIcon(QtGui.QIcon("icons/simple-search.png"))

        # APP-LAYOUT

        self.mainLayout = QtWidgets.QGridLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

        # APP-MENU-ACTION

        exit = QtWidgets.QAction("&Exit", self)
        fontsize1 = QtWidgets.QAction("&10", self)
        fontsize2 = QtWidgets.QAction("&15", self)
        fontsize3 = QtWidgets.QAction("&20", self)
        fontsize4 = QtWidgets.QAction("&25", self)
        restart = QtWidgets.QAction("&Restart", self)
        chooseFont = QtWidgets.QAction("&Choose Font", self)
        centerWindow = QtWidgets.QAction("Center Window", self)

        todo = QtWidgets.QAction(QtGui.QIcon(f"icons/simple-todos.png"), "&Simple Todos", self)
        search = QtWidgets.QAction(QtGui.QIcon(f"icons/simple-search.png"), "&Simple Search", self)
        passw = QtWidgets.QAction(QtGui.QIcon(f"icons/simple-password.png"), "&Simple Password", self)
        weather = QtWidgets.QAction(QtGui.QIcon(f"icons/simple-weather.png"), "&Simple Weather", self)
        calc = QtWidgets.QAction(QtGui.QIcon(f"icons/simple-calculator.png"), "&Simple Calculator", self)
        tictactoe = QtWidgets.QAction(QtGui.QIcon(f"icons/simple-search.png"), "&Simple Tictactoe", self)

        # APP-MENU-TRIGGERED

        exit.triggered.connect(self.exitApp)
        restart.triggered.connect(self.restartApp)
        chooseFont.triggered.connect(self.selectFont)
        centerWindow.triggered.connect(self.centerWindow)
        fontsize1.triggered.connect(lambda : self.setFontSize(10))
        fontsize2.triggered.connect(lambda : self.setFontSize(15))
        fontsize3.triggered.connect(lambda : self.setFontSize(20))
        fontsize4.triggered.connect(lambda : self.setFontSize(25))
        
        todo.triggered.connect(lambda : self.launchApp("simple-todos"))
        search.triggered.connect(lambda : self.launchApp("simple-search"))
        passw.triggered.connect(lambda : self.launchApp("simple-password"))
        calc.triggered.connect(lambda : self.launchApp("simple-calculator"))
        weather.triggered.connect(lambda : self.launchApp("simple-weather"))
        tictactoe.triggered.connect(lambda : self.launchApp("simple-tictactoe"))

        # APP-MENUBAR

        self.appMenu = self.menuBar()

        # APP-MENU-ADD

        self.fileMenu = self.appMenu.addMenu("&File")
        self.appsMenu = self.fileMenu.addMenu("&Apps")
        self.appsMenu.addAction(calc)
        self.appsMenu.addAction(passw)
        self.appsMenu.addAction(search)
        self.appsMenu.addAction(tictactoe)
        self.appsMenu.addAction(todo)
        self.appsMenu.addAction(weather)
        self.fileMenu.addAction(exit)
        self.fileMenu.addAction(restart)

        self.settingsMenu = self.appMenu.addMenu("&Settings")
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
        self.appIcon.setPixmap(QtGui.QPixmap("icons/simple-search.png"))
        self.mainLayout.addWidget(self.appIcon, 0, 0, 1, 3)

        # APP-LABEL

        self.appLabel = QtWidgets.QLabel("Simple Apps")
        self.appLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appLabel.setStyleSheet("margin: 25px 0px; font-weight: bold;")
        self.mainLayout.addWidget(self.appLabel, 1, 0, 1, 3)

        # APP-BUTTON-1

        self.appButton1 = QtWidgets.QPushButton("Simple Calculator")
        self.appButton1.setIcon(QtGui.QPixmap("icons/simple-calculator.png"))
        self.appButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.appButton1.clicked.connect(lambda : self.launchApp("simple-calculator"))
        self.mainLayout.addWidget(self.appButton1, 2, 0)

        # APP-BUTTON-2

        self.appButton2 = QtWidgets.QPushButton("Simple Password")
        self.appButton2.setIcon(QtGui.QPixmap("icons/simple-password.png"))
        self.appButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.appButton2.clicked.connect(lambda : self.launchApp("simple-password"))
        self.mainLayout.addWidget(self.appButton2, 2, 1)

        # APP-BUTTON-3

        self.appButton3 = QtWidgets.QPushButton("Simple Weather")
        self.appButton3.setIcon(QtGui.QPixmap("icons/simple-weather.png"))
        self.appButton3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.appButton3.clicked.connect(lambda : self.launchApp("simple-weather"))
        self.mainLayout.addWidget(self.appButton3, 2, 2)

        # APP-BUTTON-4

        self.appButton4 = QtWidgets.QPushButton("Simple Todos")
        self.appButton4.setIcon(QtGui.QPixmap("icons/simple-todos.png"))
        self.appButton4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.appButton4.clicked.connect(lambda : self.launchApp("simple-todos"))
        self.mainLayout.addWidget(self.appButton4, 3, 0)

        # APP-BUTTON-5

        self.appButton5 = QtWidgets.QPushButton("Simple Search")
        self.appButton5.setIcon(QtGui.QPixmap("icons/simple-search.png"))
        self.appButton5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.appButton5.clicked.connect(lambda : self.launchApp("simple-search"))
        self.mainLayout.addWidget(self.appButton5, 3, 1)

        # APP-BUTTON-6

        self.appButton6 = QtWidgets.QPushButton("Simple Tictactoe")
        self.appButton6.setIcon(QtGui.QPixmap("icons/simple-search.png"))
        self.appButton6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.appButton6.clicked.connect(lambda : self.launchApp("simple-tictactoe"))
        self.mainLayout.addWidget(self.appButton6, 3, 2)

        # APP-CENTER

        self.centerWindow()

    # APP-FUNCTIONS

    def exitApp(self):

        # EXIT-APP

        sys.exit(0)

    def restartApp(self):

        # RESTART-APP

        subprocess.run(["setsid", "-f", "python3", "simple-apps.py"])
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

    def launchApp(self, app):

        # LAUNCH-APP

        subprocess.run(["setsid", "-f", "python3", f"{app}.py"])

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleApps = SimpleApps()
    simpleApps.show()

    sys.exit(app.exec_())
