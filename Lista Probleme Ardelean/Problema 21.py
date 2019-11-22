from numpy import zeros
from math import sqrt
n=int(input('n='))
X=zeros((n),dtype=float)
Y=zeros((n),dtype=float)
D=zeros((n),dtype=float)

for i in range(0, n):
    print('X[',i,']=',end='')
    X[i]=float(input())
    print('Y[',i,']=',end='')
    Y[i]=float(input())
    D[i]=sqrt(X[i]**2+Y[i]**2)

ordine=False
while not ordine:
    ordine=True
    for i in range(0, n-1):
        if D[i]<D[i+1]:
            D[i],D[i+1]=D[i+1], D[i]
            X[i],Y[i],X[i+1],Y[i+1]=X[i+1], Y[i+1], X[i], Y[i]
            ordine=False

print('Punctele ordonate sunt:',end='')
for i in range(0, n):
    print('(',X[i],',',Y[i],')',end='')