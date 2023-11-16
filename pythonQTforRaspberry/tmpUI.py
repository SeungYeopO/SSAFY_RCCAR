# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daily2_231107.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QDial, QLCDNumber, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(601, 722)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.onButton = QPushButton(self.centralwidget)
        self.onButton.setObjectName(u"onButton")
        self.onButton.setGeometry(QRect(40, 20, 251, 71))
        self.offButton = QPushButton(self.centralwidget)
        self.offButton.setObjectName(u"offButton")
        self.offButton.setGeometry(QRect(320, 20, 241, 71))
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(40, 110, 521, 291))
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(190, 420, 211, 221))
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 601, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.onButton.clicked.connect(MainWindow.ledON)
        self.offButton.clicked.connect(MainWindow.ledOFF)
        self.dial.valueChanged.connect(MainWindow.setDial)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.onButton.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.offButton.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
    # retranslateUi

