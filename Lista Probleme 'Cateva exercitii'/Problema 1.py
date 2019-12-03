def distanta_max(x ,n, t):
    s=0
    while  x>=1 and t>0:
        s=s+x*n
        x/=2
        t-=n
    return s
x = float(input('viteza='))
n = float(input('Nr de minute dupa care magarusul oboseste='))
t=int(input('timp total='))
print(format(distanta_max(x ,n, t),'.2f'))