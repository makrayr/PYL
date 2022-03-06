import random
import os

def sorteaza_fisiere(a):  # criteriul de sortare al fisierelor
    return len(a)

''' Variabile folosite in cadrul determinarii solutiilor :'''
c=[]
g=[]
gma=[]
vmo=[0 for i in range(10)]

def generare_fisiere():
    nr_fisiere = 10
    try:
        os.mkdir('date_de_intrare_kp_without_LocalSolver')
    except:
        pass
    os.chdir('date_de_intrare_kp_without_LocalSolver')
    for i in range(nr_fisiere):
        greutati = []
        castiguri = []
        greutate = random.randint(10 ** 3, 10 ** 4)
        format_fisier = "Testul " + str(i + 1) + ".txt"
        f = open(format_fisier, 'w')
        numar_elemente_per_linie = random.randint(10, 10*2)
        for j in range(numar_elemente_per_linie):
            greutati.append(random.randint(numar_elemente_per_linie**2, numar_elemente_per_linie**3))
            castiguri.append(random.randint(numar_elemente_per_linie**2, numar_elemente_per_linie**3))
        for l in range(numar_elemente_per_linie):
            if l != numar_elemente_per_linie - 1:
                f.write(str(greutati[l]) + ",")
            else:
                f.write(str(greutati[l]))
        f.write('\n')
        for k in range(numar_elemente_per_linie):
            if k != numar_elemente_per_linie - 1:
                f.write(str(castiguri[k]) + ",")
            else:
                f.write(str(castiguri[k]))
        f.write('\n' + str(greutate))
        castiguri.clear()
        greutati.clear()



def extragere_date():
    i=0
    fisiere=os.listdir(os.getcwd())
    fisiere.sort(key=sorteaza_fisiere)
    date=[]
    for fisier in fisiere:
            with open(fisier,'r') as f:
                    for line in f:
                        date.append(line.split('\n'))
            g.append(date[0][0].split(','))
            c.append(date[1][0].split(','))
            gma.append(int(date[2][0]))
            date.clear()

            for j in range(len(c)):
                for k in range(len(c[j])):
                    c[j][k] = int(c[j][k])
                    g[j][k] = int(g[j][k])
    print(f'Datele extrase din cadrul celor {len(fisiere)} fisiere:\nGreutati({len(g)} seturi): {g[:]}\nCastiguri({len(c)} seturi): {c[:]}\nGreutati maxime admise({len(gma)} greutati maxime admise): {gma[:]}')


def rezolvare_seturi_de_date():
    for i in range(10):
            ord = False
            while not ord:
                ord = True
                for l in range(len(g[i])-1):
                    if (c[i][l]/g[i][l]) < (c[i][l+1]/g[i][l+1]):
                        c[i][l], c[i][l+1] = c[i][l+1], c[i][l]
                        g[i][l], g[i][l + 1] = g[i][l + 1], g[i][l]
                        ord = False

    for i in range(10):
        for j in range(len(g[i])):
            if g[i][j] <= gma[i]:
                gma[i]-=g[i][j]
                vmo[i]+=c[i][j]
    vmax=0
    poz=0
    for i in range(len(vmo)):
        if vmo[i] > vmax:
            vmax=vmo[i]
            poz=i
    print(f'\nValoarea maxima obtinuta in cadrul celor 10 teste este: {vmax}\n')
    print(f'Numele testului care a obtinut aceasta valoare este Testul {poz+1}')
    os.chdir('.')


generare_fisiere()
extragere_date()
rezolvare_seturi_de_date()