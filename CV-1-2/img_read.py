import cv2 as cv
import sys

img = cv.imread("./CV-1-2/dog.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다")

# 이미지 띄우기
cv.imshow("Image" , img)
cv.waitKey()
cv.destroyAllWindows()

# RGB -> GRAY 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 반으로 축소
gray_small = cv.resize(gray, dsize=(0,0) ,fx=0.5, fy=0.5)

# 이미지의 사이즈 출력
print("gray size : " , gray.shape)
print("gray_samll size : " , gray_small.shape)

# gray, gray_small 파일 저장
cv.imwrite("./CV-1-2/gray.jpg" , gray)
cv.imwrite("./CV-1-2/gray_small.jpg" , gray_small)

# 화면 띄우기
cv.imshow("gray image" , gray)
cv.imshow("gray_small image" , gray_small)
cv.waitKey()
cv.destroyAllWindows()

