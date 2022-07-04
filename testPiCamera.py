import cv2

img = cv2.VideoCapture(0)
img.set(3,240)
img.set(3,480)
while True:
    result, image = img.read()
    image = cv2.resize(image, (240,120))
    cv2.imshow('Result',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break