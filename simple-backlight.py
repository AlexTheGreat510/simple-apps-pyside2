#! /usr/bin/python3


import sys
import subprocess


from PySide2 import QtGui, QtCore, QtWidgets


class simpleSearch(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(simpleSearch, self).__init__(parent)

        # BACKLIGHT-INFO

        self.backlightProcess = subprocess.run(["backlight-brightness", "-g"], capture_output=True)
        self.backlight = int(self.backlightProcess.stdout)

        # APP-STYLE

        self.setStyleSheet("* { font-size: 15pt }")

        # APP-TITLE

        self.setWindowTitle("Simple Backlight")

        # APP-FIXEDSIZE

        self.setFixedSize(QtCore.QSize(400, 191))

        # APP-ICON

        self.iconPath = "/usr/share/icons/papirus-antix"
        self.setWindowIcon(QtGui.QIcon(f"{self.iconPath}/24x24/apps/backlight-brightness.png"))

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

        # APP-MENU-TRIGGERED

        exit.triggered.connect(self.exitApp)
        restart.triggered.connect(self.restartApp)
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
        self.appIcon.setPixmap(f"{self.iconPath}/24x24/apps/backlight-brightness.png")
        self.mainLayout.addWidget(self.appIcon, 0, 0, 1, 2)

        # APP-LABEL

        self.appLabel = QtWidgets.QLabel("Simple Backlight")
        self.appLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appLabel.setStyleSheet("margin: 25px 0px; font-weight: bold;")
        self.mainLayout.addWidget(self.appLabel, 1, 0, 1, 2)

        # APP-SLIDER

        self.appSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.appSlider.setMinimum(5)
        self.appSlider.setMaximum(100)
        self.appSlider.setTickInterval(5)
        self.appSlider.setValue(self.backlight)
        self.appSlider.valueChanged.connect(self.updateBacklight)
        self.appSlider.valueChanged.connect(self.updateSliderLabel)
        self.appSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.mainLayout.addWidget(self.appSlider, 2, 0)

        # APP-SLIDER-LABEL

        self.appSliderLabel = QtWidgets.QLabel(str(f"{self.backlight}%"))
        self.appSliderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.appSliderLabel, 2, 1)

        # APP-SYSTRAY

        self.trayIcon = QtWidgets.QSystemTrayIcon()
        self.trayIcon.setToolTip(f"{self.backlight}%")
        self.trayIcon.activated.connect(self.trayActivated)
        self.trayIcon.setIcon(QtGui.QIcon(f"{self.iconPath}/24x24/panel/redshift-status-on.png"))
        self.trayIcon.show()

        # APP-CENTER

        self.centerWindow()

    # APP-FUNCTIONS

    def exitApp(self):

        # EXIT-APP

        sys.exit(0)

    def restartApp(self):

        # RESTART-APP

        subprocess.run(["setsid", "-f", "python3", "simple-backlight.py"])
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

        self.appSliderLabel.setText(str(f"{self.appSlider.value()}%"))

    def toggleVisible(self):

        # TOGGLE-VISIBLITY

        if self.isVisible(): self.hide()
        else: self.show()

    def trayActivated(self, reason):

        # TOGGLE-VISIBLE

        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.toggleVisible()

    def updateBacklight(self):

        # GET-BACKLIGHT

        backlight = str(self.sender().value())

        # UPDATE-TOOLTIP

        self.trayIcon.setToolTip(f"{backlight}%")

        # SET-BACKLIGHT

        subprocess.run(["backlight-brightness", "-s", backlight])


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleSearch = simpleSearch()
    simpleSearch.hide()

    sys.exit(app.exec_())
