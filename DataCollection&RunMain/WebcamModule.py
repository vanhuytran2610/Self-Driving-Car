import cv2
import time

cap = cv2.VideoCapture(0)
#fps = cap.get(cv2.CAP_PROP_FPS)
#num_frames = 1

def getImg(display= False,size=[480,240]):
    #start = time.time()
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    #sum = 0
    #N = 100
    #for i in range(0,N):
    #    for j in range(0,N):
    #        sum +=1
    #end = time.time()
    #seconds = end - start
    #fps = num_frames / seconds
    if display:
        #cv2.putText(img, "FPS: " + str(round(fps)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('IMG',img)
    return img


if __name__ == '__main__':
    while True:
        img = getImg(True)
        #if img is None:
        #    print("No frame")
        #    break