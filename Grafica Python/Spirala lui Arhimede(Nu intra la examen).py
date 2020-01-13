from graphics import *
from math import *
win=GraphWin('Spirala lui Arhimede',500,500)
win.setCoords(0,0,500,500)
v=int(input('v='))
w=int(input('w='))
for i in range(0,1001):
    t=(20*pi*i)/1000
    r=v*t
    theta=w*t
    x=250+r*cos(theta)
    y=250+r*sin(theta)
    P=Point(x,y)
    P.setOutline('red')
    P.draw(win)
win.getMouse()
win.close()