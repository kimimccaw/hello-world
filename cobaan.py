import cv2
import numpy as np


img = cv2.imread("baru.png")


###convert to specific range of color

# define range of blue color

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

upper_red = np.array([216,87,25])
uper_red = np.uint8([[[216,87,25]]])
lower_blue = np.array([240,0,0])
low_blue = np.uint8([[[240,0,0]]])

hsv_red = cv2.cvtColor(uper_red, cv2.COLOR_BGR2HSV)
hsv_blue = cv2.cvtColor(low_blue, cv2.COLOR_BGR2HSV)

#treshold the hsv image to get only blue colors

mask = cv2.inRange(hsv, hsv_blue, hsv_red)

cv2.imshow('mask',mask)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()





