from PIL import ImageGrab
import cv2
import numpy
from pyrobot import Robot, Keys

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
img = cv2.equalizeHist(img)

x,y,w,h=0,0,len(img[0])/7,len(img)/10
img2=img.copy()
toClick=[]
for i in range(1,71):
    tmp=cv2.imread('Templates0\\'+str(i)+'.jpg',cv2.IMREAD_COLOR)[:,:,2]
    tw, th = tmp.shape[::-1]
    res = cv2.matchTemplate(img2,tmp,cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # if max_val<0.8:
    #     continue
    # toClick.append(max_loc)
    toClick.append(min_loc)
    cv2.putText(scrn,str(i),min_loc, cv2.FONT_HERSHEY_SIMPLEX,.5,(255,0,0),1,cv2.LINE_AA)
# for item in toClick:
#     robot.sleep(.5)
#     robot.move_and_click(item[0]+first[0],first[1]+item[1],button='left')
cv2.imshow('',scrn)
cv2.waitKey(0)