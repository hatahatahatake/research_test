import cv2
import numpy as np

im = cv2.imread('yel.png')

hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
lower_yel = np.array([20, 30, 50])
upper_yel = np.array([60, 255, 255])
img_mask = cv2.inRange(hsv, lower_yel, upper_yel)
img_color = cv2.bitwise_and(im, im, mask=img_mask)

imgray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
imgEdge,contours,hierarchy = cv2.findContours(thresh, 1, 2)

imga = cv2.drawContours(im, contours, -1, (0,255,0), -1)

#cv2.imshow("SHOW gray IMAGE", imgray)
#cv2.imshow("SHOW COLOR IMAGE", img_color)
cv2.imshow('espilon',imga)
cv2.waitKey()
cv2.destoroyAllWindows()
