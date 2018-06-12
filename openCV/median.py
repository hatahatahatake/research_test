#-*- coding:utf-8 -*-
# メディアンフィルタ
import cv2
import numpy as np

def main():
    # 入力画像をグレースケールで読み込み
    #gray = cv2.imread("shun.jpg", 0)

    img = cv2.imread("shun.jpg")

    # 方法3(OpenCVで実装)
    #dst3 = cv2.blur(gray, ksize=(3,3))

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 方法3
    dst3 = cv2.GaussianBlur(gray, ksize=(3,3), sigmaX=1.3)

    # 結果を出力
    cv2.imwrite("output_shun2.jpg", dst3)

if __name__ == "__main__":
    main()
