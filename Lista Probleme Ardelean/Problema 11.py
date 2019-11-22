n=int(input('n='))
a=[]
for i in range(0, n):
    print('a[',i,']=')
    a.append(float(input()))
ordine=False
while not ordine:
    ordine=True
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            ordine=False

print(a)