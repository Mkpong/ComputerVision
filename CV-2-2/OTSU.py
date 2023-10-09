import cv2 as cv
import sys

img = cv.imread("./img/dog.jpg")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다.")

# 이진화
# threshold -> (이미지(단일채널) , min, max, 이진화 방법)
t, bin_img = cv.threshold(img[:,:,2], 0,255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print("오츄 알고리즘이 찾은 최적의 임계값 : " , t)

# threshold
t, bin_img2 = cv.threshold(img[:,:,2] , 119.0, 255, cv.THRESH_BINARY)

cv.imshow("R channel original" , img[:,:,2])
cv.imshow("R channel binarization" , bin_img)
cv.imshow("R channel binarization2" , bin_img2)

cv.waitKey()
cv.destroyAllWindows()
