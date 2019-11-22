n=int(input("n="))
k=int(input("k="))
p=1
for i in range(1, k+1):
  p*=(n-i+1)/i
print("Combinari de",n,"luate cate",k,"=",p)