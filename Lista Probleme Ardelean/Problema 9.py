n=int(input('n='))
a=[]
o=[0 for i in range(0, n)]
v=[0 for i in range(0, n)]
for i in range(0, n):
    print('a[',i,']=')
    a.append(float(input()))
for i in range (0, n-1):
    for j in range(i+1, n):
        if a[i]<=a[j]:
            o[j]+=1
        else:
            o[i]+=1
for i in range(0, n):
     v[o[i]]=a[i]
print('Sirul sortat este:', v)