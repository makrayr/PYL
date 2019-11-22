def rost_st(k):
    global sus,jos,dr,st,fa,sp
    for i in range(0, k%4):
        sus,jos,dr,st=dr,st,jos,sus

def rost_dr(k):
    global sus,jos,dr,st,fa,sp
    for i in range(0, k%4):
       sus,jos,dr,st=st,dr,sus,jos

def rost_fa(k):
    global sus, jos, dr, st, fa, sp
    for i in range(0, k%4):
        sus,jos,fa,sp=sp,fa,sus,jos

def rost_sp(k):
    global sus, jos, dr, st, fa, sp
    for i in range(0, k%4):
        sus,jos,fa,sp=fa,sp,jos,sus

print('Dati pozitia initiala a zarului: ')
sus=int(input('Sus='))
fa=int(input('Fata='))
dr=int(input('Dreapta='))
jos=7-sus
sp=7-fa
st=7-dr
while True:
    dir=str(input('Directia?(st,dr,fa,sp)'))
    k=int(input('Nr pasi='))
    if dir=='st':
        rost_st(k)
    if dir=='dr':
        rost_dr(k)
    if dir=='fa':
        rost_fa(k)
    if dir=='sp':
        rost_sp(k)
    print('Pozitia zarului este:','\n')
    print('sus=',sus,'\n','jos=',jos,'\n','fata=',fa,'\n','spate=',sp,'\n','stanga=',st,'\n','dreapta=',dr,'\n')
    cont=str(input('Continuati? (d/n)'))
    if (cont=='N') or (cont=='n'):
          break