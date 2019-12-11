m=int(input('nr elemente din A='))
n=int(input('nr elemente din B='))
A=[]
B=[]
for i in range(0, m):
    print('A[',i,']=')
    A.append(float(input()))

for i in range(0,n):
    print('B[',i,']=')
    B.append(float(input()))
A.sort()
B.sort()
print('Submultimea din B ce maximizeaza valoarea expresiei E este:')
if n==m:
    print(B[:])
else:
    print(B[0:m])
