def Fibo(a,b,n):
    if n==0:
        f=a
    elif n==1:
        f=b
    else:
        f=Fibo(a,b,n-1)+Fibo(a,b,n-2)
    return f

a=eval(input('a='))
b=eval(input('b='))
n=eval(input('n='))
for i in range(0, n):
    print(Fibo(a,b,i),end=' ')