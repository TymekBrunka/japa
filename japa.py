"""
Japa (rozpoznawanie twarzy z kamery)
"""

import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1024)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 10)

while True:
    success, img = cap.read()
    # img = cap.flip(img, 1)
    cv2.imshow("Kamerka", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
