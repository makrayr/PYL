from graphics import *
win=GraphWin('Dreptungi si oval cu mouse-ul',500,500)
win.setCoords(0,0,500,500)
P1=win.getMouse()
P1.draw(win)
P2=win.getMouse()
P2.draw(win)
O=Oval(P1,P2)
D=Rectangle(P1,P2)
D.setOutline('blue')
D.setWidth(3)
O.setOutline('red')
O.setFill('green')
O.setWidth(3)
D.draw(win)
O.draw(win)
win.getMouse()