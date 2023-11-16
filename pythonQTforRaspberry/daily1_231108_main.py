# 라즈베리파이 이식용 샘플 코드
# 버튼을 누르면 edit의 text를 출력한다.

from PySide2.QtWidgets import *
from daily1_231108 import Ui_MainWindow
from PySide2.QtCore import Qt
from PySide2.QtCore import *

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def main(self):
        pass

    def goClick(self):
        print('go clicked')
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.run)
        self.timer.start()

    def run(self):
        print('progressing')
        self.progressBar.setValue(self.progressBar.value() + 1)
        if self.progressBar.value() == 100:
            self.timer.stop()

    def pauseClick(self):
        print('pause clicked')
        self.timer.stop()


    def resetClick(self):
        print('reset clicked')
        # progressBar 의 값을 0으로 설정
        self.progressBar.setValue(0)
        # progressBar 의 진행 방향을 수직으로 설정, Qt.Horizontal 옵션을 넣으면, 수평 방향으로 바꿀 수 있다.
        self.progressBar.setOrientation(Qt.Horizontal)
        # progressBar 의 진행 방향을 정방향으로 설정, True로 변경하면, 역방향이 된다.
        self.progressBar.setInvertedAppearance(False)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()
