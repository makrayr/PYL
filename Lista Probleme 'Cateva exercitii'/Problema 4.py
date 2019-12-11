x=0
prog=[]
while True:
    x=int(input('x='))
    if x>-1:
     prog.append(x)
    else:
     break
r=prog[1]-prog[0]
este_prog=True
for i in range(len(prog)-1, 1, -1):
    if prog[i]-prog[i-1]!=r:
        este_prog=False
        print('Sirul nu este o progresie aritmetica')
        break

if este_prog==True:
    print('Sirul este o progresie aritmetica')