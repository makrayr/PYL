from numpy import zeros
from math import *
n=int(input('n='))
b=int(input('b='))
k=ceil(log10(n)/log10(b))+1
v=zeros((k),dtype=int)
i=0
while n!=0:
    v[i]=n%b
    i+=1
    n//=b
print('Exprimarea nr dat in baza ',b,' este:','\n')
for j in range(i-1, -1, -1):
    print(v[j])
