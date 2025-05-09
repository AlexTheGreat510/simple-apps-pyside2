#! /usr/bin/python3


import sys
import requests
import subprocess


from PySide2 import QtGui, QtCore, QtWidgets


class SimpleSearch(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SimpleSearch, self).__init__(parent)

        # APP-BROWSER

        self.appBrowser = "firefox"

        # APP-STYLE

        self.setStyleSheet("* { font-size: 15pt }")

        # APP-TITLE

        self.setWindowTitle("Simple Search")

        # APP-FIXEDSIZE

        self.setFixedSize(QtCore.QSize(600, 200))

        # APP-ICON

        self.iconPath = "/usr/share/icons/papirus-antix/24x24/apps"
        self.setWindowIcon(QtGui.QIcon(f"{self.iconPath}/google.png"))

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
        firefox = QtWidgets.QAction(QtGui.QIcon(f"{self.iconPath}/firefox.png"), "firefox", self)
        chromium = QtWidgets.QAction(QtGui.QIcon(f"{self.iconPath}/chromium.png"), "chromium", self)

        # APP-MENU-TRIGGERED

        exit.triggered.connect(self.exitApp)
        restart.triggered.connect(self.restartApp)
        firefox.triggered.connect(self.setBrowser)
        chromium.triggered.connect(self.setBrowser)
        chooseFont.triggered.connect(self.selectFont)
        centerWindow.triggered.connect(self.centerWindow)
        fontsize1.triggered.connect(lambda : self.setFontSize(10))
        fontsize2.triggered.connect(lambda : self.setFontSize(15))
        fontsize3.triggered.connect(lambda : self.setFontSize(20))
        fontsize4.triggered.connect(lambda : self.setFontSize(25))

        # APP-MENUBAR

        self.appMenu = self.menuBar()

        # APP-MENU-ADD

        self.fileMenu = self.appMenu.addMenu("&File")
        self.fileMenu.addAction(exit)
        self.fileMenu.addAction(restart)
        self.settingsMenu = self.appMenu.addMenu("&Settings")
        self.browserMenu = self.settingsMenu.addMenu("&Browser")
        self.browserMenu.addAction(firefox)
        self.browserMenu.addAction(chromium)
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
        self.appIcon.setPixmap(f"{self.iconPath}/google.png")
        self.mainLayout.addWidget(self.appIcon, 0, 0, 1, 3)

        # APP-LABEL

        self.appLabel = QtWidgets.QLabel("Simple Search")
        self.appLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appLabel.setStyleSheet("margin: 25px 0px; font-weight: bold;")
        self.mainLayout.addWidget(self.appLabel, 1, 0, 1, 3)

        # APP-COMBOBOX

        self.appComboBox = QtWidgets.QComboBox()
        self.appComboBox.activated.connect(self.updateIcons)
        self.appComboBox.activated.connect(self.updateTrayIcon)
        self.appComboBox.addItem(QtGui.QIcon(f"{self.iconPath}/google.png"), "google")
        self.appComboBox.addItem(QtGui.QIcon(f"{self.iconPath}/youtube.png"), "youtube")
        self.appComboBox.addItem(QtGui.QIcon(f"{self.iconPath}/amazon.png"), "amazon")
        self.appComboBox.addItem(QtGui.QIcon(f"{self.iconPath}/google.png"), "bing")
        self.appComboBox.addItem(QtGui.QIcon(f"{self.iconPath}/google.png"), "duckduckgo")
        self.appComboBox.addItem(QtGui.QIcon(f"{self.iconPath}/wikipedia.png"), "wikipedia")
        self.mainLayout.addWidget(self.appComboBox, 2, 0)

        # APP-INPUT

        self.appInput = QtWidgets.QLineEdit()
        self.appInput.returnPressed.connect(self.searchTerm)
        self.appInput.setPlaceholderText("Enter Search Term")
        self.appInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.appInput, 2, 1)

        # APP-SEARCH

        self.appSearch = QtWidgets.QPushButton(QtGui.QIcon(f"{self.iconPath}/firefox.png"), "search ++")
        self.appSearch.clicked.connect(self.searchTerm)
        self.appSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.appSearch, 2, 2)

        # APP-SYSTRAY

        self.trayIcon = QtWidgets.QSystemTrayIcon()
        self.trayIcon.activated.connect(self.trayActivated)
        self.trayIcon.setToolTip(self.appComboBox.currentText())
        self.trayIcon.setIcon(self.appComboBox.itemIcon(self.appComboBox.currentIndex()))
        self.trayIcon.show()

        # APP-CENTER

        self.centerWindow()

    # APP-FUNCTIONS

    def exitApp(self):

        # EXIT-APP

        sys.exit(0)

    def restartApp(self):

        # RESTART-APP

        subprocess.run(["setsid", "-f", "python3", "simple-search.py"])
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

    def updateIcons(self):

        # UPDATE-WINDOW-ICON

        self.setWindowIcon(self.appComboBox.itemIcon(self.appComboBox.currentIndex()))

    def updateTrayIcon(self):

        # UDPATE-TRAYICON

        self.trayIcon.setToolTip(self.appComboBox.currentText())
        self.trayIcon.setIcon(self.appComboBox.itemIcon(self.appComboBox.currentIndex()))

    def setBrowser(self):

        # SET-BROWSER

        self.appBrowser = self.sender().text()

        # UPDATE-ICON

        self.appSearch.setIcon(self.sender().icon())

    def toggleVisible(self):

        # TOGGLE-VISIBLITY

        if self.isVisible(): self.hide()
        else: self.show()

    def trayActivated(self, reason):

        # TOGGLE-VISIBLE

        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.toggleVisible()

    def searchTerm(self):

        # SEARCH-INFO

        term = self.appInput.text()
        engine = self.appComboBox.currentText()

        # SEARCH-TERM

        if term:

            # SET-URL

            match engine:

                case "amazon":
                    url = f"https://www.amazon.in/s?k={term}"

                case "google":
                    url = f"https://www.google.com/search?q={term}"

                case "duckduckgo":
                    url = f"https://www.duckduckgo.com/search?q={term}"

                case "youtube":
                    url = f"https://www.youtube.com/results?search_query={term}"

                case "bing":
                    url = f"https://www.youtube.com/results?search_query={term}"

                case "wikipedia":
                    url = f"https://en.wikipedia.org/wiki/Special:Search/{term}"

                case _:
                    url = f"https://www.google.com/search?q={term}"

            # OPEN-URL

            subprocess.run(["setsid", "-f", self.appBrowser, url])
            self.toggleVisible()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleSearch = SimpleSearch()
    simpleSearch.hide()

    sys.exit(app.exec_())
