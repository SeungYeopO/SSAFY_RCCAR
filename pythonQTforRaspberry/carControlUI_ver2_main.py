import sys
from PySide2.QtWidgets import *
from carControlUI_ver2 import Ui_MainWindow
from PySide2.QtCore import Qt

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('key')
        self.setupUi(self)
        self.main()
        self.setFixedSize(600, 360)
        self.show()

    def main(self):
        pass

    def forward(self):
        print('fwd')

    def backward(self):
        print('bwd')

    def left(self):
        print('left')

    def right(self):
        print('right')

    def mid(self):
        print('mid')

    def gearUP(self):
        print('gear up')

    def gearDWN(self):
        print('gear down')

    def gearFirst(self):
        print('gear 1')
        self.gearBtn_1.setEnabled(True)
        self.gearBtn_2.setDisabled(True)
        self.gearBtn_3.setDisabled(True)
        self.gearBtn_4.setDisabled(True)

    def gearSecond(self):
        print('gear 2')
        self.gearBtn_1.setDisabled(True)
        self.gearBtn_2.setEnabled(True)
        self.gearBtn_3.setDisabled(True)
        self.gearBtn_4.setDisabled(True)

    def gearThird(self):
        print('gear 3')
        self.gearBtn_1.setDisabled(True)
        self.gearBtn_2.setDisabled(True)
        self.gearBtn_3.setEnabled(True)
        self.gearBtn_4.setDisabled(True)

    def gearFourth(self):
        print('gear 4')
        self.gearBtn_1.setDisabled(True)
        self.gearBtn_2.setDisabled(True)
        self.gearBtn_3.setDisabled(True)
        self.gearBtn_4.setEnabled(True)

    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Return, Qt.Key_Enter]:
            print('Enter')
        elif e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_K:
            self.right()
        elif e.key() == Qt.Key_H:
            self.left()
        elif e.key() == Qt.Key_U:
            self.forward()
        elif e.key() == Qt.Key_J:
            self.backward()
        elif e.key() == Qt.Key_Q:
            self.gearUP()
        elif e.key() == Qt.Key_W:
            self.gearDWN()
        elif e.key() == Qt.Key_1:
            self.gearFirst()
        elif e.key() == Qt.Key_2:
            self.gearSecond()
        elif e.key() == Qt.Key_3:
            self.gearThird()
        elif e.key() == Qt.Key_4:
            self.gearFourth()

        # if not control and isPrintable(e.key()):
        #     print(e.text())


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()