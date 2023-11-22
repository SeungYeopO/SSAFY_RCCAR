from motor.Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from motor.Raspi_PWM_Servo_Driver import PWM

FORWARD = 0
BACKWARD = 1

MID = 0
LEFT = 1
RIGHT = 2

class MotorController():
    def __init__(self):
        self.motor_hat = Raspi_MotorHAT(addr=0x6f)
        self.main_motor = self.motor_hat.getMotor(2)
        self.servo_motor = PWM(0x6F)
        self.servo_motor.setPWMFreq(60)
        self.gear = 1
        self.speed = 0
        self.dir = FORWARD
        self.wheel_dir = MID
    
    def set_dir(self, dir):
        if dir == FORWARD:
            self.dir = FORWARD
        elif dir == BACKWARD:
            self.dir = BACKWARD

    def set_wheel_dir(self, w_dir):
        if w_dir == MID:
            self.wheel_dir = MID
            self.servo_motor.setPWM(0, 0, 350)
            print("WHEEL DIR : MID")
        elif w_dir == LEFT:
            self.wheel_dir = LEFT
            self.servo_motor.setPWM(0, 0, 400)
            print("WHEEL DIR : LEFT")
        elif w_dir == RIGHT:
            self.wheel_dir = RIGHT
            self.servo_motor.setPWM(0, 0, 300)
            print("WHEEL DIR : RIGHT")

    def set_gear(self, step):
        self.gear = step
        print(f"GEAR : {step}")
        pass

    def set_speed(self, speed):
        self.speed = speed
        self.main_motor.setSpeed(self.speed)
        print(f"SPEED : {speed}")
        pass

    def stop(self):
        self.speed = 0
        self.main_motor.setSpeed(self.speed)
        print("STOP")
        pass

    def terminate(self):
        self.set_wheel_dir(MID)
        self.stop()
        pass




    
    
        