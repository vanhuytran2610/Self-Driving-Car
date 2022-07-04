import cv2
import numpy as np
import tensorflow as tf
import WebcamModule as wM
import MotorModule as mM
import KeyPressModule as kp
######################################

steeringSen = 0.7 # Steering Sensitivity
maxThrottle = 0.34  # Forward Speed %
motor = mM.Motor(6, 13, 12, 26, 21, 20) # Pin Numbers

interpreter = tf.lite.Interpreter(model_path="model_3.tflite")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()                   
######################################

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

while True:
    img = wM.getImg(True, size=[240, 120])
    img = np.asarray(img)
    img = preProcess(img)
    img = np.array([img], dtype=np.float32)
    
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])
    steering = float(predictions)
    print(steering*steeringSen)
    
    motor.move(maxThrottle,-steering*steeringSen)    

    cv2.waitKey(1)

