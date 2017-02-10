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
tmp=[]
# for i in range(0,10):
#     tmp.append(cv2.imread('Templates0\\'+str(i)+'.jpg',0))
for i in range(0,10):
    tmp=cv2.imread('Templates0\\'+str(i)+'.jpg',0)
    # res = cv2.matchTemplate(img2,tmp,cv2.TM_SQDIFF_NORMED)
    w, h = tmp.shape[::-1]
    res = cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = numpy.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        # cv2.rectangle(scrn, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.putText(img2,str(i),pt , cv2.FONT_HERSHEY_SIMPLEX,.5,0,1,cv2.LINE_AA)
        
    # toClick.append(min_loc)
    # cv2.putText(scrn,str(i),min_loc, cv2.FONT_HERSHEY_SIMPLEX,.5,(255,0,0),1,cv2.LINE_AA)
# for i in range(0,7):
#     for j in range(0,10):
#         x,y=i*w,j*h
#         subimg=img[y+10:y+h-10,x+10:x+w-10]
#         for t in tmp:
#             res = cv2.matchTemplate(subimg,t,cv2.TM_SQDIFF_NORMED)
#             min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#             if max_val<0.3:
#                 continue
#             cv2.putText(scrn,'x',(min_loc[0]+x,min_loc[1]+y), cv2.FONT_HERSHEY_SIMPLEX,.5,(255,0,0),1,cv2.LINE_AA)

# for item in toClick:
#     robot.sleep(.5)
#     robot.move_and_click(item[0]+first[0],first[1]+item[1],button='left')
cv2.imshow('',img2)
cv2.waitKey(0)