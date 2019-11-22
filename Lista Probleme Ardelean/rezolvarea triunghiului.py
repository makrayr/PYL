from numpy import zeros
from math import *
a=eval(input("a="))
b=eval(input("b="))
c=eval(input("c="))
p=(a+b+c)/2
P=2*p
S=math.sqrt(p * (p - a) * (p - b) * (p - c))
r=S/p
R=(a*b*c)/(4*S)
A=arccos((b**2+c**2-a**2)/(2*b*c))
B=arccos((a**2+c**2-b**2)/(2*a*c))
C=arccos((a**2+b**2-c**2)/(2*a*b))
print('Unghiul A este:', format(A, .2f))
print('Unghiul B este:', format(B, .2f))
print('Unghiul C este:', format(C, .2f))
print('Suprafata triunghiului este:', format(S, .5f))
print('Perimetrul triunghiului este:', format(S, .2f))
print('Raza cercului circumscris este:', format(R, .2f))
print('Raza cercului inscris este:',r)