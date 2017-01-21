from pyrobot import Robot, Keys
import win32clipboard

first=[460,126]
last=[905,758]
x,y=first[0],first[1]
w,h=last[0]-first[0],last[1]-first[1]
robot=Robot()
win32clipboard.OpenClipboard()

while True:
    raw_input("Press Enter to continue...")
    data = win32clipboard.GetClipboardData()
    nrs=data.split()
    for z in range(1,71):
        index=nrs.index(str(z))
        # if z=="D":
        #     index=nrs.index("D")
        i=(index-1)%7
        j=(index-1)/7
        robot.sleep(2)
        print(str(z)+":"+str(i)+str(j))
        robot.move_and_click(x+w*i,y+h*j,button='left')

win32clipboard.CloseClipboard()
    