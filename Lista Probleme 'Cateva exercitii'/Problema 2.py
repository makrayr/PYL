def cerc_patrat(R,n):
    lat=0
    while n!=0:
        print(R)
        lat=R*2/(sqrt(2))
        print(lat)
        R=lat/2
        n-=1

n=int(input('n='))
R=float(input('R='))
print(cerc_patrat(R,n))