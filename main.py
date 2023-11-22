from PySide2.QtWidgets import *
from PySide2.QtCore import *

from ui.car_ui import Ui_MainWindow
from db.db_conncetor import Connector
from motor.controller import MotorController, FORWARD, BACKWARD, MID, LEFT, RIGHT

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
        self.main()
        self.init()

    def init(self):
        self.connector = Connector(DB_ADDR, DB_USERNAME, DB_PASSWORD, DB_NAME)
        self.controller = MotorController()

    def main(self):
        pass

    def printLCD(self):
        self.gearLcd.display(self.gear)
        self.speedLcd.display(self.speed)
        if self.gear == 1:
            self.gearBtn_1.setEnabled(True)
            self.gearBtn_2.setDisabled(True)
            self.gearBtn_3.setDisabled(True)
            self.gearBtn_4.setDisabled(True)

        elif self.gear == 2:
            self.gearBtn_1.setDisabled(True)
            self.gearBtn_2.setEnabled(True)
            self.gearBtn_3.setDisabled(True)
            self.gearBtn_4.setDisabled(True)

        elif self.gear == 3:
            self.gearBtn_1.setDisabled(True)
            self.gearBtn_2.setDisabled(True)
            self.gearBtn_3.setEnabled(True)
            self.gearBtn_4.setDisabled(True)

        elif self.gear == 4:
            self.gearBtn_1.setDisabled(True)
            self.gearBtn_2.setDisabled(True)
            self.gearBtn_3.setDisabled(True)
            self.gearBtn_4.setEnabled(True)

    def gear2speed(self, gear):
        if gear == 1:
            self.speed = 50
        elif gear == 2:
            self.speed = 100
        elif gear == 3:
            self.speed = 150
        elif gear == 4:
            self.speed = 200

    def forward(self):
        print('fwd')
        self.controller.dir = FORWARD
        self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def backward(self):
        print('bwd')
        self.controller.dir = BACKWARD
        self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def left(self):
        print('left')
        self.controller.wheel_dir = LEFT
        self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def right(self):
        print('right')
        self.controller.wheel_dir = RIGHT
        self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def mid(self):
        print('mid')
        self.speed = 0
        self.printLCD()
        self.controller.wheel_dir = MID
        self.connector.send("command", self.controller.dir, self.controller.wheel_dir, f"{self.controller.gear}")

    def gearUP(self):
        print('gear up')

        if self.gear < 4:
            self.gear += 1
        else:
            print("Highest Gear")

        self.gear2speed(self.gear)
        self.printLCD()

    def gearDWN(self):
        print('gear down')

        if self.gear > 1:
            self.gear -= 1
        else:
            print("Loweset Gear")

        self.gear2speed(self.gear)
        self.printLCD()

    def gearFirst(self):
        self.gear = 1
        print('gear 1')
        #self.gearLcd.display(self.gear)
        self.gear2speed(self.gear)
        self.printLCD()

    def gearSecond(self):
        self.gear = 2
        self.speed = 100
        print('gear 2')
        #self.gearLcd.display(self.gear)
        self.gear2speed(self.gear)
        self.printLCD()

    def gearThird(self):
        self.gear = 3
        print('gear 3')
        #self.gearLcd.display(self.gear)
        self.gear2speed(self.gear)
        self.printLCD()

    def gearFourth(self):
        self.gear = 4
        self.speed = 200
        print('gear 4')
        #self.gearLcd.display(self.gear)
        self.gear2speed(self.gear)
        self.printLCD()


    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Return, Qt.Key_Enter]:
            print('Enter')
        elif e.key() == Qt.Key_Escape:
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


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()