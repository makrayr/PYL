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
for i in range(1, n+1):
    if prim(i)==True:
        print(i, end=' ')