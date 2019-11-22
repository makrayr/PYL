def num_cif(x):
    contor=0
    while x!=0:
        contor+=1
        x//=10
    return contor

def par_impar(x):
    par,impar=0, 0
    while x!=0:
        if (x%10)%2==0:
            par+=1
        else:
            impar+=1
        x//=10
    if par>=1 and impar>=1:
        return True
    else:
        return False

def corectitudine_cod(x):
    if num_cif(x)>=9 or par_impar(x)==False:
        return 'Cod incorect'
    suma=0
    produsul=1
    while x>9:
        if (x%10)%2==0:
            produsul*=x%10
        else:
            suma+=x%10
        x//=10
    if x%2==0:
        produsul*=x
    else:
        suma+=x
    if  produsul%x==suma%x:
        print('Cod corect')
    else:
        print('Cod incorect')

cod=eval(input('cod='))
print(corectitudine_cod(cod))