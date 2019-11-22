def prefix_sufix(a, b, c):
    if len(a) >= 4:
        if a.find(b) == 0:
            print(a + c)
        else:
            print(b + a)
    else:
        print('Șir prea scurt')

a=str(input('a='))
b=str(input('b='))
c=str(input('c='))
print(prefix_sufix(a,b,c))