import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

# 원본 채널 수대로 불러옴
img = cv.imread("./CV-2-2/JohnHancocksSignature.png" , cv.IMREAD_UNCHANGED)

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")
    
t , bin_img = cv.threshold(img[:,:,3] , 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# cv.imshow("imagebin_img)
# cv.waitKey()
# cv.destroyAllWindows()

plt.imshow(bin_img, cmap='gray') # grayscale img로 표현
plt.xticks([]) # x축 눈금 없음
plt.yticks([]) # y축 눈금 없음
plt.show()

b = bin_img[bin_img.shape[0]//2:bin_img.shape[0], 0:bin_img.shape[1]//2 + 1]
plt.imshow(b , cmap="gray")
plt.xticks([])
plt.yticks([])
plt.show()

# 구조요소 생성
se = np.uint8([
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,1,1,1,0],
    [0,0,1,0,0]
])

# 팽창
b_dilation=cv.dilate(b, se, iterations=1)
plt.imshow(b_dilation, cmap="gray")
plt.xticks([])
plt.yticks([])
plt.show()

# 침식
b_erosion = cv.erode(b, se, iterations=1)
plt.imshow(b_erosion , cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 닫기(팽창 후 침식)
b_closing = cv.erode(cv.dilate(b, se, iterations=1) , se, iterations=1)
plt.imshow(b_closing, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 열림(침식 후 팽창)
b_opening = cv.dilate(cv.erode(b, se , iterations =1) , se , iterations=1)
plt.imshow(b_opening, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()