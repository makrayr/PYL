def sortare(list,n):
    ordine=False
    while not ordine:
        ordine=True
        for i in range(0, n-1):
            if list[i]>=list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                ordine=False
    return list

if __name__=='__main__':
m=int(input('nr elemente din A='))
n=int(input('nr elemente din B='))
A=[]
B=[]

for i in range(0, m):
    print('A[',i,']=')
    A.append(float(input()))

for i in range(0, n):
    print('B[',i,']=')
    B.append(float(input()))
A=sortare(A,m)
B=sortare(B,n)
print('Submultimea din B ce maximizeaza valoarea expresiei E este:')
if n==m:
    print(B[:])
else:
    print(B[0:m])
