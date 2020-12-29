# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skeleton_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        font = QtGui.QFont()
        font.setFamily("Comic Sans")

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 20, 1000, 61))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        #input_handle_prompt
        font.setWeight(50)
        self.input_handle_prompt = QtWidgets.QLabel(self.centralwidget)
        self.input_handle_prompt.setGeometry(QtCore.QRect(50, 100, 600, 40))
        font.setPointSize(9)
        self.input_handle_prompt.setFont(font)
        self.input_handle_prompt.setAlignment(QtCore.Qt.AlignLeft)
        self.input_handle_prompt.setObjectName("input_handle_prompt")
        #input_handle
        self.input_handle = QtWidgets.QLineEdit(self.centralwidget)
        self.input_handle.setGeometry(QtCore.QRect(50, 125, 600, 31))
        self.input_handle.setText("")
        self.input_handle.setObjectName("input_handle")

        #input_number_prompt
        self.input_number_prompt = QtWidgets.QLabel(self.centralwidget)
        self.input_number_prompt.setGeometry(QtCore.QRect(50, 170, 600, 40))
        self.input_number_prompt.setFont(font)
        self.input_number_prompt.setAlignment(QtCore.Qt.AlignLeft)
        self.input_number_prompt.setObjectName("input_number_prompt")
        #input_number
        self.input_number = QtWidgets.QLineEdit(self.centralwidget)
        self.input_number.setGeometry(QtCore.QRect(50, 195, 250, 31))
        self.input_number.setText("")
        self.input_number.setObjectName("input_number")

        #input_remove_rt_prompt
        self.input_remove_rt_prompt = QtWidgets.QLabel(self.centralwidget)
        self.input_remove_rt_prompt.setGeometry(QtCore.QRect(50, 240, 600, 40))
        self.input_remove_rt_prompt.setFont(font)
        self.input_remove_rt_prompt.setAlignment(QtCore.Qt.AlignLeft)
        self.input_remove_rt_prompt.setObjectName("input_remove_rt_prompt")
        #input_remove_rt
        # self.input_remove_rt = QtWidgets.QCheckBox("Button1")
        # self.input_remove_rt.setGeometry(QtCore.QRect(50, 285, 250, 31))
        # self.input_remove_rt.move(50, 265)
        # self.input_remove_rt.setObjectName("input_remove_rt")

        #searchButton
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(50, 300, 75, 23))
        self.searchButton.setObjectName("searchButton")
        
        # self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        # self.resultLabel.setGeometry(QtCore.QRect(30, 200, 461, 331))
        # self.resultLabel.setFont(font)
        # self.resultLabel.setText("")
        # self.resultLabel.setPixmap(QtGui.QPixmap(str(pathlib.Path().absolute()) + '/assets/raccoon.png').scaled(500, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        # self.resultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        # self.resultLabel.setObjectName("resultLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.searchButton.clicked.connect(lambda: self.clicked())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Twitter Scraper"))
        self.input_handle_prompt.setText(_translate("MainWindow", "Enter the screen name of the twitter account you want to collect tweets for:"))
        self.input_number_prompt.setText(_translate("MainWindow", "Enter the number of tweets you want from them (minimum = 0, maximum = 350):"))
        self.input_remove_rt_prompt.setText(_translate("MainWindow", "Do you want to include retweet?"))
        self.searchButton.setText(_translate("MainWindow", "Search"))

    def clicked(self):
        # pixmap = QtGui.QPixmap(str(pathlib.Path().absolute()) + '/assets/red_panda.jpg').scaled(500, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        # self.resultLabel.setPixmap(pixmap)
        input_handle = self.input_handle.text()
        input_number = int(self.input_number.text())
        print(f'click complete: {input_handle}: {input_number}')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
