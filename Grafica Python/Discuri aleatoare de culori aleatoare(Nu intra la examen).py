from graphics import *
from random import *
import time
def alegere():
    culori=['blue','black','brown','red','yellow','green','orange','magenta','turquoise','pink']
    shuffle(culori)
    return culori[0]
win=GraphWin('Discuri aleatoare',500,500)
win.setCoords(0,0,500,500)
while True:
    x=int(uniform(0,500))
    y=int(uniform(0,500))
    r=int(uniform(0,50))
    C=Circle(Point(x,y),r)
    c=alegere()
    C.setFill(c)
    C.draw(win)
    time.sleep(0.02)
    if win.getMouse()!=None :
        break

win.close()