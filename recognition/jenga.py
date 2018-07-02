import cv2
import numpy as np
import time

cap = cv2.VideoCapture(1)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Heigh
cap.set(5, 15)   # FPS


if cap.isOpened() is False:
    raise("IO Error")

cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    # フレームを取得
ret, frame = cap.read()

    # フレームをHSVに変換
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower = np.array([20, 30, 100])
upper = np.array([57, 99, 255])
img_mask = cv2.inRange(hsv, lower, upper)
img_color = cv2.bitwise_and(frame, frame, mask=img_mask)

imgray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
imgEdge,contours,hierarchy = cv2.findContours(thresh, 1, 2)

imga = cv2.drawContours(frame, contours, -1, (0,255,0), -1)

cv2.imwrite("jenga.png",imga)


cap.release()
cv2.destroyAllWindows()
