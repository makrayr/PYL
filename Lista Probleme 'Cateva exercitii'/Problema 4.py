x=0
prog=[]
while True:
    x=int(input('x='))
    if x>-1:
     prog.append(x)
    else:
     break
r=abs(prog[0]-prog[1])
k=1
for i in range(2,len(prog)-1):
    if abs(prog[i]-prog[i+1])==r:
        k+=1
if abs(prog[len(prog)-1]-prog[len(prog)-2])==r:
    k+=1
if k==len(prog)-1:
    print('Termenii dati reprezinta o progresie aritmetica')
else:
    print('Termenii dati nu reprezinta o progresie aritmetica')