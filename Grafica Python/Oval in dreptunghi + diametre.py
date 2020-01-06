from graphics import *
win=GraphWin('Dreptunghi si oval centrate',500,500)
win.setCoords(0,0,500,500)
P1=Point(100,350)
P2=Point(400,150)
M=Point(250,350)
N=Point(250,150)
P=Point(100,250)
Q=Point(400,250)

D=Rectangle(P1,P2)
MN=Line(M,N)
PQ=Line(P,Q)
O=Oval(P1,P2)

D.setOutline('blue')
D.setWidth(3)

O.setOutline('red')
O.setWidth(3)

MN.setOutline('green')
MN.setWidth(3)
PQ.setOutline('green')
PQ.setWidth(3)

D.draw(win)
O.draw(win)
MN.draw(win)
PQ.draw(win)
win.getMouse()
win.close()