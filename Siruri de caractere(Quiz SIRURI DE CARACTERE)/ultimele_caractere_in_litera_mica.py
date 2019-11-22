def ultimele_in_mica(n,b):
    n=n[:len(n)-b:]+n[len(n)-b::].lower()
    print(n)
n=str(input('n='))
b=int(input('b='))
print(ultimele_in_mica(n,b))