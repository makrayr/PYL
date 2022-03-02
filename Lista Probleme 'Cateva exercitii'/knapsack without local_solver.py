import random
import os

def sorteaza_fisiere(a):  # criteriul de sortare al fisierelor
    return len(a)

''' Variabile folosite in cadrul determinarii solutiilor :'''
c=[]
g=[]
gma=[]
vmo=[]
cperg=[]

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
        cpg=[]
        greutate = random.randint(10 ** 3, 10 ** 4)
        format_fisier = "Testul " + str(i + 1) + ".txt"
        f = open(format_fisier, 'w')
        numar_elemente_per_linie = random.randint(10, 10*2)
        for j in range(numar_elemente_per_linie):
            cpg.append([])
            greutati.append(random.randint(numar_elemente_per_linie**2, numar_elemente_per_linie**3))
            castiguri.append(random.randint(numar_elemente_per_linie**2, numar_elemente_per_linie**3))
            cpg.append(castiguri[j]/greutati[j])
        cperg.append(cpg)
        cpg.clear()
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
    cpg=[]
    for fisier in fisiere:
            try:
                with open(fisier,'r') as f:
                        for line in f:
                            date.append(line.split('\n'))
                        for j in range(len(date)):
                            try:
                                date[j].pop(1)
                            except:
                                pass
                        g.append(date[0][0].split(','))
                        c.append(date[1][0].split(','))
                        gma.append(int(date[2][0]))
                        date.clear()
            except:
                print('Nu am putut extrage nimic din fisier :(')

            for j in range(len(c)):
                cpg.append([])
                for k in range(len(c[j])):
                    c[j][k] = int(c[j][k])
                    g[j][k] = int(g[j][k])
    print(f'Datele extrase din cadrul celor {len(fisiere)} fisiere:\nGreutati({len(g)} seturi): {g[:]}\nCastiguri({len(c)} seturi): {c[:]}\nGreutati maxime admise({len(gma)} greutati maxime admise): {gma[:]}\nRaporturi castig per greutate({len(cperg)} rapoarte): {cperg[:]}')


generare_fisiere()
extragere_date()
