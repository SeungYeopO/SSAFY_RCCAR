# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daily3_231107.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(721, 611)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 551, 701, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.nameChangeButton = QPushButton(self.horizontalLayoutWidget)
        self.nameChangeButton.setObjectName(u"nameChangeButton")
        font1 = QFont()
        font1.setPointSize(10)
        self.nameChangeButton.setFont(font1)

        self.horizontalLayout.addWidget(self.nameChangeButton)

        self.backgroundChangeButton = QPushButton(self.horizontalLayoutWidget)
        self.backgroundChangeButton.setObjectName(u"backgroundChangeButton")
        self.backgroundChangeButton.setFont(font1)

        self.horizontalLayout.addWidget(self.backgroundChangeButton)

        self.startButton = QPushButton(self.horizontalLayoutWidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setFont(font1)

        self.horizontalLayout.addWidget(self.startButton)

        self.backgroundLabel = QLabel(self.centralwidget)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(9, 9, 703, 535))
        self.backgroundLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(220, 160, 48, 16))
        self.nameLabel.setFont(font)
        self.nameLabel.setLayoutDirection(Qt.LeftToRight)
        self.nameLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.backgroundLabel.raise_()
        self.horizontalLayoutWidget.raise_()
        self.nameLabel.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.backgroundChangeButton.clicked.connect(MainWindow.changeBackgroundColor)
        self.nameChangeButton.clicked.connect(MainWindow.changeLabelName)
        self.startButton.clicked.connect(MainWindow.timerStart)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nameChangeButton.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984 \ubcc0\uacbd", None))
        self.backgroundChangeButton.setText(QCoreApplication.translate("MainWindow", u"\ubc30\uacbd\uc0c9 \ubcc0\uacbd", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.backgroundLabel.setText("")
        self.nameLabel.setText("")
    # retranslateUi

