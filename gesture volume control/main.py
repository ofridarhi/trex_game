import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import pycaw
from ctypes import cast, POINTER
from  comtypes import  CLSCTX_ALL
from  pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def angle(c,b,a):
    angle = math.acos((c ** 2 - b ** 2 - a ** 2) / (-2 * a * b))
    return angle


def detectRSP():
    wCam, hCam = 640, 480

    cam = cv2.VideoCapture(0)
    cam.set(3, wCam)
    cam.set(4, hCam)

    detector = htm.handDetector(detectionCon=0.7)

    while True:
        check, img = cam.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img, draw=False)
        if len(lmlist) != 0:
            #print(lmlist)
            dx08,dy08 = lmlist[8][1] - lmlist[0][1],lmlist[0][2] - lmlist[8][2]
            d08 = math.sqrt(abs(dx08**2 + dy08**2))

            dx012,dy012 = lmlist[0][1] - lmlist[12][1] ,lmlist[0][2] - lmlist[12][2]
            d012 = math.sqrt(abs(dx012**2 + dy012**2))

            dx812,dy812 = lmlist[8][1] - lmlist[12][1] ,lmlist[8][2] - lmlist[12][2]
            d812 = math.sqrt(abs(dx812**2 + dy812**2))

            dx418,dy418 = lmlist[4][1] - lmlist[19][1],lmlist[4][2] - lmlist[19][2]
            d418 = math.sqrt(abs(dx418**2 + dy418**2))

            dx415,dy415 = lmlist[4][1] - lmlist [15][1], lmlist[4][2] - lmlist [15][2]
            d415 = math.sqrt(abs(dx415**2 + dy415**2))

            #print(d418**2)
            print(math.acos((d812**2-d012**2-d08**2)/(-2 * d012 * d08)))
            #if 0.25 < angle(d812,dx012,d08) < 0.40:
                #print("finger")


        cv2.imshow('name', img)
        cv2.waitKey(1)

detectRSP()