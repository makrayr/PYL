def suma_inv(n):
    s=1
    for i in range(2,n+1):
        s+=1/i
    print(s)
n=int(input('n='))
print(suma_inv(n))