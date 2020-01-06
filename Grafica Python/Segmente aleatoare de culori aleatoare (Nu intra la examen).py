from graphics import *
from random import *
import time
def alegere():
    culori=['blue','black','brown','red','yellow','green','orange','magenta','turquoise','pink']
    shuffle(culori)
    return culori[0]
win=GraphWin('Segmente aleatoare',500,500)
win.setCoords(0,0,500,500)
while True:
    x1=int(uniform(0,500))
    y1=int(uniform(0,500))
    x2=int(uniform(0,500))
    y2=int(uniform(0,500))
    Linie=Line(Point(x1,y1),Point(x2,y2))
    c=alegere()
    Linie.setOutline(c)
    Linie.setWidth(5)
    Linie.draw(win)
    time.sleep(0.01)
    if win.getMouse()!=None:
        break
win.close()