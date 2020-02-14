# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.our_map = QtWidgets.QLabel(self.centralwidget)
        self.our_map.setGeometry(QtCore.QRect(10, 10, 650, 450))
        self.our_map.setText("")
        self.our_map.setObjectName("our_map")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 510, 341, 31))
        self.input.setObjectName("input")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(10, 550, 341, 31))
        self.search.setObjectName("search")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 470, 211, 31))
        self.label_2.setObjectName("label_2")
        self.chng_map = QtWidgets.QPushButton(self.centralwidget)
        self.chng_map.setGeometry(QtCore.QRect(10, 590, 341, 31))
        self.chng_map.setObjectName("chng_map")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search.setText(_translate("MainWindow", "Искать"))
        self.label_2.setText(_translate("MainWindow", "Введите адрес:"))
        self.chng_map.setText(_translate("MainWindow", "press to change type of the map"))

