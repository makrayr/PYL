from math import cos
def f(x):
    return cos(x)-x
a=eval(input('a='))
b=eval(input('b='))
eps=eval(input('eps='))
c=(a+b)/2
while abs(b-a)>=eps:
    if f(c)==0:
        print('Radacina este:',c)
    elif f(a)*f(c)<0:
        b=c
    else:
        c=a
    c=(a+b)/2
print('Radacina aprox. este:',format(c,'.5f'))