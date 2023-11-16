# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daily3_231108.ui'
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
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 70, 541, 401))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.progressBar_1 = QProgressBar(self.verticalLayoutWidget)
        self.progressBar_1.setObjectName(u"progressBar_1")
        self.progressBar_1.setSizeIncrement(QSize(50, 50))
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_1.setFont(font)
        self.progressBar_1.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_1)

        self.progressBar_2 = QProgressBar(self.verticalLayoutWidget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setFont(font)
        self.progressBar_2.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_2)

        self.progressBar_3 = QProgressBar(self.verticalLayoutWidget)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setFont(font)
        self.progressBar_3.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_3)

        self.progressBar_4 = QProgressBar(self.verticalLayoutWidget)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setFont(font)
        self.progressBar_4.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_4)

        self.progressBar_5 = QProgressBar(self.verticalLayoutWidget)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setFont(font)
        self.progressBar_5.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_5)

        self.downloadBtn = QPushButton(self.centralwidget)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setGeometry(QRect(640, 260, 101, 31))
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.downloadBtn.setFont(font1)
        self.downloadBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.downloadBtn.setLayoutDirection(Qt.LeftToRight)
        self.downloadBtn.setAutoDefault(False)
        self.downloadBtn.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.downloadBtn.clicked.connect(MainWindow.download)

        self.downloadBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.downloadBtn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

