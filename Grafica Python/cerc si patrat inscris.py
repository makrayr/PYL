from graphics import *
win=GraphWin('Cerc si patrat inscris',500,500)
win.setCoords(0,0,500,500)
C=Circle(Point(250,250),100)
C.setOutline('red')
C.setWidth(3)
x=250-(100/(2)**0.5)
y=250+(100/(2)**0.5)
P=Rectangle(Point(x,x),Point(y,y))
C.draw(win)
P.draw(win)
win.getMouse()
win.close()