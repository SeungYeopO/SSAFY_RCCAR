# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'carControlUI.ui'
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
        MainWindow.resize(721, 611)
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

        self.gridLayout.addWidget(self.rightBtn, 1, 2, 1, 1)

        self.fwdBtn = QPushButton(self.centralwidget)
        self.fwdBtn.setObjectName(u"fwdBtn")
        sizePolicy.setHeightForWidth(self.fwdBtn.sizePolicy().hasHeightForWidth())
        self.fwdBtn.setSizePolicy(sizePolicy)
        self.fwdBtn.setFont(font)

        self.gridLayout.addWidget(self.fwdBtn, 0, 1, 1, 1)

        self.stopBtn = QPushButton(self.centralwidget)
        self.stopBtn.setObjectName(u"stopBtn")
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)
        self.stopBtn.setFont(font)

        self.gridLayout.addWidget(self.stopBtn, 1, 1, 1, 1)

        self.leftBtn = QPushButton(self.centralwidget)
        self.leftBtn.setObjectName(u"leftBtn")
        sizePolicy.setHeightForWidth(self.leftBtn.sizePolicy().hasHeightForWidth())
        self.leftBtn.setSizePolicy(sizePolicy)
        self.leftBtn.setFont(font)

        self.gridLayout.addWidget(self.leftBtn, 1, 0, 1, 1)

        self.bwdBtn = QPushButton(self.centralwidget)
        self.bwdBtn.setObjectName(u"bwdBtn")
        sizePolicy.setHeightForWidth(self.bwdBtn.sizePolicy().hasHeightForWidth())
        self.bwdBtn.setSizePolicy(sizePolicy)
        self.bwdBtn.setFont(font)

        self.gridLayout.addWidget(self.bwdBtn, 2, 1, 1, 1)

        self.midBtn = QPushButton(self.centralwidget)
        self.midBtn.setObjectName(u"midBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.midBtn.sizePolicy().hasHeightForWidth())
        self.midBtn.setSizePolicy(sizePolicy1)
        self.midBtn.setFont(font)

        self.gridLayout.addWidget(self.midBtn, 0, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dirDial = QDial(self.centralwidget)
        self.dirDial.setObjectName(u"dirDial")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dirDial.sizePolicy().hasHeightForWidth())
        self.dirDial.setSizePolicy(sizePolicy2)
        self.dirDial.setMinimum(250)
        self.dirDial.setMaximum(420)

        self.horizontalLayout.addWidget(self.dirDial)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_7)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.speedSlider = QSlider(self.centralwidget)
        self.speedSlider.setObjectName(u"speedSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(7)
        sizePolicy3.setHeightForWidth(self.speedSlider.sizePolicy().hasHeightForWidth())
        self.speedSlider.setSizePolicy(sizePolicy3)
        self.speedSlider.setMaximum(250)
        self.speedSlider.setSingleStep(10)
        self.speedSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.speedSlider)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.leftBtn.clicked.connect(MainWindow.left)
        self.rightBtn.clicked.connect(MainWindow.right)
        self.stopBtn.clicked.connect(MainWindow.stop)
        self.midBtn.clicked.connect(MainWindow.mid)
        self.fwdBtn.clicked.connect(MainWindow.forward)
        self.bwdBtn.clicked.connect(MainWindow.backward)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rightBtn.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.fwdBtn.setText(QCoreApplication.translate("MainWindow", u"FORWARD", None))
        self.stopBtn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.leftBtn.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.bwdBtn.setText(QCoreApplication.translate("MainWindow", u"BACKWARD", None))
        self.midBtn.setText(QCoreApplication.translate("MainWindow", u"MID", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
    # retranslateUi

