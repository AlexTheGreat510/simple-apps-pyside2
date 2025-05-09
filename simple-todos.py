#! /usr/bin/python3


import sys
import requests
import subprocess


from PySide2 import QtGui, QtCore, QtWidgets


class SimpleTodos(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SimpleTodos, self).__init__(parent)

        # TODO-STYLE

        self.setStyleSheet("* { font-size: 15pt }")

        # TODO-TITLE

        self.setWindowTitle("Simple Todos")

        # TODO-ICON

        self.setWindowIcon(QtGui.QIcon("icons/simple-todos.png"))

        # TODO-LAYOUT

        self.mainLayout = QtWidgets.QGridLayout()
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

        # TODO-MENU-ACTION

        exit = QtWidgets.QAction("&Exit", self)
        restart = QtWidgets.QAction("&Restart", self)
        fontsize1 = QtWidgets.QAction("&10", self)
        fontsize2 = QtWidgets.QAction("&15", self)
        fontsize3 = QtWidgets.QAction("&20", self)
        fontsize4 = QtWidgets.QAction("&25", self)
        resetAll = QtWidgets.QAction("Remove All", self)
        chooseFont = QtWidgets.QAction("&Choose Font", self)
        centerWindow = QtWidgets.QAction("Center Window", self)

        # TODO-MENU-TRIGGERED

        exit.triggered.connect(self.exitApp)
        restart.triggered.connect(self.restartApp)
        resetAll.triggered.connect(self.resetTodos)
        chooseFont.triggered.connect(self.selectFont)
        centerWindow.triggered.connect(self.centerWindow)
        fontsize1.triggered.connect(lambda : self.setFontSize(10))
        fontsize2.triggered.connect(lambda : self.setFontSize(15))
        fontsize3.triggered.connect(lambda : self.setFontSize(20))
        fontsize4.triggered.connect(lambda : self.setFontSize(25))

        # TODO-MENUBAR

        self.todoMenu = self.menuBar()

        # TODO-MENU-ADD

        self.fileMenu = self.todoMenu.addMenu("&File")
        self.fileMenu.addAction(exit)
        self.fileMenu.addAction(restart)
        self.settingsMenu = self.todoMenu.addMenu("&Settings")
        self.settingsMenu.addAction(resetAll)
        self.fontSizeMenu = self.settingsMenu.addMenu("&Font Size")
        self.fontSizeMenu.addAction(fontsize1)
        self.fontSizeMenu.addAction(fontsize2)
        self.fontSizeMenu.addAction(fontsize3)
        self.fontSizeMenu.addAction(fontsize4)
        self.settingsMenu.addAction(chooseFont)
        self.settingsMenu.addAction(centerWindow)

        # TODO-ICON

        self.todoIcon = QtWidgets.QLabel("")
        self.todoIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.todoIcon.setPixmap(QtGui.QPixmap("icons/simple-todos.png"))
        self.mainLayout.addWidget(self.todoIcon, 0, 0, 1, 2)

        # TODO-LABEL

        self.todoLabel = QtWidgets.QLabel("Simple Todos")
        self.todoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.todoLabel.setStyleSheet("margin: 25px 0px; font-weight: bold")
        self.mainLayout.addWidget(self.todoLabel, 1, 0, 1, 2)

        # TODO-INPUT

        self.todoInput = QtWidgets.QLineEdit()
        self.todoInput.setPlaceholderText("Enter todo")
        self.todoInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.todoInput, 2, 0)

        # TODO-ADD

        self.todoAdd = QtWidgets.QPushButton("+")
        self.todoAdd.clicked.connect(self.addTodo)
        self.todoAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.todoAdd, 2, 1)

        # TODO-CONTAINER

        self.todoRow = 0
        self.todoContainer = QtWidgets.QWidget()
        self.todoContainerLayout = QtWidgets.QGridLayout()
        self.todoContainer.setStyleSheet("margin: 25px 0px")
        self.todoContainer.setLayout(self.todoContainerLayout)
        self.mainLayout.addWidget(self.todoContainer, 3, 0, 1, 2)

        # TODO-REMOVE-ALL

        self.todoRemoveAll = QtWidgets.QPushButton("RESET")
        self.todoRemoveAll.clicked.connect(self.resetTodos)
        self.todoRemoveAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainLayout.addWidget(self.todoRemoveAll, 4, 0, 1, 2)

        # TODO-CENTER

        self.centerWindow()

    # TODO-FUNCTIONS

    def exitApp(self):

        # EXIT-APP

        sys.exit(0)

    def restartApp(self):

        # RESTART-APP

        subprocess.run(["setsid", "-f", "python3", "simple-todos.py"])
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

    def resetTodos(self):

        # DELETE-ALL-TODOS

        for i in reversed(range(self.todoContainerLayout.count())):
            todo = self.todoContainerLayout.itemAt(i).widget()

            if todo:
                todo.deleteLater()

        # TODO-ROW

        self.todoRow = 0

    def updateCheckboxText(self, checkbox, state):

        # CHANGE-TODO-STYLE

        if not state == QtCore.Qt.Checked:
            checkbox.setStyleSheet("text-decoration: none")
        else:
            checkbox.setStyleSheet("text-decoration: line-through")

    def addTodo(self):

        # TODO-TEXT

        todo = self.todoInput.text()

        # ADD-TODO

        if (todo):
            todoCheckbox = QtWidgets.QCheckBox(todo, self)
            todoCheckbox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            todoCheckbox.stateChanged.connect(lambda state, cb=todoCheckbox: self.updateCheckboxText(cb, state))
            self.todoContainerLayout.addWidget(todoCheckbox, self.todoRow, 0)
            self.todoInput.clear()

        # TODO-ROW

        self.todoRow += 1


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    simpleTodos = SimpleTodos()
    simpleTodos.show()

    sys.exit(app.exec_())
