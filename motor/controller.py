from motor.Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from motor.Raspi_PWM_Servo_Driver import PWM

STOP = 0
FORWARD = 1
BACKWARD = 2

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
        self.speed_profile = [0, 50, 100, 150, 200]
        self.dir = STOP
        self.wheel_dir = MID
    
    def set_dir(self, dir):
        if dir == STOP:
            self.dir = STOP
        elif dir == FORWARD:
            self.dir = FORWARD
        elif dir == BACKWARD:
            self.dir = BACKWARD

    def set_wheel_dir(self, w_dir):
        if w_dir == MID:
            self.wheel_dir = MID
            self.servo_motor.setPWM(0, 0, 350)
            # print("WHEEL DIR : MID")
        elif w_dir == LEFT:
            self.wheel_dir = LEFT
            self.servo_motor.setPWM(0, 0, 300)
            # print("WHEEL DIR : LEFT")
        elif w_dir == RIGHT:
            self.wheel_dir = RIGHT
            self.servo_motor.setPWM(0, 0, 400)
            # print("WHEEL DIR : RIGHT")

    def set_gear(self, step):
        self.gear = step
        # print(f"GEAR : {step}")
        self.set_speed()
        return

    def set_speed(self):
        self.speed = self.speed_profile[self.gear]
        # print(f"DIR : {self.dir}")
        # print(f"SPEED : {self.speed}")
        
        self.main_motor.setSpeed(self.speed)

        if self.dir == STOP:
            self.main_motor.run(Raspi_MotorHAT.RELEASE)
            # print("MOTOR RELEASE")
        elif self.dir == FORWARD:
            self.main_motor.run(Raspi_MotorHAT.FORWARD)
            # print("MOTOR FORWARD")
        elif self.dir == BACKWARD:
            self.main_motor.run(Raspi_MotorHAT.BACKWARD)
            # print("MOTOR BACKWARD")
        return

    def stop(self):
        self.set_dir(STOP)
        self.set_speed()
        # print("STOP")
        return

    def terminate(self):
        self.set_wheel_dir(MID)
        self.stop()
        return




    
    
        