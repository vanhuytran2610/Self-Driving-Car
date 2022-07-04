from MotorModule import Motor
import KeyPressModule as kp

motor = Motor(6, 13, 12, 26, 21, 20)

kp.init()

def main():
    if kp.getKey('UP'):
        motor.move(0.6,0,0.1)
    elif kp.getKey('DOWN'):
        motor.move(-0.6,0,0.1)
    elif kp.getKey('LEFT'):
        motor.move(0.3,0.5,0.1)
    elif kp.getKey('RIGHT'):
        motor.move(0.3,-0.5,0.1)
        #motor.stop()
    else:
        motor.stop(0.1)

if __name__ == '__main__':
    while True:
        main()