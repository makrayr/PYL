n=int(input('Nr. obiecte='))
gr_rucsac=float(input('Greutatea maxima admisa de rucsac='))
castig_obtinut=0
greutate=[]
castig=[]
castig_greutate=[]
for i in range (0, n):
    print('Greutate obiect',i+1,'=')
    greutate.append(float(input()))
    print('Castig obiect',i+1,'=')
    castig.append(float(input()))
    castig_greutate.append(castig[i]/greutate[i])

ord=False
while not ord:
    ord=True
    for i in range(0, n-1):
        if castig_greutate[i]<=castig_greutate[i+1]:
            castig[i],castig[i+1]=castig[i+1],castig[i]
            greutate[i],greutate[i+1]=greutate[i+1],greutate[i]
            castig_greutate[i],castig_greutate[i+1]=castig_greutate[i+1],castig_greutate[i]
            ord=False

for i in range(0, n):
    if gr_rucsac == 0:
        break
    if greutate[i]>=gr_rucsac:
        castig_obtinut=castig_obtinut+((gr_rucsac*castig[i])/greutate[i])
        gr_rucsac=0
    else:
        castig_obtinut=castig_obtinut+castig[i]
        gr_rucsac-=greutate[i]

print('Castigul maxim ce poate fi obtinut este:',castig_obtinut)