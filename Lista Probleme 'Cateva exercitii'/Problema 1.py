def distanta_max(x ,n):
    s=0
    while  x>=1:
        s=s + x*n
        x/=2
    return s
x = float(input('x='))
n = float(input('n='))
print(distanta_max(x ,n))