import numpy as np
import cv2 as cv
import os



#parameter jenis: 0 for grayscale ; 1 for color

def measure(rgbWhite,rgbBlack,path):
    filename = 'measure.png'
    width = 0 
    pipePixelSize = 0
    greencolor = [0,255,0]
    whiteColor = 0
    blackColor = 0

    join_image = os.path.join(path, filename)
    
    img = cv.imread(join_image,0)
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
    textPipeSize = "Pipe pixel size : " , pipePixelSize
    print(textPipeSize)
    textPipePercent = "pipe size percent: " , ((pipePixelSize)/imageSize)*100
    print(textPipePercent)
    textWhitePercent = "white percent: " , ((whiteColor)/pipePixelSize)*100
    print(textWhitePercent)
    textBlackPercent = "Black percent: " , ((blackColor)/(pipePixelSize-whiteColor))*100
    print(textBlackPercent)

    cv.imshow("median circles", img)
    cv.imshow('detected circles',cimg)
    join_result_cimg = os.path.join(path, "result.png")
    join_result_img = os.path.join(path, "result_img.png")
    cv.imwrite(join_result_cimg , cimg)
    cv.imwrite(join_result_img, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    join_txt = os.path.join(path, "Result.txt")
    outF = open(join_txt , "w")
    outF.writelines(str(textPipePercent))
    outF.writelines(str(textPipeSize))
    outF.writelines(str(textWhitePercent))
    outF.writelines(str(textBlackPercent))
    outF.close()


rgbWhite = [255,255,255] 
rgbBlack = [116,116,116]



cwd = os.getcwd()
for name in os.listdir("."):
    if os.path.isdir(name):
        laluan = os.path.abspath(name)
        #laluan = "C:/Users/Kimimccaw/Desktop/Data/Hough_transform/Data"
        print(laluan)
        measure(rgbWhite, rgbBlack, laluan)