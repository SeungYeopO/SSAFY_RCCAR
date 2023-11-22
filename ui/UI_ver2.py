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
        MainWindow.resize(1065, 326)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.midBtn = QPushButton(self.centralwidget)
        self.midBtn.setObjectName(u"midBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.midBtn.sizePolicy().hasHeightForWidth())
        self.midBtn.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.midBtn.setFont(font)

        self.gridLayout_2.addWidget(self.midBtn, 2, 7, 1, 1)

        self.gearBtn_2 = QPushButton(self.centralwidget)
        self.gearBtn_2.setObjectName(u"gearBtn_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gearBtn_2.sizePolicy().hasHeightForWidth())
        self.gearBtn_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\uace0\ub515")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.gearBtn_2.setFont(font1)

        self.gridLayout_2.addWidget(self.gearBtn_2, 0, 3, 1, 1)

        self.rightBtn = QPushButton(self.centralwidget)
        self.rightBtn.setObjectName(u"rightBtn")
        sizePolicy1.setHeightForWidth(self.rightBtn.sizePolicy().hasHeightForWidth())
        self.rightBtn.setSizePolicy(sizePolicy1)
        self.rightBtn.setFont(font)

        self.gridLayout_2.addWidget(self.rightBtn, 4, 8, 1, 1)

        self.bwdBtn = QPushButton(self.centralwidget)
        self.bwdBtn.setObjectName(u"bwdBtn")
        sizePolicy1.setHeightForWidth(self.bwdBtn.sizePolicy().hasHeightForWidth())
        self.bwdBtn.setSizePolicy(sizePolicy1)
        self.bwdBtn.setFont(font)

        self.gridLayout_2.addWidget(self.bwdBtn, 4, 7, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.gearLcd = QLCDNumber(self.centralwidget)
        self.gearLcd.setObjectName(u"gearLcd")

        self.horizontalLayout.addWidget(self.gearLcd)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 6, 1, 1)

        self.fwdBtn = QPushButton(self.centralwidget)
        self.fwdBtn.setObjectName(u"fwdBtn")
        sizePolicy1.setHeightForWidth(self.fwdBtn.sizePolicy().hasHeightForWidth())
        self.fwdBtn.setSizePolicy(sizePolicy1)
        self.fwdBtn.setFont(font)

        self.gridLayout_2.addWidget(self.fwdBtn, 0, 7, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy3)
        self.lineEdit_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.speedLcd = QLCDNumber(self.centralwidget)
        self.speedLcd.setObjectName(u"speedLcd")

        self.horizontalLayout_2.addWidget(self.speedLcd)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 8, 1, 1)

        self.gearBtn_3 = QPushButton(self.centralwidget)
        self.gearBtn_3.setObjectName(u"gearBtn_3")
        sizePolicy1.setHeightForWidth(self.gearBtn_3.sizePolicy().hasHeightForWidth())
        self.gearBtn_3.setSizePolicy(sizePolicy1)
        self.gearBtn_3.setFont(font1)

        self.gridLayout_2.addWidget(self.gearBtn_3, 0, 4, 1, 1)

        self.gearBtn_1 = QPushButton(self.centralwidget)
        self.gearBtn_1.setObjectName(u"gearBtn_1")
        sizePolicy1.setHeightForWidth(self.gearBtn_1.sizePolicy().hasHeightForWidth())
        self.gearBtn_1.setSizePolicy(sizePolicy1)
        self.gearBtn_1.setFont(font1)

        self.gridLayout_2.addWidget(self.gearBtn_1, 0, 2, 1, 1)

        self.leftBtn = QPushButton(self.centralwidget)
        self.leftBtn.setObjectName(u"leftBtn")
        sizePolicy1.setHeightForWidth(self.leftBtn.sizePolicy().hasHeightForWidth())
        self.leftBtn.setSizePolicy(sizePolicy1)
        self.leftBtn.setFont(font)

        self.gridLayout_2.addWidget(self.leftBtn, 4, 6, 1, 1)

        self.gearBtn_4 = QPushButton(self.centralwidget)
        self.gearBtn_4.setObjectName(u"gearBtn_4")
        sizePolicy1.setHeightForWidth(self.gearBtn_4.sizePolicy().hasHeightForWidth())
        self.gearBtn_4.setSizePolicy(sizePolicy1)
        self.gearBtn_4.setFont(font1)

        self.gridLayout_2.addWidget(self.gearBtn_4, 0, 5, 1, 1)

        self.gdwnBtn = QPushButton(self.centralwidget)
        self.gdwnBtn.setObjectName(u"gdwnBtn")
        sizePolicy1.setHeightForWidth(self.gdwnBtn.sizePolicy().hasHeightForWidth())
        self.gdwnBtn.setSizePolicy(sizePolicy1)
        self.gdwnBtn.setFont(font)

        self.gridLayout_2.addWidget(self.gdwnBtn, 4, 4, 1, 1)

        self.gupBtn = QPushButton(self.centralwidget)
        self.gupBtn.setObjectName(u"gupBtn")
        sizePolicy1.setHeightForWidth(self.gupBtn.sizePolicy().hasHeightForWidth())
        self.gupBtn.setSizePolicy(sizePolicy1)
        self.gupBtn.setFont(font)

        self.gridLayout_2.addWidget(self.gupBtn, 4, 3, 1, 1)

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
        self.gdwnBtn.pressed.connect(MainWindow.gearDWN)
        self.gearBtn_1.pressed.connect(MainWindow.gearFirst)
        self.gearBtn_2.pressed.connect(MainWindow.gearSecond)
        self.gearBtn_3.pressed.connect(MainWindow.gearThird)
        self.gearBtn_4.pressed.connect(MainWindow.gearFourth)
        self.gupBtn.pressed.connect(MainWindow.gearUP)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.midBtn.setText(QCoreApplication.translate("MainWindow", u"MID", None))
        self.gearBtn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.rightBtn.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.bwdBtn.setText(QCoreApplication.translate("MainWindow", u"BACKWARD", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"GEAR", None))
        self.fwdBtn.setText(QCoreApplication.translate("MainWindow", u"FORWARD", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"SPEED", None))
        self.gearBtn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.gearBtn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.leftBtn.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.gearBtn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.gdwnBtn.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.gupBtn.setText(QCoreApplication.translate("MainWindow", u"UP", None))
    # retranslateUi

