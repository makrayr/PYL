from graphics import *
win=GraphWin('Dreptunghi si diagonale',500,500)
win.setCoords(0,0,500,500)
A=Point(100,350)
B=Point(100,150)
C=Point(400,150)
D=Point(400,350)
L1=Line(A,C)
L2=Line(B,D)
dreptunghi=Polygon(A,B,C,D)
dreptunghi.setOutline('red')
dreptunghi.setWidth(3)

dreptunghi.draw(win)
L1.draw(win)
L2.draw(win)
win.getMouse()