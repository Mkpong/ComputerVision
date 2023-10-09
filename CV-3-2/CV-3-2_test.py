import cv2 as cv
import numpy as np
import sys

# rose 이미지 불러오기
img = cv.imread("./img/rose.png")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")

# patch = 이미지 자르기 (170,250) , (270,350)
patch = img[250:350, 170:270 , :]

# 원본 이미지에 사각형 그리기
img = cv.rectangle(img, (170,250) , (270,350) , (255,0,0) , 3)

# NEAREST 보간
patch1 = cv.resize(patch, dsize=(0,0) , fx=5, fy=5 , interpolation=cv.INTER_NEAREST)

# 선형 보간
patch2 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)

# 큐빅 보간
patch3 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)

#이미지 하나로 합체
total = np.hstack((patch1, patch2, patch3))

#출력
cv.imshow("Original" , img)
cv.imshow("Total" , total)
cv.waitKey()
cv.destroyAllWindows()