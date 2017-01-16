from PIL import ImageGrab
import cv2
import numpy

img=cv2.imread('img.tiff',0)
first=[482,186]
last=[883,759]
x,y=first[0],first[1]
w,h=last[0]-first[0],last[1]-first[1]
img=img[y:y+h, x:x+w]
x,y,w,h=0,0,len(img[0])/7,len(img)/10
img2=img.copy()

for i in range(1,71):
    tmp=cv2.imread('Templates\\'+str(i)+'.jpg',0)
    tw, th = tmp.shape[::-1]
    res = cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val<0.8:
        continue
    top_left = max_loc
    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(img,top_left, bottom_right,0, 2)

cv2.imshow('',img)
cv2.waitKey(0)