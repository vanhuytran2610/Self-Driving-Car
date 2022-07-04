import WebcamModule as wM
import DataCollectionModule as dcM
import JoyStickModule as jsM
import MotorModule as mM
import cv2
from time import sleep
import random

maxThrottle = 0.5
#maxSteering = 0.3
motor = mM.Motor(6, 13, 12, 26, 21, 20)

record = 0
while True:
    joyVal = jsM.getJS()
    #print(joyVal)
    steering = joyVal['axis1']
    throttle = joyVal['axis2']*(-maxThrottle)
    if joyVal['share'] == 1:
        if record ==0: print('Recording Started ...')
        record +=1
        sleep(0.300)
    if record == 1:
        img = wM.getImg(True,size=[240,120])
        dcM.saveData(img,steering)
    elif record == 2:
        dcM.saveLog()
        record = 0

    motor.move(throttle,-steering)
    cv2.waitKey(1)