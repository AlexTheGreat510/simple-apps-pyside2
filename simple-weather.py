#! /usr/bin/python3


import sys
import requests
import subprocess
from PySide2 import QtGui, QtCore, QtWidgets


class SimpleWeather(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SimpleWeather, self).__init__(parent)

        # APP-STYLE

        self.setStyleSheet("""* {
                                    font-size: 15pt
                              }

                              QLineEdit {
                                    font-weight: bold
                              }""")

        # APP-TITLE

        self.setWindowTitle("Simple Weather")

        # APP-FIXEDSIZE

        self.setFixedSize(QtCore.QSize(600, 676))

        # APP-ICON

        self.setWindowIcon(QtGui.QIcon("icons/simple-weather.png"))

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

        paris = QtWidgets.QAction("Paris", self)
        tokyo = QtWidgets.QAction("Tokyo", self)
        berlin = QtWidgets.QAction("Berlin", self)
        london = QtWidgets.QAction("London", self)
        lucknow = QtWidgets.QAction("Lucknow", self)
        beijing = QtWidgets.QAction("Beijing", self)
        baghdad = QtWidgets.QAction("Baghdad", self)
        jabalpur = QtWidgets.QAction("Jabalpur", self)
        prayagraj = QtWidgets.QAction("Prayagraj", self)

        # APP-MENU-TRIGGERED

        exit.triggered.connect(self.exitApp)
        restart.triggered.connect(self.restartApp)
        chooseFont.triggered.connect(self.selectFont)
        centerWindow.triggered.connect(self.centerWindow)
        fontsize1.triggered.connect(lambda : self.setFontSize(10))
        fontsize2.triggered.connect(lambda : self.setFontSize(15))
        fontsize3.triggered.connect(lambda : self.setFontSize(20))
        fontsize4.triggered.connect(lambda : self.setFontSize(25))

        paris.triggered.connect(self.fetchWeatherAPI)
        tokyo.triggered.connect(self.fetchWeatherAPI)
        berlin.triggered.connect(self.fetchWeatherAPI)
        london.triggered.connect(self.fetchWeatherAPI)
        lucknow.triggered.connect(self.fetchWeatherAPI)
        beijing.triggered.connect(self.fetchWeatherAPI)
        baghdad.triggered.connect(self.fetchWeatherAPI)
        jabalpur.triggered.connect(self.fetchWeatherAPI)
        prayagraj.triggered.connect(self.fetchWeatherAPI)

        # APP-MENUBAR

        self.appMenu = self.menuBar()

        # APP-MENU-ADD

        self.fileMenu = self.appMenu.addMenu("&File")
        self.fileMenu.addAction(exit)
        self.fileMenu.addAction(restart)
        self.settingsMenu = self.appMenu.addMenu("&Settings")
        self.cityMenu = self.settingsMenu.addMenu("&Cities")
        self.cityMenu.addAction(paris)
        self.cityMenu.addAction(tokyo)
        self.cityMenu.addAction(berlin)
        self.cityMenu.addAction(london)
        self.cityMenu.addAction(lucknow)
        self.cityMenu.addAction(beijing)
        self.cityMenu.addAction(baghdad)
        self.cityMenu.addAction(jabalpur)
        self.cityMenu.addAction(prayagraj)

        self.fontSizeMenu = self.settingsMenu.addMenu("&Font Size")
        self.fontSizeMenu.addAction(fontsize1)
        self.fontSizeMenu.addAction(fontsize2)
        self.fontSizeMenu.addAction(fontsize3)
        self.fontSizeMenu.addAction(fontsize4)
        self.settingsMenu.addAction(chooseFont)
        self.settingsMenu.addAction(centerWindow)

        # WEATHER-ICON

        self.weatherIcon = QtWidgets.QLabel("")
        self.weatherIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherIcon.setPixmap(QtGui.QPixmap("icons/simple-weather.png"))
        self.mainLayout.addWidget(self.weatherIcon, 0, 0, 1, 3)

        # WEATHER-LABEL

        self.weatherLabel = QtWidgets.QLabel("Simple Weather")
        self.weatherLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherLabel.setStyleSheet("margin: 25px 0px; font-weight: bold")
        self.mainLayout.addWidget(self.weatherLabel, 1, 0, 1, 2)

        # WEATHER-DAY-1

        self.weatherDay1 = QtWidgets.QLabel("today")
        self.weatherDay1.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherDay1.setStyleSheet("color: gray; margin: 25px 0px; font-weight: bold;")
        self.mainLayout.addWidget(self.weatherDay1, 2, 0, 1, 3)

        # WEATHER-TEMPRATURE

        self.temprature1 = QtWidgets.QLineEdit()
        self.temprature1.setReadOnly(True)
        self.temprature1.setAlignment(QtCore.Qt.AlignCenter)
        self.tempratureLabel1 = QtWidgets.QLabel("Temprature: ")

        self.mainLayout.addWidget(self.tempratureLabel1, 3, 0)
        self.mainLayout.addWidget(self.temprature1, 3, 1)

        # WEATHER-WIND

        self.wind1 = QtWidgets.QLineEdit()
        self.wind1.setReadOnly(True)
        self.wind1.setAlignment(QtCore.Qt.AlignCenter)
        self.windLabel1 = QtWidgets.QLabel("Wind: ")

        self.mainLayout.addWidget(self.windLabel1, 4, 0)
        self.mainLayout.addWidget(self.wind1, 4, 1)

        # WEATHER-DESCRIPTION

        self.description1 = QtWidgets.QLineEdit()
        self.description1.setReadOnly(True)
        self.description1.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionLabel1 = QtWidgets.QLabel("Description: ")

        self.mainLayout.addWidget(self.descriptionLabel1, 5, 0)
        self.mainLayout.addWidget(self.description1, 5, 1)

        # WEATHER-DAY-2

        self.weatherDay2 = QtWidgets.QLabel("tomorrow")
        self.weatherDay2.setStyleSheet("color: gray")
        self.weatherDay2.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherDay2.setStyleSheet("color: gray; margin: 25px 0px; font-weight: bold;")
        self.mainLayout.addWidget(self.weatherDay2, 6, 0, 1, 3)

        # WEATHER-WIND-2

        self.wind2 = QtWidgets.QLineEdit()
        self.wind2.setReadOnly(True)
        self.windLabel2 = QtWidgets.QLabel("Wind: ")
        self.wind2.setAlignment(QtCore.Qt.AlignCenter)

        self.mainLayout.addWidget(self.windLabel2, 7, 0)
        self.mainLayout.addWidget(self.wind2, 7, 1)

        # WEATHER-TEMPRATURE-2

        self.temprature2 = QtWidgets.QLineEdit()
        self.temprature2.setReadOnly(True)
        self.temprature2.setAlignment(QtCore.Qt.AlignCenter)
        self.tempratureLabel2 = QtWidgets.QLabel("Temprature: ")

        self.mainLayout.addWidget(self.tempratureLabel2, 8, 0)
        self.mainLayout.addWidget(self.temprature2, 8, 1)

        # WEATHER-DAY-3

        self.weatherDay3 = QtWidgets.QLabel("yesterday")
        self.weatherDay3.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherDay3.setStyleSheet("color: gray; margin: 25px 0px; font-weight: bold;")
        self.mainLayout.addWidget(self.weatherDay3, 9, 0, 1, 3)

        # WEATHER-WIND-3

        self.wind3 = QtWidgets.QLineEdit()
        self.wind3.setReadOnly(True)
        self.wind3.setAlignment(QtCore.Qt.AlignCenter)
        self.windLabel3 = QtWidgets.QLabel("Wind: ")

        self.mainLayout.addWidget(self.windLabel3, 10, 0)
        self.mainLayout.addWidget(self.wind3, 10, 1)

        # WEATHER-TEMPRATURE-3

        self.temprature3 = QtWidgets.QLineEdit()
        self.temprature3.setReadOnly(True)
        self.temprature3.setAlignment(QtCore.Qt.AlignCenter)
        self.tempratureLabel3 = QtWidgets.QLabel("Temprature: ")

        self.mainLayout.addWidget(self.tempratureLabel3, 11, 0)
        self.mainLayout.addWidget(self.temprature3, 11, 1)

        # APP-CENTER

        self.centerWindow()

    # APP-FUNCTIONS

    def exitApp(self):

        # EXIT-APP

        sys.exit(0)

    def restartApp(self):

        # RESTART-APP

        subprocess.run(["setsid", "-f", "python3", "simple-weather.py"])
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

    def updateWeatherWidgets(self, weatherData):

        # TRY-UPDATE-WIDGETS

        try: 
            self.wind1.setText(weatherData["wind"])
            self.temprature1.setText(weatherData["temperature"])
            self.description1.setText(weatherData["description"])

            self.wind2.setText(weatherData["forecast"][0]["wind"])
            self.temprature2.setText(weatherData["forecast"][0]["temperature"])

            self.wind3.setText(weatherData["forecast"][1]["wind"])
            self.temprature3.setText(weatherData["forecast"][1]["temperature"])

        # SHOW-ERROR-MESSAGE

        except:
            errorMessageDialog = QtWidgets.QErrorMessage(self)
            errorMessageDialog.showMessage("Unable to parse weather API!!")

    def fetchWeatherAPI(self):

        # WETAHER-CITY

        weatherCity = self.sender().text()

        # FETCH-WEATHER-API

        try:
            self.weatherAPI = requests.get(f"https://goweather.herokuapp.com/weather/{weatherCity}")

        # SHOW-ERROR-MESSAGE

        except:
            self.errorMessageDialog = QtWidgets.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Unable to fetch weather API!!")

        # UPDATE-WIDGETS

        else:
            self.weatherAPIData = self.weatherAPI.json()
            print(self.weatherAPIData)
            self.updateWeatherWidgets(self.weatherAPIData)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleWeather = SimpleWeather()
    simpleWeather.show()

    sys.exit(app.exec_())
