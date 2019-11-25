#!/usr/bin/env python
# coding: utf-8

# # 作業
# 
# 思考一下我們前面有提到圖片是矩陣，但維度可能會不一樣
# 例如灰階圖只有兩個維度，RGB 彩圖則有 3 個維度
# 
# 假如今天我們把 RGB 3 個維度拆開來看會有甚麼不同的效果呢？

# In[4]:


import cv2

img_path = 'images/ccat.jpg'

# 以彩色圖片的方式載入
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

b = img.copy()
b[:, :, 1] = 0
b[:, :, 2] = 0

g = img.copy()
g[:, :, 0] = 0
g[:, :, 2] = 0

r = img.copy()
r[:, :, 0] = 0
r[:, :, 1] = 0
# 為了要不斷顯示圖片，所以使用一個迴圈
while True:
    cv2.imshow('B-RGB', b)
    cv2.imshow('G-RGB', g)
    cv2.imshow('R-RGB', r)
    print("就是這樣的效果La")

    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break


# In[ ]:




