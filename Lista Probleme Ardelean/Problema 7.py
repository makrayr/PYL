p=eval(input('p='))
q=eval(input("q="))
fc=[]
d=p
i=q
r=1
while r!=0:
    r=d%i
    c=d//i
    fc.append(c)
    d=i
    i=r
print(fc)