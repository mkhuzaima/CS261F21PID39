# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui2.ui'
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
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 50, 211, 31))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(36, 120, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(36, 170, 51, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 240, 75, 23))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 170, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 120, 181, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", "Sorting Specifications"))
        self.label_2.setText(_translate("MainWindow", "Sorting Algorithm"))
        self.label_3.setText(_translate("MainWindow", "Sort By"))
        self.pushButton.setText(_translate("MainWindow", "Done"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select Column Name"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Select Row Name"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Select Seller\'s Name"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Select Seller\'s Service Price"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Merge Sort"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Selction Sort"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Bubble Sort"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Quick Sort"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Insertion sort"))
        self.menuScrapelancer.setTitle(_translate("MainWindow", "Scrapelancer"))
