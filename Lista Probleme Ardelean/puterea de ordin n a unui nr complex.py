from numpy import zeros
a=int(input("a="))
b=int(input("b="))
n=int(input("n="))
x=a
y=b
for i in range(1, n):
  t=x
  x*=a-b*y
  y*=a+b*t
print("x=",x,' ',"y=",y)
print((a+b*1j)**n)