from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
from gpiozero import DistanceSensor
from time import sleep

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2) #핀번호

servo = PWM(0x6F)
servo.setPWMFreq(60)  # Set frequency to 60 Hz

sensor = DistanceSensor(echo=15, trigger=14)
speed = 50

def speedUP(acc):
    acc += 10
    if acc >= 300:
        return acc - 10
    return acc

def speedDOWN(acc):
    acc -= 10
    if acc <=50:
        return acc + 10
    return acc

while True:
    dist = sensor.distance

    dist = dist * 100
    dist = int(dist)
    if dist > 8:
        speed = speedUP(speed)
        up_flag = 1
    elif dist < 7:
        speed = speedDOWN(speed)
        down_flag = 1
    elif dist <= 2:
        speed = 0

    myMotor.setSpeed(speed)
    myMotor.run(Raspi_MotorHAT.FORWARD)

    print(dist, 'cm', speed, 'm/h')
    sleep(0.01)
