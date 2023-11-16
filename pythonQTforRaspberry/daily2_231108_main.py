# 라즈베리파이 이식용 샘플 코드
# 버튼을 누르면 edit의 text를 출력한다.

from PySide2.QtWidgets import *
from daily2_231108 import Ui_MainWindow
from PySide2.QtCore import Qt
from PySide2.QtCore import *

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.upBtn.timer = QTimer()
        self.upBtn.timer.setInterval(100)
        self.downBtn.timer = QTimer()
        self.downBtn.timer.setInterval(100)
        self.upBtn.timer.timeout.connect(self.rundown)
        self.downBtn.timer.timeout.connect(self.runup)
        # 슬라이더의 값이 변경될 때, run() 호출
        self.speedSlider.valueChanged.connect(self.speedTrans)
        # 슬라이더의 pageStep 변경
        self.speedSlider.setPageStep(10)
        # 슬라이더의 최대값 변경
        self.speedSlider.setMaximum(100)

    def speedTrans(self, val):
        self.speed = 100 - val
        self.upBtn.timer.setInterval(self.speed)
        self.downBtn.timer.setInterval(self.speed)
        print(val)

    def up(self):
        self.upBtn.timer.start()

    def down(self):
        self.downBtn.timer.start()

    def runup(self):
        #print(self.progressBar.value())
        self.progressBar.setValue(self.progressBar.value() + 1)
        if self.progressBar.value() == 100:
            self.upBtn.timer.stop()

    def rundown(self):
        #print(self.progressBar.value())
        self.progressBar.setValue(self.progressBar.value() - 1)
        if self.progressBar.value() == 0:
            self.downBtn.timer.stop()

    def stop(self):
        self.upBtn.timer.stop()
        self.downBtn.timer.stop()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()
