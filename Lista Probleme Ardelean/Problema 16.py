def suma_inv(n):
    if n==1:
        return 1
    else:
        return 1/n+suma_inv(n-1)
n=int(input('n='))
print(suma_inv(n))