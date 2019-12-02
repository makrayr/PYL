def distanta_max(x ,n, t):
    s=0
    while  x>=1 and t>0:
        s=s+x*n
        x/=2
        t-=n
    return s
x = float(input('viteza='))
n = float(input('nr de minute='))
t=int(input('timp total='))
print(distanta_max(x ,n))