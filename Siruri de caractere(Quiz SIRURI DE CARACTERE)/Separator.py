def separator(n,b):
    inp=n.rsplit(b, 2)
    print(inp[0])
n=str(input('n='))
b=str(input('b='))
print(separator(n,b))