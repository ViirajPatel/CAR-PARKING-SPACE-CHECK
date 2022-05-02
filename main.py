import cv2
import pickle
import cvzone
import numpy as np


cap = cv2.VideoCapture("carPark.mp4")
with open('CarParkPosition', 'rb') as f:
    posList = pickle.load(f)
width, height = 107, 48

def check(imgP):
    count = 0
    for pos in posList:
        x, y = pos

        imgCrop = imgP[y:y+height, x:x+width]
        
        countPixels = cv2.countNonZero(imgCrop)


        if int(countPixels) < 900:
            color = (0,255,0)
            thickness = 5
            count+=1
        else:
            color=(0,0,255)
            thickness = 0
        cvzone.putTextRect(img,str(countPixels),(x,y+height-10),scale=1,thickness=1,offset=0,)

        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, thickness)
    outstr = f"Freespace : {count}/{len(posList)}"
    cvzone.putTextRect(img, outstr, (100, 50), scale=5,
                       thickness=5, offset=0, colorR=(0, 0, 0))


while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)   
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imgMedian,kernel,iterations=1)
    check(imgDilate)
    img = cv2.resize(img, (1920 , 1080))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

 
   
  
