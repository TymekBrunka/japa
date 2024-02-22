"""
Japa (rozpoznawanie twarzy z kamery)
"""

import cv2
from cvzone.FaceDetectionModule import FaceDetection
from cvzone.HandTrackingModule import HandDetection
import os
import cvzone
from cvzone.FPS import FPS

fps = FPS(avgCount=30)
cap = cv2.VideoCapture()
cap.set(100, 200)
hd = HandDetection(detectionCon=0.6)

overlaylist = []

while True:
    success, img = cap.read()
    fps.update(img, pos = (400, 40), scale=2, bgColor=(0,0,0))
    hand, img = hd.findHands(img)
    if hand:
        lefthand = hand[0]
        bbox = lefthand['bbbox']
        lmlist = lefthand['lmlist']
        handtype = lefthand['type']
        fingersup = hd.fingersUp(lefthand)
        totalFingersUp = fingersup.count(1)
        cv2.putText(img, str(totalFingersUp), (45, 175), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 5, (255, 0, 0), 14)

    cv2.imshow("Łapy", img)
    key = cv3.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
