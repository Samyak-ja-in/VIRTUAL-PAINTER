#you can add more colour values easily by checking for hue saturation values for those colours refer paint_trainer for more info
import cv2 as cv
import numpy as np

colours=[[91,116,18,151,255,255,[255,0,0]],    #BLUE  #satmin,huemin,valuemin,satmax,huemax,valuemax,colourby whichpaint is to be done BGR
         [0,78,226,65,255,255,[255,255,0]],         #YELLOW #shv min-max
         [0,114,152,206,255,255,[0,0,255]],              #RED
         [22,55,105,57,170,240,[0,255,255]],     #YELLOW WALA PEN
         [136,195,102,196,255,206,[0,0,255]],       #Red cap of colgate
         [0,46,103,96,163,142,[0,255,255]]]         #yellow pencil


##################BLUE pen
# hue_min=116
# hue_max=255
# sat_min=91
# sat_max=151
# val_min=18
# val_max=255

####################3YELLOW mobile
# hue_min=78
# hue_max=255
# sat_min=0
# sat_max=65
# val_min=226
# val_max=255

# ######################RED MOBILE
# hue_min=114
# hue_max=255
# sat_min=0
# sat_max=206
# val_min=152
# val_max=255
global list
list=[]
def getcontours(img,data):
    global list
    contours,hierarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x=0
    y=0
    w=0
    for cont in contours:
        area=cv.contourArea(cont)
        if area>500:

            # cv.drawContours(img_result, cont, -1, (255,0,0),4)            #for drawing contours of blue colour if detected

            perimeter=cv.arcLength(cont, True)
            approx_vertex=cv.approxPolyDP(cont, 0.02*perimeter, True)
            x,y,w,h=cv.boundingRect(approx_vertex)
            cv.rectangle(img_result,(x,y),(x+w,y+h),(0,0,0),4)
            x=x+w//2 
            cv.circle(img_result, (x,y), 10, data,cv.FILLED)
            list.append([x,y,data])


def find_colour(img,colours):
    img_hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # cv.imshow("hsv image",img_hsv)                #hsv image hue-saturation-value
    for colour in colours:
        lower=np.array(colour[0:3])
        upper=np.array(colour[3:6])
        mask_img=cv.inRange(img_hsv, lower, upper)
        data=colour[6]

        draw(data)
        getcontours(mask_img,data)
        # cv.imshow("Masked image",mask_img)                #masked image



def draw(data):
    for value in list:
        if value[2]==data:
            cv.circle(img_result, (value[0],value[1]), 10, value[2],cv.FILLED)




vid=cv.VideoCapture(0)
vid.set(3,640)      #width
vid.set(4,480)      #height
vid.set(10,200)       #brightness
success=True
while success:
    success,img1=vid.read()
    img1=cv.flip(img1,1)                            #1 means flip horizontally and 0 means flip vertically
    img_result=img1.copy()

    # cv.imshow("SAMYAK PROJECT",img1)              #original webcam image
    
    find_colour(img1,colours)
    cv.imshow("contours image",img_result)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break


cv.imwrite("painted_image.png", img_result)             #painted image will be saved and overwrited 
