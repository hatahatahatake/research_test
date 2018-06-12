#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    # 入力画像をグレースケールで読み込み
    gray = cv2.imread("shun.jpg", 0)

    # 方法3(OpenCVで実装)
    dst3 = cv2.blur(gray, ksize=(3,3))

    # 結果を出力
    cv2.imwrite("output_shun.jpg", dst3)

if __name__ == "__main__":
    main()
