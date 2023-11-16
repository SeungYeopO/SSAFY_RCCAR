# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'carControlUI2.ui'
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
        MainWindow.resize(925, 420)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.dirDial = QDial(self.centralwidget)
        self.dirDial.setObjectName(u"dirDial")
        self.dirDial.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dirDial.sizePolicy().hasHeightForWidth())
        self.dirDial.setSizePolicy(sizePolicy1)
        self.dirDial.setMinimum(280)
        self.dirDial.setMaximum(420)
        self.dirDial.setSingleStep(10)
        self.dirDial.setPageStep(10)
        self.dirDial.setValue(350)
        self.dirDial.setOrientation(Qt.Horizontal)
        self.dirDial.setInvertedControls(False)

        self.horizontalLayout.addWidget(self.dirDial)

        self.speedSlider = QSlider(self.centralwidget)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(7)
        sizePolicy2.setHeightForWidth(self.speedSlider.sizePolicy().hasHeightForWidth())
        self.speedSlider.setSizePolicy(sizePolicy2)
        self.speedSlider.setMaximum(250)
        self.speedSlider.setSingleStep(10)
        self.speedSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.speedSlider)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.fwdBtn = QPushButton(self.centralwidget)
        self.fwdBtn.setObjectName(u"fwdBtn")
        self.fwdBtn.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fwdBtn.sizePolicy().hasHeightForWidth())
        self.fwdBtn.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fwdBtn.setFont(font)

        self.gridLayout_2.addWidget(self.fwdBtn, 1, 0, 1, 1)

        self.offBtn = QPushButton(self.centralwidget)
        self.offBtn.setObjectName(u"offBtn")
        sizePolicy3.setHeightForWidth(self.offBtn.sizePolicy().hasHeightForWidth())
        self.offBtn.setSizePolicy(sizePolicy3)
        self.offBtn.setFont(font)

        self.gridLayout_2.addWidget(self.offBtn, 0, 1, 1, 1)

        self.onBtn = QPushButton(self.centralwidget)
        self.onBtn.setObjectName(u"onBtn")
        sizePolicy3.setHeightForWidth(self.onBtn.sizePolicy().hasHeightForWidth())
        self.onBtn.setSizePolicy(sizePolicy3)
        self.onBtn.setFont(font)

        self.gridLayout_2.addWidget(self.onBtn, 0, 0, 1, 1)

        self.bwdBtn = QPushButton(self.centralwidget)
        self.bwdBtn.setObjectName(u"bwdBtn")
        self.bwdBtn.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.bwdBtn.sizePolicy().hasHeightForWidth())
        self.bwdBtn.setSizePolicy(sizePolicy3)
        self.bwdBtn.setFont(font)

        self.gridLayout_2.addWidget(self.bwdBtn, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.speedSlider.valueChanged.connect(MainWindow.speedTrans)
        self.onBtn.clicked.connect(MainWindow.motorON)
        self.offBtn.clicked.connect(MainWindow.motorOFF)
        self.fwdBtn.clicked.connect(MainWindow.forward)
        self.bwdBtn.clicked.connect(MainWindow.backward)
        self.dirDial.valueChanged.connect(MainWindow.setDial)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fwdBtn.setText(QCoreApplication.translate("MainWindow", u"FORWARD", None))
        self.offBtn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.onBtn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.bwdBtn.setText(QCoreApplication.translate("MainWindow", u"BACKWARD", None))
    # retranslateUi

