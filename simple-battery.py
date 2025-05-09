#! /usr/bin/python3


import sys
import subprocess


from PySide2 import QtGui, QtCore, QtWidgets


class SimpleBattery(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SimpleBattery, self).__init__(parent)

        # BATTERY-INFO

        self.batteryProcess = subprocess.run(["cat", "/sys/class/power_supply/BAT0/capacity"], capture_output=True)
        self.battery = int(self.batteryProcess.stdout)

        # APP-STYLE

        self.setStyleSheet("* { font-size: 15pt }")

        # APP-TITLE

        self.setWindowTitle("Simple Battery")

        # APP-FIXEDSIZE

        # ~ self.setFixedSize(QtCore.QSize(600, 200))

        # APP-ICON

        self.iconPath = "/usr/share/icons/papirus-antix"
        self.setWindowIcon(QtGui.QIcon(f"{self.iconPath}/24x24/apps/xfce4-power-manager-settings.png"))

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
        self.appIcon.setPixmap(QtGui.QPixmap(f"{self.iconPath}/24x24/apps/xfce4-power-manager-settings.png"))
        self.mainLayout.addWidget(self.appIcon, 0, 0)

        # APP-LABEL

        self.appLabel = QtWidgets.QLabel("Simple Battery")
        self.appLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appLabel.setStyleSheet("margin: 25px 0px; font-weight: bold;")
        self.mainLayout.addWidget(self.appLabel, 1, 0)

        # APP-BATTERY

        self.appBattery = QtWidgets.QLabel(f"BATTERY: {self.battery}%")
        self.appLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appLabel.setStyleSheet("margin: 25px 0px; font-weight: bold;")
        self.mainLayout.addWidget(self.appLabel, 2, 0)

        # APP-SYSTRAY

        self.trayIcon = QtWidgets.QSystemTrayIcon()
        self.trayIcon.setToolTip(str(self.battery))
        self.trayIcon.activated.connect(self.trayActivated)
        self.trayIcon.show()

        # UPDATE-SYSTRAY

        self.updateTrayIcon()

        # APP-CENTER

        self.centerWindow()

    # APP-FUNCTIONS

    def exitApp(self):

        # EXIT-APP

        sys.exit(0)

    def restartApp(self):

        # RESTART-APP

        subprocess.run(["setsid", "-f", "python3", "simple-battery.py"])
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

    def updateTrayIcon(self):

        # UDPATE-TRAYICON

        self.trayIcon.setIcon(QtGui.QIcon(f"{self.iconPath}/panel/battery-charged.png"))

    def toggleVisible(self):

        # TOGGLE-VISIBLITY

        if self.isVisible(): self.hide()
        else: self.show()

    def trayActivated(self, reason):

        # TOGGLE-VISIBLE

        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.toggleVisible()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleBattery = SimpleBattery()
    simpleBattery.hide()

    sys.exit(app.exec_())
