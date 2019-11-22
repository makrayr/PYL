n = int(input('n='))
a = []
for i in range(0, n):
    linie = []
    for j in range(0, n):
        print('a[',i,j,']=')
        linie.append(int(input()))
    a.append(linie)

SD, SS, SP = 0, 0, 0
for i in range(0, n):
    for j in range(0, n):
        if i==j:
            SP+=a[i][j]
        elif i<j:
            SD+=a[i][j]
        else:
            SS+=a[i][j]

print('Media pe diagonala este: ',SP/n)
print('Media sub diagonala este: ', SS/((n**2-n)/2))
print('Media deasupra diagonalei este: ', SD/((n**2-n)/2))