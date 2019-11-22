def eliminare(sir,x):
    print(sir[:x-1]+sir[x:])
sir=str(input('sir='))
p=int(input('p='))
print(eliminare(sir,p))