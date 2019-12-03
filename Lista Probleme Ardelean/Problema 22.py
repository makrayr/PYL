def arm(a,b,n):
    if n==0:
        med=a
    elif n==1:
        med=b
    else:
        med=2*arm(a,b,n-1)*arm(a,b,n-2)/(arm(a,b,n-1)+arm(a,b,n-2))
    return med

a=eval(input('a='))
b=eval(input('b='))
n=eval(input('n='))
print('Termenul de ordinul',n,'este:',arm(a,b,n))