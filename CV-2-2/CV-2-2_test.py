import cv2 as cv
import sys
import matplotlib.pyplot as plt
import numpy as np

# 원본대로 이미지를 불러오기
img = cv.imread("./img/JohnHancocksSignature.png" ,cv.IMREAD_UNCHANGED)

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")

# 오츄 알고리즘을 적용시켜 이진화 진행
t , bin_img = cv.threshold(img[:,:,3] , 0, 255 , cv.THRESH_BINARY+cv.THRESH_OTSU)
print("오츄 알고리즘이 결정한 최적의 임계값 : " , t)

plt.imshow(bin_img , cmap='gray')
plt.xticks([])
plt.xticks([])
plt.show()

# 구조 정의
se = np.uint8([
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,1,1,1,0],
    [0,0,1,0,0]
])

# 팽창 연산
dilate_img = cv.dilate(bin_img , se, iterations=1)
plt.imshow(dilate_img , cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 침식 연산
erode_img = cv.erode(bin_img , se , iterations=1)
plt.imshow(erode_img , cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 닫힘 연산
close_img = cv.erode(cv.dilate(bin_img , se , iterations=1) , se , iterations=1)

# 열림 연산
open_img = cv.dilate(cv.erode(bin_img , se, iterations=1) , se, iterations=1)

