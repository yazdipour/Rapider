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
import pytesseract
print(pytesseract.image_to_string(Image.open('zz.jpg')))
# scrn = numpy.array(ImageGrab.grab().convert('RGB')) 
# scrn = scrn[:, :, ::-1].copy() 
# scrn=scrn[y:y+h, x:x+w]
# img = scrn[:,:,2]

# img = Image.fromarray(img)
# txt = pytesseract.image_to_string(img, config='digits')

# img = cv2.equalizeHist(img)
# x,y,w,h=0,0,len(img[0])/7,len(img)/10
# img2=img.copy()
# toClick=[]
# for i in range(0,7):
#     for j in range(0,10):
#         x,y=i*w,j*h
#         subimg=img[y+10:y+h-10,x+10:x+w-10]
#         n=pytesseract.image_to_string(scrn, config='digits')
#         cv2.putText(scrn,n,(min_loc[0]+x,min_loc[1]+y), cv2.FONT_HERSHEY_SIMPLEX,.5,(255,0,0),1,cv2.LINE_AA)

# for item in toClick:
#     robot.sleep(.5)
#     robot.move_and_click(item[0]+first[0],first[1]+item[1],button='left')
cv2.imshow('',img2)
cv2.waitKey(0)