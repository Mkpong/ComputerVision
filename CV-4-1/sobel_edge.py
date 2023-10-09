import cv2 as cv
import sys

img = cv.imread("./img/dog.jpg")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# sobel 적용
grad_x = cv.Sobel(gray , cv.CV_32F, 1,0, ksize=3)
grad_y = cv.Sobel(gray , cv.CV_32F, 0,1, ksize=3)

# 절댓값
sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)

edge_strength = cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0)

cv.imshow("Origianl" , gray)
cv.imshow("sobel x",sobel_x)
cv.imshow("sobel_y",sobel_y)
cv.imshow("Edge Strangtg", edge_strength)

cv.waitKey()
cv.destroyAllWindows()