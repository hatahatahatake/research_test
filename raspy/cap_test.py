# Webカメラ 画像取得コードのテスト
# OpenCV のインポート
import cv2
import glob
import os
import sys
from os import getpid
from os import kill
from threading import Timer
from time import sleep
from signal import SIGTERM

# VideoCaptureのインスタンスを作成する。
# 引数でカメラを選べれる。
# 0は内蔵カメラ、1は入力カメラ
cap = cv2.VideoCapture(1)
cap.set(4, 700)  # Width
cap.set(4, 500)  # Heigh
cap.set(5, 15)   # FPS

sys.path.append('Desktop/iMac-Desktop/git/research_test/raspy/images')

# ディレクトリパス指定
setnumber = "cap_img"
dir_path = u"./images"
#output_path = "C:Desktop/iMac-Desktop/git/research_test/raspy/images"
output_path = "./images"
output_name = output_path + '/' + setnumber

# ディレクトリ確認用(うまく行かなかった時用)
import os
print(os.path.exists(output_path))

i = 1;
while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    # 画像を取得
    cv2.imshow('Raw Frame', frame)

    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == ord('c'):

        # raspy/image ディレクトリに取得画像を保存
        cv2.imwrite(output_name + str(i) + ".png", frame)
        i += 1

    elif k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()
