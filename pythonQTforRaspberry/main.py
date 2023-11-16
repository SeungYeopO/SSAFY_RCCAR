# 라즈베리파이 이식용 샘플 코드
# 버튼을 누르면 edit의 text를 출력한다.

from PySide2.QtWidgets import *
from mainUI import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def go(self):
        print(self.edit.text())


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()
