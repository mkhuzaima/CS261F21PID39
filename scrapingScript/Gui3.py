# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 60, 211, 41))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 110, 171, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 541, 51))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 230, 311, 51))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 310, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuScrapelancer = QtWidgets.QMenu(self.menubar)
        self.menuScrapelancer.setObjectName("menuScrapelancer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuScrapelancer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Process Complete "))
        self.label_2.setText(_translate("MainWindow", "Congratulations! The  Process of Sorting has been  completed Successfully."))
        self.label_3.setText(_translate("MainWindow", "Total Time Taken:  2 minutes 5 seconds"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.menuScrapelancer.setTitle(_translate("MainWindow", "Scrapelancer"))
