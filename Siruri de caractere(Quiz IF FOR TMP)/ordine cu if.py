def ordine(a):
    if len(a) % 4 == 0:
        print(a[::-1])
    elif len(a) % 3 == 0:
        print(a[::2])
    else:
        print(a)


a = str(input('a='))
print(ordine(a))
