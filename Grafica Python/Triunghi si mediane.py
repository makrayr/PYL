from graphics import *
win=GraphWin('Triunghi si mediane',500,500)
win.setCoords(0,0,500,500)
mes=Text(Point(100,450),'Dati click pe 3 puncte')
mes.draw(win)
A=win.getMouse()
A.draw(win)
B=win.getMouse()
B.draw(win)
C=win.getMouse()
C.draw(win)
Triunghi=Polygon(A,B,C)
Triunghi.setOutline('blue')
Triunghi.setWidth(3)
M=Line(B,C).getCenter()
N=Line(A,C).getCenter()
P=Line(A,B).getCenter()
PC=Line(P,C)
PC.setOutline('red')
PC.setWidth(3)
AM=Line(A,M)
AM.setOutline('red')
AM.setWidth(3)
BN=Line(B,N)
BN.setOutline('red')
BN.setWidth(3)
G=Point((A.getX()+B.getX()+C.getX())/3,(A.getY()+B.getY()+C.getY())/3)
CercG=Circle(G,4)
CercG.setWidth(6)
CercG.setOutline('green')
Triunghi.draw(win)
PC.draw(win)
AM.draw(win)
BN.draw(win)
CercG.draw(win)
Ancora_G=Point(G.getX()+20,G.getY())
TextG=Text(Ancora_G,'G')
TextG.draw(win)
win.getMouse()