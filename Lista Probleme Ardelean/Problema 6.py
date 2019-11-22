from numpy import zeros
n=int(input("n="))
b[i]=zeros((n+1),dtype=float)
s=0
for i in range(1, n+1):
    print('a[',i,']=')
    b[i]=int(input())
    s+=b[i]
for i in range(1, n+1):
    b[i]=(s-b[i])/(n-1)
print(b)
