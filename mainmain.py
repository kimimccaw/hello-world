import numpy as np
import cv2 as cv
img = cv.imread('baru.png',0)
cv.imshow("original image", img)
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,400,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
print(circles)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

###calculating the number of pixels



width = 0 
pipePixelSize = 0
greencolor = [0,255,0]
whiteColor = 0
blackColor = 0
jenis = input("What kind of File 0 or 1 :")

if jenis == str(0):
    rgbWhite = [255,255,255] 
    rgbBlack = [24,24,24]
elif jenis == str(1):
    rgbWhite = [240,240,240]
    rgbBlack = [84,84,84]



start = False

for i in cimg:
    width +=1
    for j in i:
        k = 0
        #while k < 5:
        #    k+=1
        #    print(j)         
        if (j == greencolor).all() and not start:
            #print(j)
            inside = True
            #pipePixelSize +=1
            start = True
        elif not (j == greencolor).all() and start:
            inside = False
            pipePixelSize += 1
            if (j==rgbWhite).all():
                whiteColor +=1
            elif (j==rgbBlack).all():
                blackColor +=1
        elif (j == greencolor).all() and start:
            start = False
        

imageSize = img.shape[0]*img.shape[1]
print("Image Size :" , imageSize)
print("Image dimensions :" , img.shape)
print("CImage dimensions :" , cimg.shape)

print(width)
print("Pipe pixel size : ", pipePixelSize)
print("pipe size percent: " , ((pipePixelSize)/imageSize)*100)
print("white percent: " , ((whiteColor)/pipePixelSize)*100)
print("Black percent: " , ((blackColor)/(pipePixelSize-whiteColor))*100)

cv.imshow("median circles", img)
cv.imshow('detected circles',cimg)
cv.imwrite('baruabarua.png', img)
cv.waitKey(0)
cv.destroyAllWindows()
