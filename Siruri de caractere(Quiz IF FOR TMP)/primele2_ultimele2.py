def p2_u2(a):
    if len(a) >= 2:
        print(a[:2] + a[len(a)-2:])
    else:
        print("Șirul este prea scurt.")
a=str(input('a='))
print(p2_u2(a))