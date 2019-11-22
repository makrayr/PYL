from numpy import zeros
m = eval(input('m='))
n = eval(input('n='))
a = zeros((m, n), dtype=int)
def SA(m, n, a, l, c):
    e_sa = True
    for j in range(0, n):
        if a[l, c] > a[l, j]:
            e_sa = False
    for i in range(0, m):
        if a[l, c] < a[i, c]:
            e_sa = False
    if e_sa == True:
        return True
    else:
        return False


for i in range(0, m):
    for j in range(0, n):
        print('a[', i, j, ']=')
        a[i, j] = eval(input())
print('Punctele SA sunt pe pozitiile: ', end=' ')
for i in range(0, m):
    for j in range(0, n):
        if SA(a, m, n, i, j) == True:
            print('(', i, ',', j, ')', end=' ')
