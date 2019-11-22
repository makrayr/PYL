from math import sqrt
def radical(a, eps):
    x = a
    y = 0.5*(x+a/x)
    while abs(x-y) >= eps:
        x = y
        y = 0.5*(x+a/x)
    return y

while True:
    a=eval(input())
    if a>0:
        break
eps=eval(input('eps='))
print('Radicalul aproximativ=', radical(a,eps))
print('Rezultatul cu functia sqrt este:', sqrt(a))