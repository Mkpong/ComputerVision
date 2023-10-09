import cv2 as cv
import sys

img = cv.imread("./img/dog.jpg")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

canny1 = cv.Canny(gray, 50, 150)
canny2 = cv.Canny(gray, 100, 200)

cv.imshow("Original" , gray)
cv.imshow("Canny1" , canny1)
cv.imshow("Canny2" , canny2)

cv.waitKey()
cv.destroyAllWindows()