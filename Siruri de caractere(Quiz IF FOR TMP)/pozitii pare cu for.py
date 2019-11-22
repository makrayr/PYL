def pare(a):
    for i in range(len(a)):
        if i % 2 == 1:
            print(a[i], end = '')
a=str(input('a='))
print(pare(a))