def prim(n):
    if (n<2) or ((n>2) and n%2==0):
        return False
    d=3
    while d*d<=n:
        if n%d==0:
            return False
        else:
            d+=2
    return True

n=int(input('n='))
s=0
i=2
p=1
while p<=n:
    if prim(i)==True:
        s+=i
        i+=1
        p+=1
    else:
        i+=1
print('Suma primelor',n,'numere prime este:',s)