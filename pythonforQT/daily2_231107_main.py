# Qt Designer 에서 signal/slot 등록 후 등록한 slot 함수를 재정의해서 사용하는 샘플 코드

from PySide6.QtWidgets import *
from daily2_231107 import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    # designer 에서 등록한 ledON() 재정의해서 사용
    def ledON(self):
        print('led ON')
    # designer 에서 등록한 ledOFF() 재정의해서 사용
    def ledOFF(self):
        print('led OFF')

    def setDial(self, value):
        self.lcdNumber.display(value)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
