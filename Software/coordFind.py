##########
#Image Processing & Coordinates Extraction
##########

import numpy as np
import cv2 
import imutils 

##DEFINING LIMITS##

#RED color Limits
lower_red = np.array([0,100,0])
upper_red = np.array([15,255,255])

#Green color Limits
lower_green = np.array([45,100,0])
upper_green = np.array([75,255,255])

#Yellow color Limits.
lower_yellow = np.array([20,100,0])
upper_yellow = np.array([30,255,255])


def colorFilter(imageName,lowerLimits,upperLimits):
    hsv = cv2.cvtColor(imageName, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerLimits, upperLimits)
    res = cv2.bitwise_and(imageName,imageName, mask = mask)
    return res

def centers(imageFiltered):
    #array of centers
    coords = np.zeros((5,2))
    #Prepare image for defining the center of contours in it
    grayimg = cv2.cvtColor(imageFiltered, cv2.COLOR_BGR2GRAY)
    blurredimg = cv2.GaussianBlur(grayimg, (5, 5), 0)
    threshimg = cv2.threshold(blurredimg, 0, 255, cv2.THRESH_BINARY)[1]
    #extract contours from image
    cnts = cv2.findContours(threshimg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # loop over the contours
    i=0
    for c in cnts:
        if(i <= (coords.shape[0])):
            # compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draw the contour and center of the shape on the image
            cv2.drawContours(imageFiltered, [c], -1, (0, 255, 0), 2)
            cv2.circle(imageFiltered, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(imageFiltered, "center", (cX - 20, cY - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            #save coordinates of centers
            coords[i,0] = cX
            coords[i,1] = cY
            i+=1
    return coords


##FOR TESTING##

#img = cv2.imread('sample.jpg',1)

#imgRed = colorFilter(img,lower_red,upper_red)
#imgYellow = colorFilter(img,lower_yellow,upper_yellow)
#imgGreen = colorFilter(img,lower_green,upper_green)

#cr = centers(imgRed)
#cy = centers(imgYellow)
#cg = centers(imgGreen)

#cv2.imshow('img',img)
#cv2.imshow('imgRed',imgRed)
#cv2.imshow('imgYellow',imgYellow)
#cv2.imshow('imgGreen',imgGreen)
#cv2.imshow('threshRed', threshRed)

#cv2.imwrite('imgRed.png',imgRed)
#cv2.imwrite('imgYellow.png',imgYellow)
#cv2.imwrite('imgGreen.png',imgGreen)

#cv2.waitKey(0)
#cv2.destroyAllWindows()