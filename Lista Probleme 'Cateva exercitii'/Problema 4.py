x=0
prog=[]
while True:
    x=int(input('x='))
    if x>-1:
     prog.append(x)
    else:
     break
r=prog[1]-prog[0]
k=1
x=len(prog)-1
for i in range(x, 1, -1):
    if prog[i]-prog[i-1]==r:
        k+=1
if k==x:
    print('Termenii dati reprezinta o progresie aritmetica cu ratia',r)
else:
    print('Termenii dati nu reprezinta o progresie aritmetica')