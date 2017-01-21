from PIL import ImageGrab
import cv2
import numpy
import time
time.sleep(5)

first=[460,126]
last=[905,758]
x,y=first[0],first[1]
w,h=last[0]-first[0],last[1]-first[1]


scrn = numpy.array(ImageGrab.grab().convert('RGB')) 
scrn = scrn[:, :, ::-1].copy() 
img = scrn[:,:,2]
img=img[y:y+h, x:x+w]
img = cv2.equalizeHist(img)

w,h= len(img[0])/7,len(img)/10
x,y=0,0
for i in range(0,7):
    for j in range(0,10):
        x,y=i*w,j*h
        cv2.imwrite('Templates0\\q'+str(i)+str(j)+'.bmp',img[y+15:y+h-15,x+15:x+w-15])
