import cv2 as cv
import sys

img = cv.imread("./img/dog.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

# 이미지의 특정 부위만 표시
# OpenCV는 (y,x)로 좌표를 표시한다 -> 기본적으로
cv.imshow("Original Image" , img)
cv.imshow("Upper left half Image" , img[0:img.shape[0]//2 , 0:img.shape[1]//2])
cv.imshow("test" , img[0:img.shape[0]//2 , img.shape[1]//4:3*img.shape[1]//4])

cv.waitKey()
cv.destroyAllWindows()

# 이미지 채널별로 Display
# OpenCV는 기본적으로 BGR 이미지를 지원한다.
cv.imshow("Red Channel Image" , img[:,:,2])
cv.imshow("Green Channel Image" , img[:,:,1])
cv.imshow("Blue Channel Image" , img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()