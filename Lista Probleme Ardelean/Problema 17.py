from numpy import *
m=int(input('m='))
n=int(input('n='))
p=int(input('p='))
a=[]
b=[]
c=[]
for i in range(0, m):
    a.append([])
    for j in range(0, n):
        print('a[',i,j,']=')
        a[i].append(float(input()))

for i in range(0, n):
    b.append([])
    for j in range(0, p):
        print('b[',i,j,']=')
        b[i].append(float(input()))

for i in range(0, m):
    c.append([])
    for j in range(0, p):
        c[i].append(0)

for i in range(0, m):
    for j in range(0, p):
        for k in range(0, n):
            c[i][j]= c[i][j] + a[i][k] * b[k][j]

print('Rezultatul este:')
for linie in c:
  for valoare in linie:
         print(valoare, end=' ')
print('\n')
print('Rezultatul cu functia dot din numpy este :',dot(a,b))