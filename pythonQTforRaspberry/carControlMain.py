# Qt Designer 에서 signal/slot 등록 후 등록한 slot 함수를 재정의해서 사용하는 샘플 코드

from PySide2.QtWidgets import *
from carControlUI import Ui_MainWindow
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2) #핀번호

servo = PWM(0x6F)
servo.setPWMFreq(60)  # Set frequency to 60 Hz


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        #self.flag = False
        pass

    # designer 에서 등록한 ledON() 재정의해서 사용
    def mid(self):
        print('direction: mid')
        servo.setPWM(0, 0, 350)

    # designer 에서 등록한 ledOFF() 재정의해서 사용
    def right(self):
        print('direction: right')
        servo.setPWM(0, 0, 420)

    def left(self):
        print('direction: left')
        servo.setPWM(0, 0, 280)

    # designer 에서 등록한 ledOFF() 재정의해서 사용
    def forward(self):
        print('forward')
        myMotor.setSpeed(200)
        myMotor.run(Raspi_MotorHAT.FORWARD)

    def backward(self):
        print('backward')
        myMotor.setSpeed(200)
        myMotor.run(Raspi_MotorHAT.BACKWARD)

    def stop(self):
        print('stop')
        myMotor.run(Raspi_MotorHAT.RELEASE)

    # def setDial(self, value):
    #     if self.flag == True:
    #         self.lcdNumber.display(value)
    #         led.value = value/100
    #     elif self.flag == False:
    #         self.lcdNumber.display(0)
    #         led.value = 0


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()
