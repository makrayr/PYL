n=int(input("n="))
aux=n
cmax=0
while n!=0:
  if n%10>cmax:
    cmax=n%10
  else:
    n//=10
print("Cifra maxima a numarului ",aux,' este: ',cmax)