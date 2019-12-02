x=0
prog=[]
while True:
    x=int(input('x='))
    if x>-1:
     prog.append(x)
    else:
     break
r=prog[1]-prog[0]
k=0
x=len(prog)-1
for i in range(x, 0 , -1):
    if prog[i]-prog[i-1]==r:
        k+=1
if k==(len(prog)-1):
    print('Termenii dati reprezinta o progresie aritmetica')
else:
    print('Termenii dati nu reprezinta o progresie aritmetica')