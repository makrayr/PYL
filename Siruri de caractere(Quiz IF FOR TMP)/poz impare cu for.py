def impare(a):
    for i in range(len(a)):
        if i % 2 == 0:
            print(a[i], end= '')
a=str(input('a='))
print(impare(a))