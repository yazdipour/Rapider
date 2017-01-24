from PIL import Image,ImageGrab
import cv2
import numpy
from pyrobot import Robot, Keys
import pytesseract
first=[460,126]
last=[905,758]
x,y=first[0],first[1]
w,h=last[0]-first[0],last[1]-first[1]
robot = Robot()
robot.sleep(3)
scrn = numpy.array(ImageGrab.grab().convert('RGB')) 
scrn = scrn[:, :, ::-1].copy() 
scrn=scrn[y:y+h, x:x+w]
img = scrn[:,:,2]
x,y,w,h=0,0,len(img[0])/7,len(img)/10 #pieces
positionToClick=[]

ocr=pytesseract.image_to_string(img)
cv2.putText(scrn,ocr,max_loc, cv2.FONT_HERSHEY_SIMPLEX,.5,(255,0,0),1,cv2.LINE_AA)

# for i in range(1,71):
#     positionToClick.append(max_loc)
#     cv2.putText(scrn,str(i),max_loc, cv2.FONT_HERSHEY_SIMPLEX,.5,(255,0,0),1,cv2.LINE_AA)

cv2.imshow('',img)
cv2.imshow('',scrn)
cv2.waitKey(0)