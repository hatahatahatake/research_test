import cv2

# 画像ファイルの読み込み
img = cv2.imread('houses.jpg')

#AgastFeatureDetector_create
#detector = cv2.AgastFeatureDetector_create()

# FAST
#detector = cv2.FastFeatureDetector_create()

# BRISK
#detector = cv2.BRISK_create()

# KAZE
#detector = cv2.KAZE_create()

# AKAZE
#detector = cv2.AKAZE_create()

# SimpleBlobDetector
#detector = cv2.SimpleBlobDetector_create()

# SIFT
#detector = cv2.xfeatures2d.SIFT_create()#opencv3はオプションで設定しないといけないみたい

# ORB (Oriented FAST and Rotated BRIEF)
detector = cv2.ORB_create()

# 特徴検出
keypoints = detector.detect(img)

# 画像への特徴点の書き込み
out = cv2.drawKeypoints(img, keypoints, None)

# 表示
cv2.imshow("keypoints", out)
cv2.waitKey()
cv2.destoroyAllWindows()
