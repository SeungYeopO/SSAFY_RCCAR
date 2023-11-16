# Qt Designer 에서 signal/slot 등록 후 등록한 slot 함수를 재정의해서 사용하는 샘플 코드

from PySide2.QtWidgets import *
from carControlUI2 import Ui_MainWindow
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
        self.motorFlag = False
        self.motorSpeed = 0

    # designer 에서 등록한 ledON() 재정의해서 사용
    def motorON(self):
        if self.motorFlag == False:
            self.motorFlag = True
            self.motorSpeed = 0

            self.speedSlider.setEnabled(True)
            self.dirDial.setEnabled(True)
            self.fwdBtn.setEnabled(True)
            self.bwdBtn.setEnabled(True)
            print('Motor ON')


    # designer 에서 등록한 ledOFF() 재정의해서 사용
    def motorOFF(self):
        if self.motorFlag == True:
            self.motorFlag = False

            self.speedSlider.setValue(0)
            self.dirDial.setValue(350)
            self.speedSlider.setDisabled(True)
            self.dirDial.setDisabled(True)
            self.fwdBtn.setDisabled(True)
            self.bwdBtn.setDisabled(True)

            myMotor.run(Raspi_MotorHAT.RELEASE)
            servo.setPWM(0, 0, 350)
            print('Motor OFF')


    def forward(self):
        if self.motorFlag == True:
            myMotor.setSpeed(self.motorSpeed)
            myMotor.run(Raspi_MotorHAT.FORWARD)

            print('Go Forward')


    def backward(self):
        if self.motorFlag == True:
            myMotor.setSpeed(self.motorSpeed)
            myMotor.run(Raspi_MotorHAT.BACKWARD)

            print('Go Backward')

    def speedTrans(self, val):
        self.motorSpeed = val
        print(val)

    def setDial(self, value):
        if self.motorFlag == True:
            servo.setPWM(0, 0, value)
            print(value)
        # elif self.motorFlag == False:
        #     servo.setPWM(0, 0, 350)
        #     print(value)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()
