import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt

# dog 이미지 불러와서 히스토그램 출력하기
img = cv.imread("./img/dog.jpg")

h = cv.calcHist([img] , [1] , None, [256] , [0,256])
plt.plot(h, color='r' , linewidth=1)
plt.show()

# dog 이미지의 중앙 아래 부분, Upper Left 부분 이미지 출력하기
UpperLeft_img = img[0:img.shape[0]//2 , 0:img.shape[1]//2]
BottomCenter_img = img[img.shape[0]//2: , img.shape[1]//4 : 3*img.shape[1]//4]

cv.imshow("Original Image" , img)
cv.imshow("Upper Left Image" , UpperLeft_img)
cv.imshow("Bottom Center Image" , BottomCenter_img)
cv.waitKey()
cv.destroyAllWindows()

# R,G,B 채널별로 이미지 띄우기
cv.imshow("Red Channel" , img[:,:,2])
cv.imshow("Green Channel" , img[:,:,1])
cv.imshow("Blue Channel" , img[:,:,0])
cv.waitKey()
cv.destroyAllWindows()