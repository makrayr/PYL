from numpy import zeros
n=int(input("n="))
aux=n
p=0
while n!=0:
  p=p*10+n%10
  n//=10
print('Oglinditul lui ',aux,' este:',p)
