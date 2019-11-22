def litera_mica(n,x):
    n=n[:x:].lower()+n[x::]
    print(n)
n=str(input('n='))
x=int(input('x='))
print(litera_mica(n,x))