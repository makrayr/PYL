n=int(input('n='))
a=[]
for i in range(0, n):
    print('a[',i,']=')
    a.append(eval(input()))
for i in range(0, n-1):
    min=a[i]
    ind_min=i
    for j in range(i+1, n):
        if a[j]<min:
            min=a[j]
            ind_min=j
    a[ind_min]=a[i]
    a[i]=min

print('Sirul ordonat este:', a)