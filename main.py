from PySide2.QtWidgets import *
from PySide2.QtCore import *

from ui.car_ui import Ui_MainWindow
from db.db_connector import Connector
from motor.controller import MotorController, FORWARD, BACKWARD, MID, LEFT, RIGHT, STOP

DB_ADDR = "43.202.6.43"
DB_USERNAME = "user"
DB_PASSWORD = "1234"
DB_NAME = "driveDB"

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('key')
        self.setupUi(self)
        self.setFixedSize(1080, 360)
        self.init()
        self.timer_init()


    def init(self):
        self.connector = Connector(DB_ADDR, DB_USERNAME, DB_PASSWORD, DB_NAME)
        self.controller = MotorController()

    def timer_init(self):
        self.tm = QTimer()
        self.tm.setInterval(500)
        self.tm.timeout.connect(self.send2database)
        self.tm.start()

    def printLCD(self):
        self.gearLcd.display(self.controller.gear)
        self.speedLcd.display(self.controller.speed)
        if self.controller.gear == 1:
            self.gearBtn_1.setEnabled(True)
            self.gearBtn_2.setDisabled(True)
            self.gearBtn_3.setDisabled(True)
            self.gearBtn_4.setDisabled(True)

        elif self.controller.gear == 2:
            self.gearBtn_1.setDisabled(True)
            self.gearBtn_2.setEnabled(True)
            self.gearBtn_3.setDisabled(True)
            self.gearBtn_4.setDisabled(True)

        elif self.controller.gear == 3:
            self.gearBtn_1.setDisabled(True)
            self.gearBtn_2.setDisabled(True)
            self.gearBtn_3.setEnabled(True)
            self.gearBtn_4.setDisabled(True)

        elif self.controller.gear == 4:
            self.gearBtn_1.setDisabled(True)
            self.gearBtn_2.setDisabled(True)
            self.gearBtn_3.setDisabled(True)
            self.gearBtn_4.setEnabled(True)


    def forward(self):
        # print('fwd')
        self.controller.set_dir(FORWARD)
        self.controller.set_speed()
        # self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def backward(self):
        # print('bwd')
        self.controller.set_dir(BACKWARD)
        self.controller.set_speed()
        # self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def left(self):
        # print('left')
        self.controller.set_wheel_dir(LEFT)
        # self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def right(self):
        # print('right')
        self.controller.set_wheel_dir(RIGHT)
        # self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def mid(self):
        # print('mid')
        self.controller.set_wheel_dir(MID)
        self.controller.set_speed()
        self.printLCD()
        # self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def stop(self):
        self.controller.set_dir(STOP)
        self.controller.set_speed()
        self.printLCD()

    def gearUP(self):
        # print('gear up')

        if self.controller.gear < 4:
            self.controller.set_gear(self.controller.gear + 1)
        else:
            print("Highest Gear")

        self.controller.set_speed()
        self.printLCD()

    def gearDWN(self):
        # print('gear down')

        if self.controller.gear > 1:
            self.controller.set_gear(self.controller.gear - 1)
        else:
            print("Loweset Gear")

        self.printLCD()

    def gearFirst(self):
        self.controller.set_gear(1)
        # print('gear 1')
        self.printLCD()

    def gearSecond(self):
        self.controller.set_gear(2)
        self.speed = 100
        # print('gear 2')
        self.printLCD()

    def gearThird(self):
        self.controller.set_gear(3)
        # print('gear 3')
        self.printLCD()

    def gearFourth(self):
        self.controller.set_gear(4)
        self.speed = 200
        # print('gear 4')
        self.printLCD()


    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Return, Qt.Key_Enter]:
            # print('Enter')
            pass
        elif e.key() == Qt.Key_Escape:
            # print("Escaped")
            self.connector.close()
            self.controller.terminate()
            self.close()
        elif e.key() == Qt.Key_K:
            self.right()
            self.rightBtn.setDisabled(True)
        elif e.key() == Qt.Key_H:
            self.left()
            self.leftBtn.setDisabled(True)
        elif e.key() == Qt.Key_U:
            self.forward()
            self.fwdBtn.setDisabled(True)
        elif e.key() == Qt.Key_J:
            self.backward()
            self.bwdBtn.setDisabled(True)
        elif e.key() == Qt.Key_Q:
            self.gearUP()
            self.gupBtn.setDisabled(True)
        elif e.key() == Qt.Key_W:
            self.gearDWN()
            self.gdwnBtn.setDisabled(True)
        elif e.key() == Qt.Key_Space:
            self.mid()
        elif e.key() == Qt.Key_S:
            self.stop()

        elif e.key() == Qt.Key_1:
            self.gearFirst()
        elif e.key() == Qt.Key_2:
            self.gearSecond()
        elif e.key() == Qt.Key_3:
            self.gearThird()
        elif e.key() == Qt.Key_4:
            self.gearFourth()

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_H:
            self.leftBtn.setEnabled(True)
        elif e.key() == Qt.Key_K:
            self.rightBtn.setEnabled(True)
        elif e.key() == Qt.Key_U:
            self.fwdBtn.setEnabled(True)
        elif e.key() == Qt.Key_J:
            self.bwdBtn.setEnabled(True)
        elif e.key() == Qt.Key_Q:
            self.gupBtn.setEnabled(True)
        elif e.key() == Qt.Key_W:
            self.gdwnBtn.setEnabled(True)

    def send2database(self):
        self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")
        print(".", end="")
        return


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()