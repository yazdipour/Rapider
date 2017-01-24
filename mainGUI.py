from PIL import ImageGrab,Image
import cv2
import numpy
from Tkinter import *
from pyrobot import Robot, Keys

def go():
    toClick=[0]*70
    i,j=0,0
    for txt10 in txtbox:
        for txt7 in txt10:
            try:
                nr=int(txt7.get())
                if nr>0 and nr<71:
                    toClick[nr]=[i,j]
            except :
                pass
            j=j+1
        i=i+1
        j=0
    for item in toClick:
        if item==0:
            continue
        robot.sleep(.3)
        robot.move_and_click(item[1]*pw+first[0]+30,30+first[1]+item[0]*ph,button='left')
    return
def ocr():
    img = numpy.array(ImageGrab.grab().convert('RGB'))[:, :, ::-1].copy()[y:y+h, x:x+w][:,:,2]
    # img = cv2.equalizeHist(img)
    index=0
    for tmp in templates:
        res = cv2.matchTemplate(img,tmp,cv2.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        ix,iy=max_loc[0]/pw,max_loc[1]/ph
        strx=txtbox[iy][ix].get()
        index=index+1
        txtbox[iy][ix].insert(len(strx),str(index))
    return


robot=Robot()
first,last=[460,126],[905,758]
x,y,w,h=first[0],first[1],last[0]-first[0],last[1]-first[1]
pw,ph=w/7,h/10
templates=[]
txtbox = [[] for i in range(10)]
root = Tk()
for r in range(10):
    for c in range(7):
        t=Entry(root,width=6)
        t.grid(row=r,column=c,ipady=4)
        # t.pack()
        txtbox[r].append(t)
Button(root, text ="Go",width=30,command=go,bg='green').grid(pady=10,columnspan=7)
Button(root, text ="OCR",width=30,command=ocr,bg='lightblue').grid(pady=10,columnspan=8)
for i in range(1,71):
    templates.append(cv2.imread('Templates0\\'+str(i)+'.bmp',cv2.TM_CCORR_NORMED)[:,:,2])

def __init__(self):
    return

root.mainloop()    