from numpy import zeros
n=int(input("n="))
a=zeros((n),dtype=float)
s,s1=0,0
k,k1=0,0
for i in range(0, n):
  print('a[', i ,']=')
  a[i]=float(input())
  if a[i]>0:
    s+=a[i]
    k+=1
  if a[i]<0:
    s1+=a[i]
    k1+=1
if k==0:
  print('Nu exista termeni pozitivi')
else:
  print('Media termenilor pozitivi este: ',s/k)
if k1==0:
  print('Nu exista termeni negativi')
else:
  print('Media termenilor negativi este: ',s1/k1)