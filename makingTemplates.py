from PIL import ImageGrab
import cv2
import numpy
import time
time.sleep(5)

# img=ImageGrab.grab()
# img = numpy.array(img.convert('L')) 
# img = img[:, :].copy() 
scrn = numpy.array(ImageGrab.grab().convert('RGB')) 
scrn = scrn[:, :, ::-1].copy() 
img = scrn[:,:,2]

first=[460,126]
last=[905,758]
x,y=first[0],first[1]
w,h=last[0]-first[0],last[1]-first[1]
img=img[y:y+h, x:x+w]
w,h= len(img[0])/7,len(img)/10
x,y=0,0
for i in range(0,7):
    for j in range(0,10):
        x,y=i*w,j*h
        cv2.imwrite('Templates\\q'+str(i)+str(j)+'.jpg',img[y+10:y+h-10,x+10:x+w-10])
