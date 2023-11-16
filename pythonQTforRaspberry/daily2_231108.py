# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daily2_231108.ui'
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
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(70, 60, 321, 411))
        self.progressBar.setValue(50)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Vertical)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(470, 310, 201, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.speed_label = QLabel(self.verticalLayoutWidget)
        self.speed_label.setObjectName(u"speed_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_label.sizePolicy().hasHeightForWidth())
        self.speed_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.speed_label.setFont(font)
        self.speed_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.speed_label)

        self.speedSlider = QSlider(self.verticalLayoutWidget)
        self.speedSlider.setObjectName(u"speedSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.speedSlider.sizePolicy().hasHeightForWidth())
        self.speedSlider.setSizePolicy(sizePolicy1)
        self.speedSlider.setMaximum(100)
        self.speedSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.speedSlider)

        self.upBtn = QPushButton(self.centralwidget)
        self.upBtn.setObjectName(u"upBtn")
        self.upBtn.setGeometry(QRect(470, 140, 201, 41))
        self.upBtn.setFont(font)
        self.downBtn = QPushButton(self.centralwidget)
        self.downBtn.setObjectName(u"downBtn")
        self.downBtn.setGeometry(QRect(470, 220, 201, 41))
        self.downBtn.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.upBtn.pressed.connect(MainWindow.up)
        self.downBtn.pressed.connect(MainWindow.down)
        self.speedSlider.valueChanged.connect(MainWindow.speedTrans)
        self.upBtn.released.connect(MainWindow.stop)
        self.downBtn.released.connect(MainWindow.stop)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\ud130 \uc18d\ub3c4 \uc81c\uc5b4", None))
        self.upBtn.setText(QCoreApplication.translate("MainWindow", u"UP", None))
        self.downBtn.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
    # retranslateUi
