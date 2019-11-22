n = int(input("n="))
aux=n
p=0
while n!=0:
  p*=10
  p+=n % 10
  n//=10
if aux==p:
  print('Numarul ', aux ,'este palindrom')
else:
  print('Numarul ', aux ,' nu este palindrom')