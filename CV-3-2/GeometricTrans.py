import cv2 as cv
import sys

img = cv.imread("./img/rose.png")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")

patch = img[250:350, 170:270 , :]

img = cv.rectangle(img, (170,250) , (270, 350) , (255,0,0) , 3)
patch1 = cv.resize(patch , dsize=(0,0) , fx=5 , fy=5 , interpolation=cv.INTER_NEAREST)
patch2 = cv.resize(patch , dsize=(0,0) , fx=5 , fy=5 , interpolation=cv.INTER_LINEAR)
patch3 = cv.resize(patch , dsize=(0,0) , fx=5, fy=5 , interpolation=cv.INTER_CUBIC)

cv.imshow("Original Image" , img)
cv.imshow("NEAREST" , patch1)
cv.imshow("LINER" , patch2)
cv.imshow("CUBIC" , patch3)

cv.waitKey()
cv.destroyAllWindows()