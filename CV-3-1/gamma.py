import cv2 as cv
import numpy as np
import sys

img = cv.imread("./img/dog.jpg")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")

img = cv.resize(img, dsize=(0,0) , fx = 0.5, fy = 0.5)

def gamma(f, gamma=1.0):
    f1 = f/255.0
    return np.uint8(255*(f1**gamma))

gc = np.hstack((gamma(img, 0.5), gamma(img, 0.75) , gamma(img, 1.0) , gamma(img, 2.0) , gamma(img , 3.0)))

cv.imshow("gamma image" , gc)
cv.waitKey()
cv.destroyAllWindows()