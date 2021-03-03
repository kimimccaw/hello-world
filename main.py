import cv2
import numpy as np

img = cv2.imread('baru.png')
#cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cimg2 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
kira = 0

nomb = 0


for i in img:
    if kira < 50:
        kira += 1
        for j in i:
            print(j)
    else:
        break

print(cv2.minMaxLoc(img))

print(img.shape)
print(nomb)
cv2.imshow("gambar", img)
#cv2.imshow("gambar2", cimg2)

cv2.waitKey(0)
cv2.destroyAllWindows()
