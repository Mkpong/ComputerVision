import cv2 as cv
import numpy as np
import sys
import matplotlib.pyplot as plt

# 감마함수 정의
def gamma(f, gamma=1.0):
    f1 = f/255.0
    return np.uint8(255*(f1**gamma))

# 이미지 불러오기 dog
img1 = cv.imread('./img/dog.jpg')

if img1 is None:
    sys.exit("이미지를 불러올 수 없습니다")

# 감마 함수를 적용시킨 값을 이어 붙여 하나의 이미지로 출력 -> 0.5 0.75 1.0 2.0 4.0
gc = np.hstack((gamma(img1 , 0.5) , gamma(img1, 0.75) , gamma(img1 , 1.0) , gamma(img1, 2.0) , gamma(img1 , 4.0)))
plt.imshow(gc , cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 히스토그램 평활화
# mistyroad 이미지 불러와서 히스토그램 출력
img2 = cv.imread("./img/mistyroad.jpg")

if img2 is None:
    sys.exit("이미지를 불러올 수 없습니다")

gray = cv.cvtColor(img2 , cv.COLOR_BGR2GRAY)

h = cv.calcHist([gray] , [0] , None, [256] , [0,256])
plt.plot(h , color='r' , linewidth=1)
plt.show()

# 히스토그램 평활화 작업 이후 히스토그램 다시 출력
equal_gray = cv.equalizeHist(gray)
equal_h = cv.calcHist([equal_gray] , [0] , None, [256] , [0,256])
plt.plot(equal_h , color='r' , linewidth=1)
plt.show()

# 평활화된 이미지의 전후를 붙여서 출력
new_img = np.hstack((gray, equal_gray))
cv.imshow("IMAGE" , new_img)
cv.waitKey()
cv.destroyAllWindows()

