import cv2 
import pickle

img  = cv2.imread("carParkImg.png")
width,height=107,48 # width = 157 - 50 , height = 240-192
# cv2.rectangle(img, (50, 192), (157, 240), (255, 0, 0), 2)
try:
    with open('CarParkPosition', 'rb') as f:
        posList = pickle.load(f)
except:

    posList=[]


def onthego(event, x, y, flags, params):
    print(x)
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1< y <y1 + height :
                posList.pop(i)

    with open('CarParkPosition','wb') as f :
        pickle.dump(posList,f)





while True:
    img = cv2.imread("carParkImg.png")
    for pos in posList:
       cv2.rectangle(img, pos,(pos[0]+width,pos[1]+height), (255, 0, 0), 2)
       
    #    cv2.rectangle(img, (50, 192), (157, 240), (255, 0, 0), 2)
    winname = "abc"
    cv2.namedWindow(winname)
    cv2.setMouseCallback(winname, onthego)
    cv2.imshow(winname, img)
    cv2.waitKey(1)
