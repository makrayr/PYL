p=int(input("p="))
q=int(input("q="))
d=p
i=q
r=1
while r!=0:
    r=d%i
    d=i
    i=r
print(p,"/",q," ",p//d,"/",q/d)