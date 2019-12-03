a=eval(input('a='))
b=eval(input('b='))
eps=eval(input('eps='))
x=a
y=b
while abs(x-y)>=eps:
    z=(x+y)/2
    x=y
    y=z
print('Limita este:',z)
