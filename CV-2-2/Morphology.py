import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

img = cv.imread("./CV-1-2/dog.jpg")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다")
    

