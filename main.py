import cv2
import numpy as np
import coordFind as cf
import uArmKinematics as kin
import serial
import time

###CODE STRATEGY###
#-----------------#
#Start robot and home it:
ArduinoSerial = serial.Serial('com9',9600) #creat serial port called ArduinoSerial

time.sleep(2) #wait for 2 seconds for the communication to get established

ArduinoSerial.write(kin.PHome.encode('utf-8')) #Homing the Robotic Arm


#Start webcam and take a picture of working area
cap = cv2.VideoCapture(1) #use an external webcam (mounted on robotic arm)

while True:
    ret, frame = cap.read()
    
#process image and extract coordinates of objects and colors
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
    
    imgRed = cf.colorFilter(frame,lower_red,upper_red)
    imgYellow = cf.colorFilter(frame,lower_yellow,upper_yellow)
    imgGreen = cf.colorFilter(frame,lower_green,upper_green)
    
    cr = cf.centers(imgRed) #coordinates of RED objects centers
    cy = cf.centers(imgYellow) #coordinates of YELLOW objects centers
    cg = cf.centers(imgGreen) #coordinates of GREEN objects centers
    
#flag processing complete and wait for order to execute sorting sequence
#pass coordinates to robot and organize motion sequence
#start executing the sequence
#finish sequence then go home and repeat
##if no objects detected (HALT)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
###EOC###