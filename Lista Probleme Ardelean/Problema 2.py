from numpy import zeros
m=int(input("m="))
n=int(input("n="))
a=zeros((m,n),dtype=int)
b=zeros((m,n),dtype=int)
v=zeros((m*n),dtype=int)
for i in range(0, m):
 for j in range(0, n):
     print('a[',i,j,']=')
     a[i,j]=eval(input())
     print('b[',i,j,']=')
     b[i,j]=eval(input())
     v[b[i,j]]=a[i,j]
print('Elementele matricii A dupa ordinea data de B sunt:')
print(v)