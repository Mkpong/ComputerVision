import cv2 as cv
import matplotlib.pyplot as plt
import sys

img = cv.imread("./img/dog.jpg")

if img is None:
    sys.exit("이미지를 찾을 수 없습니다.")

h = cv.calcHist([img], [1] , None, [256] , [0,256])
plt.plot(h, color="r" , linewidth=1)
plt.show()