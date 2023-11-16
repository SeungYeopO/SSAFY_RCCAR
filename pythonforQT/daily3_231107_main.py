# Qt Designer 에서 signal/slot 등록 후 등록한 slot 함수를 재정의해서 사용하는 샘플 코드

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from daily3_231107 import Ui_MainWindow
import random
import time


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    def changeLabelName(self):
        ret, ok = QInputDialog.getText(self, "이름 변경", "이름을 입력하세요")
        if ok:
            self.nameLabel.setText(ret)
            self.nameLabel.adjustSize()

    def changeBackgroundColor(self):
        color = QColorDialog.getColor().name()
        if color:
            self.nameLabel.setStyleSheet("background-color:%s" % color)

    def timerStart(self):
        print("start")
        self.num = 0
        # QBasicTimer() 객체 생성
        self.timer = QBasicTimer()
        # timer 시작, 500ms 에 한번 timerEvent() 호출
        self.timer.start(1000, self)

    # num = 0
    count = 0

    # timerEvent() 재정의
    def timerEvent(self, event):
        if self.num >= 10:
            # timer 종료
            self.timer.stop()
            text = str(self.count)
            # QMessageBox() 객체 생성
            msg = QMessageBox()
            # About messageBox, 현재 애플리케이션의 빌드 시기 or 버전을 표시하는 정보 창
            msg.about(self, "Result", text)
            self.count = 0

        else:
            self.num += 1
            #print(self.num)
            x = random.randrange(9, self.backgroundLabel.width() - self.nameLabel.width())
            y = random.randrange(9, self.backgroundLabel.height() - self.nameLabel.height())
            self.nameLabel.move(x, y)

    def mousePressEvent(self, event):
        # 마우스의 좌표 정보를 담고 있는 event.x(), event.y()
        press_x = event.x()
        press_y = event.y()
        #print(press_x, press_y)
        #print(self.nameLabel.pos())
        if press_x <= self.nameLabel.pos().x() + self.nameLabel.width() and press_x >= self.nameLabel.pos().x() \
        and press_y <= self.nameLabel.pos().y() + self.nameLabel.height() and press_y >= self.nameLabel.pos().y():
            #print("clicked")
            self.count += 1
            print(self.count)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
