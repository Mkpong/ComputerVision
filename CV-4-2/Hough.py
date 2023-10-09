import cv2 as cv
import sys

img = cv.imread("./img/apples.jpg")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

apples = cv.HoughCircles(gray, cv.HOUGH_GRADIENT , 1, 200, param1=150, param2=20, minRadius=50, maxRadius=120)

for apple in apples[0]:
    cv.circle(img, (int(apple[0]),int(apple[1])), int(apple[2]), (255, 0, 0) , 3)

cv.imshow("apple circle" , img)
cv.waitKey()
cv.destroyAllWindows()