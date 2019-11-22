def ord_inversa(n):
    inp=n.split(' ')
    inp=inp[-1::-1]
    n=' '.join(inp)
    print(n)
n=str(input('n='))
print(ord_inversa(n))