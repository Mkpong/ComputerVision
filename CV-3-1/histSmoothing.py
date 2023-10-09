import cv2 as cv
import matplotlib.pyplot as plt
import sys

img = cv.imread("./img/mistyroad.jpg")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

h = cv.calcHist([gray] , [0] , None, [256] , [0,256])
plt.plot(h , color='r' , linewidth=1)
plt.show()

equal = cv.equalizeHist(gray)
plt.imshow(equal , cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

h_equal = cv.calcHist([equal] , [0] , None, [256] , [0,256])
plt.plot(h_equal , color='r' , linewidth= 1)
plt.show()