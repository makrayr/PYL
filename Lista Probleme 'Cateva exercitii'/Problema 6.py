n=int(input('n='))
print('Modurile prin care',n,'poate fi scris ca suma de 2 termeni consecutivi este:','\n')
for i in range(0, (n//2)+1):
    print(i,'+',n-i,'\n')