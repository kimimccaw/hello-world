import numpy as np
import cv2 as cv
import os

img = cv.imread("measure.png", 0)
img = cv.medianBlur(img, 5)
grayImg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

print(grayImg.shape)
cv.imshow("ori image", img)
cv.imshow("gray", grayImg)
cv.imwrite("grayscale.png", grayImg)
cv.waitKey(0)
cv.destroyAllWindows()
