from numpy import zeros
from math import *
xa=int(input("xa="))
ya=int(input("ya="))
xb=int(input("xb="))
yb=int(input("yb="))
xc=int(input("xc="))
yc=int(input("yc="))
a=((xb-xc)**2+(yb-yc)**2)**0.5
b=((xa-xc)**2+(ya-yc)**2)**0.5
c=((xb-xa)**2+(yb-ya)**2)**0.5
p=(a+b+c)/2
print("Aria este:",sqrt((p*(p-a)*(p-b)*(p-c))))
print("Perimetrul este:",2*p)