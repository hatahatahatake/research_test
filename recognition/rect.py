import cv2
import numpy as np
import time

if __name__ == '__main__':
    im = cv2.imread('test21.png')
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #(B)グレイスケール
    im_blur = cv2.GaussianBlur(im_gray, (11, 11), 0) #(C)ガウシアンブレラ
    #二値化処理
    #ret1, th1 = cv2.threshold(im_blur, 127, 255, cv2.THRESH_BINARY_INV)
    #閾値をとる範囲：単純に範囲内のピクセルの平均を取る cv2.ADAPTIVE_THRESH_MEAN_C と、ガウシアンの重みをつけて平均を取る cv2.ADAPTIVE_THRESH_GAUSSIAN_Cで輪郭を取得
    th2 = cv2.adaptiveThreshold(im_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)
    image, contours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # 画像表示
    recter = cv2.drawContours(im, contours, -1, (0,255,0), 3)

    cv2.imwrite('gray.png', im_gray)
    cv2.imwrite('blur.png', im_blur)
    cv2.imwrite('binary.png', th2)
    cv2.imshow('img',recter)
    cv2.imwrite('edge.png', recter)


    # 何かキーを押したら終了
    cv2.waitKey(0)
    cv2.destroyAllWindows()
