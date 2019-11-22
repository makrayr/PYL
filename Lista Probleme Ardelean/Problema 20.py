from numpy import zeros
n=int(input('n='))
a=zeros((n+1),dtype=int)
b=zeros((n+1),dtype=int)
c=float(input('c='))
for i in range (0, n+1):
  print('a[', i ,']=')
  a[i]=eval(input())
b[0]=a[0]
for i in range (1, n+1):
 b[i]=c*b[i-1]+a[i]
print('Coeficientii catului sunt: ','\n')
for i in range(0, n):
    print(b[i],end=' ')
print('Restul este: ',b[n])
