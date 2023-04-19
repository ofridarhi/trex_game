import cv2
import numpy as np
import utlis

webcam = False

path = 'assets/cards.png'
cap = cv2.VideoCapture(0)
cap.set(10,169)
cap.set(3,1920)
cap.set(4,1080)

wP =210
hP = 297
scale = 3


while True:
    if webcam: _,img = cap.read()
    else: img = cv2.imread(path)

    img, counts = utlis.getContours(img, minArea=200,filter=4)

    if len(counts) != 0:
        biggest = counts[0][2]
        #print(biggest)
        imgWarp = utlis.warpImg(img,biggest,wP,hP)

    cv2.imshow("Original",img)
    cv2.imshow("WARP", imgWarp)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()