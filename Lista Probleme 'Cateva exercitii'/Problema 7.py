def tip_triunghi(a,b,c,A):
    if a==b and a==c:
        print('Echilatral')
    elif ((a*b)/2==A or (a*c)/2==A or (c*b)/2==A) and (a==b or a==c or b==c):
        print('Triunghi dreptunghic isoscel')
    elif (a==b or a==c or b==c):
        print('Isoscel')
    elif (a*b)/2==A or (a*c)/2==A or (b*c)/2==A:
        print('Triunghi dreptunghic')
    else:
        print('Oarecare')

def arie_inaltimi(a,b,c):
    sp=(a+b+c)/2
    A=(sp*(sp-a)*(sp-b)*(sp-c))**0.5
    print('Aria=',A)
    print('Inaltimea perp. pe latura AB este:',(2*A)/c)
    print('Inaltimea perp. pe latura BC este:',(2*A)/a)
    print('Inaltimea perp. pe latura AC este:',(2*A)/b)
    if __name__=='__main__':
        tip_triunghi(a,b,c,A)

c=float(input('Latura AB='))
a=float(input('Latura BC='))
b=float(input('Latura AC='))

if __name__=='__main__':
    arie_inaltimi(a,b,c)