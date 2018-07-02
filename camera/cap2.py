import cv2


# カメラからキャプチャー

# 0は内蔵カメラ、1は入力カメラ
cap = cv2.VideoCapture(1)
cap.set(4, 700)  # Width
cap.set(4, 500)  # Heigh
cap.set(5, 15)   # FPS

i = 1;
while(True):

    # 動画ストリームからフレームを取得
    ret, frame = cap.read()

     # 表示
    cv2.imshow("Show FLAME Image", frame)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # qを押したら終了。
    k = cv2.waitKey(1)
    if k == ord('c'):
        #setnumber="test"
        setnumber="Even_Dataset"
        cv2.imwrite(setnumber+str(i)+".png",frame)
        # cv2.imwrite(setnumber+str(i+1)+".png",frame)
        # cv2.imwrite(setnumber+str(i+2)+".png",frame)
        # cv2.imwrite(setnumber+str(i+3)+".png",frame)#4枚画像取得
        # i = i + 4
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
