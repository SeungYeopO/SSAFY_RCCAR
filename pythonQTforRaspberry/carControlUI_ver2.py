# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'carControlUI_ver2.ui'
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
        MainWindow.resize(977, 407)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.rightBtn = QPushButton(self.centralwidget)
        self.rightBtn.setObjectName(u"rightBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightBtn.sizePolicy().hasHeightForWidth())
        self.rightBtn.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rightBtn.setFont(font)

        self.gridLayout.addWidget(self.rightBtn, 4, 6, 1, 1)

        self.gearBtn_3 = QPushButton(self.centralwidget)
        self.gearBtn_3.setObjectName(u"gearBtn_3")
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\uace0\ub515")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.gearBtn_3.setFont(font1)

        self.gridLayout.addWidget(self.gearBtn_3, 0, 2, 1, 1)

        self.fwdBtn = QPushButton(self.centralwidget)
        self.fwdBtn.setObjectName(u"fwdBtn")
        sizePolicy.setHeightForWidth(self.fwdBtn.sizePolicy().hasHeightForWidth())
        self.fwdBtn.setSizePolicy(sizePolicy)
        self.fwdBtn.setFont(font)

        self.gridLayout.addWidget(self.fwdBtn, 0, 5, 1, 1)

        self.bwdBtn = QPushButton(self.centralwidget)
        self.bwdBtn.setObjectName(u"bwdBtn")
        sizePolicy.setHeightForWidth(self.bwdBtn.sizePolicy().hasHeightForWidth())
        self.bwdBtn.setSizePolicy(sizePolicy)
        self.bwdBtn.setFont(font)

        self.gridLayout.addWidget(self.bwdBtn, 4, 5, 1, 1)

        self.gearBtn_4 = QPushButton(self.centralwidget)
        self.gearBtn_4.setObjectName(u"gearBtn_4")
        self.gearBtn_4.setFont(font1)

        self.gridLayout.addWidget(self.gearBtn_4, 0, 3, 1, 1)

        self.gearBtn_2 = QPushButton(self.centralwidget)
        self.gearBtn_2.setObjectName(u"gearBtn_2")
        self.gearBtn_2.setFont(font1)

        self.gridLayout.addWidget(self.gearBtn_2, 0, 1, 1, 1)

        self.gearBtn_1 = QPushButton(self.centralwidget)
        self.gearBtn_1.setObjectName(u"gearBtn_1")
        self.gearBtn_1.setFont(font1)

        self.gridLayout.addWidget(self.gearBtn_1, 0, 0, 1, 1)

        self.gupBtn = QPushButton(self.centralwidget)
        self.gupBtn.setObjectName(u"gupBtn")
        self.gupBtn.setFont(font)

        self.gridLayout.addWidget(self.gupBtn, 4, 0, 1, 1)

        self.gdwnBtn = QPushButton(self.centralwidget)
        self.gdwnBtn.setObjectName(u"gdwnBtn")
        self.gdwnBtn.setFont(font)

        self.gridLayout.addWidget(self.gdwnBtn, 4, 1, 1, 1)

        self.midBtn = QPushButton(self.centralwidget)
        self.midBtn.setObjectName(u"midBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.midBtn.sizePolicy().hasHeightForWidth())
        self.midBtn.setSizePolicy(sizePolicy1)
        self.midBtn.setFont(font)

        self.gridLayout.addWidget(self.midBtn, 1, 5, 1, 1)

        self.leftBtn = QPushButton(self.centralwidget)
        self.leftBtn.setObjectName(u"leftBtn")
        sizePolicy.setHeightForWidth(self.leftBtn.sizePolicy().hasHeightForWidth())
        self.leftBtn.setSizePolicy(sizePolicy)
        self.leftBtn.setFont(font)

        self.gridLayout.addWidget(self.leftBtn, 4, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.fwdBtn.pressed.connect(MainWindow.forward)
        self.leftBtn.pressed.connect(MainWindow.left)
        self.bwdBtn.pressed.connect(MainWindow.backward)
        self.rightBtn.pressed.connect(MainWindow.right)
        self.midBtn.pressed.connect(MainWindow.mid)
        self.gupBtn.toggled.connect(MainWindow.gearUP)
        self.gdwnBtn.toggled.connect(MainWindow.gearDWN)
        self.gearBtn_1.toggled.connect(MainWindow.gearFirst)
        self.gearBtn_2.toggled.connect(MainWindow.gearSecond)
        self.gearBtn_3.toggled.connect(MainWindow.gearThird)
        self.gearBtn_4.toggled.connect(MainWindow.gearFourth)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rightBtn.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.gearBtn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.fwdBtn.setText(QCoreApplication.translate("MainWindow", u"FORWARD", None))
        self.bwdBtn.setText(QCoreApplication.translate("MainWindow", u"BACKWARD", None))
        self.gearBtn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.gearBtn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.gearBtn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.gupBtn.setText(QCoreApplication.translate("MainWindow", u"UP", None))
        self.gdwnBtn.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.midBtn.setText(QCoreApplication.translate("MainWindow", u"MID", None))
        self.leftBtn.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
    # retranslateUi

