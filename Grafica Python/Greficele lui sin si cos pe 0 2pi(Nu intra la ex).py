from graphics import *
from math import *
win=GraphWin('Graficele lui sin si cos',400,200)
win.setCoords(0,0,400,200)
for i in range(0, 301):
    t=2*pi*i/300
    P=Point(200/pi*t,100*sin(t)+100)
    P.setOutline('red')
    P.draw(win)
    P=Point(200/pi*t,100*cos(t)+100)
    P.setOutline('blue')
    P.draw(win)
    P=Point(200/pi*t,100)
    P.setOutline('black')
    P.draw(win)
win.getMouse()
win.close()