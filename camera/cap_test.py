# Webカメラ 画像取得コードのテスト
# OpenCV のインポート
import cv2

# VideoCaptureのインスタンスを作成する。
# 引数でカメラを選べれる。
# 0は内蔵カメラ、1は入力カメラ
cap = cv2.VideoCapture(1)
cap.set(4, 700)  # Width
cap.set(4, 500)  # Heigh
cap.set(5, 15)   # FPS

while True:
    # VideoCaptureから1フレーム読み込む → このままでは動画になる
    ret, frame = cap.read()

    cv2.imshow('Raw Frame', frame)

    cv2.imwrite("test.png", frame)

    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()
