from numpy import zeros
n=int(input("n="))
v=zeros((500),dtype=int)
m=n
i=0
while n!=4:
    v[i]=n
    i=i+1
    if n%10==0:
        n=n//10
    elif n%10==4:
        n=n//10
    else:
        n=n*2
v[i]=4
for k in range(i ,-1,-1):
    print(v[k] , end=' ')