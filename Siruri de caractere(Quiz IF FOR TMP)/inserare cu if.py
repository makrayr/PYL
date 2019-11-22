def inserare(a, b):
    if len(a) >= 2:
        if len(a) % 2 == 0:
            print(a[:len(a)//2] + b + a[len(a)//2:])
        else:
            print(a[:len(a)//2] + b + a[len(a)//2+1:])
    else:
        print('text prea scurt')

a=str(input('a='))
b=str(input('b='))
print(inserare(a,b))