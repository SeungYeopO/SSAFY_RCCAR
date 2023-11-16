# 라즈베리파이 이식용 샘플 코드
# 버튼을 누르면 edit의 text를 출력한다.

from PySide2.QtWidgets import *
from daily3_231108 import Ui_MainWindow
from PySide2.QtCore import *
from time import sleep

# QThread를 상속 받은 class 생성
class MyThread(QThread):
    mySignal = Signal(int)
    def __init__(self):
        super().__init__()

    flag = False

    # thread 가 start() 되면, 동작하는 함수
    def run(self):
        self.flag = True
        while self.flag:
            self.mySignal.emit(1)
            sleep(0.1)

    # thread 가 stop() 되면, 동작하는수함수
    def stop(self):
        self.flag = False
        print("Thread Stop")

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        # MyThread() 객체 생성
        self.th = MyThread()
        self.th.mySignal.connect(self.download)

    # 버튼 누르면 호출되는 함수
    def download(self, val):
        self.th.start()
        # thread 시작 -> MyThread() 의 run() 실행
        self.progressBar_1.setValue(self.progressBar_1.value() + val)
        if self.progressBar_1.value() == 100:
            self.progressBar_2.setValue(self.progressBar_2.value() + val)
            if self.progressBar_2.value() == 100:
                self.progressBar_3.setValue(self.progressBar_3.value() + val)
                if self.progressBar_3.value() == 100:
                    self.progressBar_4.setValue(self.progressBar_4.value() + val)
                    if self.progressBar_4.value() == 100:
                        self.progressBar_5.setValue(self.progressBar_5.value() + val)
                        if self.progressBar_5.value() == 100:
                            self.th.stop()



if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()
