import cv2 as cv
import numpy as np

img = cv.imread("./img/dog.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray,100,200)

# 경계선 검출
contours , hierarchy = cv.findContours(canny, cv.RETR_LIST , cv.CHAIN_APPROX_NONE)

lcontours = []

# 길이가 100 이상인 경계선 추출
for contour in contours:
    if contour.shape[0] > 100:
        lcontours.append(contour)



cv.drawContours(img, lcontours , -1, (0,255,0) , 3)

cv.imshow("Origianl with contour" , img)
cv.imshow("Canny" , canny)

cv.waitKey()
cv.destroyAllWindows()