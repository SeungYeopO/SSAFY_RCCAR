# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daily1_231108.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 320, 711, 231))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.goBtn = QPushButton(self.horizontalLayoutWidget)
        self.goBtn.setObjectName(u"goBtn")
        self.goBtn.setEnabled(True)
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.goBtn.setFont(font)

        self.horizontalLayout.addWidget(self.goBtn)

        self.pauseBtn = QPushButton(self.horizontalLayoutWidget)
        self.pauseBtn.setObjectName(u"pauseBtn")
        self.pauseBtn.setFont(font)

        self.horizontalLayout.addWidget(self.pauseBtn)

        self.resetBtn = QPushButton(self.horizontalLayoutWidget)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setFont(font)

        self.horizontalLayout.addWidget(self.resetBtn)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 134, 641, 110))
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\uace0\ub515")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.progressBar.setFont(font1)
        self.progressBar.setValue(50)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.goBtn.clicked.connect(MainWindow.goClick)
        self.pauseBtn.clicked.connect(MainWindow.pauseClick)
        self.resetBtn.clicked.connect(MainWindow.resetClick)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.goBtn.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.pauseBtn.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
    # retranslateUi
