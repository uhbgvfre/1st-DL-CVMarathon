import cv2

img_path = 'images/lena.png'

oImg = cv2.imread(img_path, cv2.IMREAD_COLOR)

ImgGRAY = cv2.cvtColor(oImg, cv2.COLOR_BGR2GRAY)
ImgHLS = cv2.cvtColor(oImg, cv2.COLOR_BGR2HLS)
ImgHSV = cv2.cvtColor(oImg, cv2.COLOR_BGR2HSV)
ImgLAB = cv2.cvtColor(oImg, cv2.COLOR_BGR2LAB)

while True:
    cv2.imshow('o', oImg)
    cv2.imshow('ImgGRAY', ImgGRAY)
    cv2.imshow('ImgHLS', ImgHLS)
    cv2.imshow('ImgHSV', ImgHSV)
    cv2.imshow('ImgLAB', ImgLAB)
    print("就是這樣的效果Ha")

    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
