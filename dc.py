from adafruit_motorkit import MotorKit
import sys
kit = MotorKit()
motor = sys.argv[1]
motor_list = {'1': kit.motor1, '2': kit.motor2, '3': kit.motor3}


state = int(sys.argv[2])

if '-' in sys.argv[2]:
        state = -1
motor_list[motor].throttle = state
