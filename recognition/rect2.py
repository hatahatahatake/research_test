import cv2
import numpy as np
import time


def getRectByPoints(points):
    # prepare simple array
    points = list(map(lambda x: x[0], points))

    points = sorted(points, key=lambda x:x[1])
    top_points = sorted(points[:2], key=lambda x:x[0])
    bottom_points = sorted(points[2:4], key=lambda x:x[0])
    points = top_points + bottom_points

    left = min(points[0][0], points[2][0])
    right = max(points[1][0], points[3][0])
    top = min(points[0][1], points[1][1])
    bottom = max(points[2][1], points[3][1])
    return (top, bottom, left, right)

def getPartImageByRect(rect):
    img = im
    return img[rect[0]:rect[1], rect[2]:rect[3]]

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    cap.set(3, 640)  # Width
    cap.set(4, 480)  # Heigh
    #cap.set(5, 15)   # FPS
    while(1):
        ret, im = cap.read()
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im_blur = cv2.GaussianBlur(im_gray, (11, 11), 0)

        ret1, th1 = cv2.threshold(im_blur, 127, 255, cv2.THRESH_BINARY_INV)
        th2 = cv2.adaptiveThreshold(im_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)

        contours = cv2.findContours(th2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]

        # filtered with area over (all area / 100 )
        th_area = im.shape[0] * im.shape[1] / 100
        contours_large = list(filter(lambda c:cv2.contourArea(c) > th_area, contours))

        outputs = []
        rects = []
        approxes = []

        for (i,cnt) in enumerate(contours_large):
            arclen = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*arclen, True)
            if len(approx) < 4:
                continue
            approxes.append(approx)
            rect = getRectByPoints(approx)
            rects.append(rect)
            outputs.append(getPartImageByRect(rect))
            #cv2.imwrite('./out/output'+str(i)+'.jpg', getPartImageByRect(rect))

        # 画像表示
        recter = cv2.bitwise_and(im, im, mask = th2)
        #imga = cv2.drawContours(im, contours, -1, (0,255,0), -1)
        cv2.imshow('rect',recter)
            # qを押したら終了
        k = cv2.waitKey(1)
        if k == ord('q'):
            break


        # 何かキーを押したら終了
    cap.release()
    cv2.destroyAllWindows()
