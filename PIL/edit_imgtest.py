# coding:utf-8

# python 画像処理テスト
from PIL import Image
import numpy as np

# 元となる画像の読み込み
img = Image.open('img.jpg')
# オリジナル画像の幅と高さを取得
width, height = img.size
# オリジナル画像と同じサイズのImageオブジェクトを作成する
img2 = Image.new('RGB', (width, height))

# 画像ファイルの配列化
#img_pixels = []
#for y in range(height):
#    for x in range(width):
# getpixel((x,y))で左からx番目,上からy番目のピクセルの色を取得し、img_pixelsに追加する
#    img_pixels.append(img.getpixel((x,y)))
# 後で計算しやすいように numpy の array に変換しておく
#img_pixels = np.array(img_pixels)

# この一行でも書くことができる
img_pixels = np.array([[img.getpixel((i,j)) for j in range(height)] for i in range(width)])

# 各ピクセルの値の取得
img_pixels[100][200]

# ピクセルへの値のセット
img2.putpixel((100, 200), (0, 0, 255))

# インスタンスを表示
img2.show()

# インスタンスの保存
img2.save('edited_img.jpg')

