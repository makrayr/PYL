from math import sqrt
def cerc_patrat(R,n):
    latura=0
    x=sqrt(2)
    while n!=0:
        print(R)
        latura=(R*2)/x
        print(latura)
        R=latura/2
        n-=1

n=int(input('n='))
R=float(input('R='))
print(cerc_patrat(R,n))