# Qt Designer 에서 signal/slot 등록 후 등록한 slot 함수를 재정의해서 사용하는 샘플 코드

from PySide2.QtWidgets import *
from tmpUI import Ui_MainWindow
from gpiozero import PWMLED
from time import sleep

led = PWMLED(14)

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.flag = False

    # designer 에서 등록한 ledON() 재정의해서 사용
    def ledON(self):
        led.value = 1
        print('led ON')
        self.flag = True
        self.setDial(self.dial.value())

    # designer 에서 등록한 ledOFF() 재정의해서 사용
    def ledOFF(self):
        led.value = 0
        print('led OFF')
        self.flag = False
        self.setDial(0)

    def setDial(self, value):
        if self.flag == True:
            self.lcdNumber.display(value)
            led.value = value/100
        elif self.flag == False:
            self.lcdNumber.display(0)
            led.value = 0




if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()
