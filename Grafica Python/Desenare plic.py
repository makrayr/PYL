from graphics import *
win=GraphWin('Desenare plic',500,500)
win.setCoords(0,0,500,500)
P1=Point(250,400)
P2=Point(100,300)
P3=Point(100,100)
P4=Point(400,100)
P5=Point(400,300)
P=Polygon(P1,P2,P3,P4,P5)
L1=Line(P2,P4)
L2=Line(P3,P5)
L3=Line(P2,P5)

P.draw(win)
L1.draw(win)
L2.draw(win)
L3.draw(win)
win.getMouse()