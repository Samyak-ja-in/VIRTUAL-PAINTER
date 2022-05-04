import cv2 as cv
import numpy as np
import concat

def empty(a):
    pass

def vhconcat(list_2d):
    final=cv.vconcat([cv.hconcat(img) for img in list_2d])
    return final


# img_original=cv.imread("IMAGES/lambo.png")
# img_original=cv.imread("IMAGES/SAMYAK RESIZED.jpg")


# img_hsv=cv.cvtColor(img_original,cv.COLOR_BGR2HSV)
# cv.imshow("ORIGINAL",img_original)
# cv.imshow("HSV",img_hsv)
# print(img_original.shape)
# print(img_hsv.shape)


img=np.zeros((462,623,3),np.uint8)
cv.namedWindow("TRACKBAR")
cv.resizeWindow("TRACKBAR", 623, 462)

cv.createTrackbar("sat_min", "TRACKBAR",0,255, empty)
cv.createTrackbar("sat_max", "TRACKBAR",255,255, empty)
cv.createTrackbar("hue_min", "TRACKBAR",0,255, empty)
cv.createTrackbar("hue_max", "TRACKBAR",255,255, empty)
cv.createTrackbar("val_min", "TRACKBAR",0,255, empty)
cv.createTrackbar("val_max", "TRACKBAR",255,255, empty)
cv.imshow("TRACKBAR",img)

vid=cv.VideoCapture(0)
while(1):
    # img_original=cv.imread("IMAGES/lambo.png")

    # img_hsv=cv.cvtColor(img_original,cv.COLOR_BGR2HSV)
    success,img_original=vid.read()
    img_original=cv.flip(img_original, 1) 
    img_hsv=cv.cvtColor(img_original,cv.COLOR_BGR2HSV)
    satmin=cv.getTrackbarPos("sat_min", "TRACKBAR")
    satmax=cv.getTrackbarPos("sat_max", "TRACKBAR")
    huemin=cv.getTrackbarPos("hue_min", "TRACKBAR")
    huemax=cv.getTrackbarPos("hue_max", "TRACKBAR")
    valmin=cv.getTrackbarPos("val_min", "TRACKBAR")
    valmax=cv.getTrackbarPos("val_max", "TRACKBAR")

    lower=np.array([satmin,huemin,valmin])
    upper=np.array([satmax,huemax,valmax])
    

    mask=cv.inRange(img_hsv,lower,upper)
    image_result=cv.bitwise_and(img_original,img_original,mask=mask )
    # cv.imshow("ORIGINAL",img_original)
    # cv.imshow("HSV",img_hsv)
    # cv.imshow("MASK",mask)
    # cv.imshow("FINAL IMAGE",image_result)
    # print(img_original.shape,img_hsv.shape,img.shape,image_result.shape)
    concata=concat.stackImages(1,[[img_original,img_hsv],[mask,image_result]])
    cv.imshow("FINAL concatenated IMAGE",concata)
    if cv.waitKey(1) & 0xFF==ord("q"):
        break