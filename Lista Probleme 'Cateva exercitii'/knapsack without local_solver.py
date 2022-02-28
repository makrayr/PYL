import random


def generare_fisiere():
    nr_fisiere = random.randint(10, 20)
    for i in range(nr_fisiere):
        greutati = []
        castiguri = []
        greutate = random.randint(nr_fisiere, nr_fisiere ** 2)
        format_fisier = "Testul " + str(i + 1) + ".txt"
        f = open(format_fisier, 'w')
        numar_elemente_per_linie = random.randint(nr_fisiere, nr_fisiere*2)
        for j in range(numar_elemente_per_linie):
            greutati.append(random.randint(12, numar_elemente_per_linie))
            castiguri.append(random.randint(12, numar_elemente_per_linie))
        for k in range(numar_elemente_per_linie):
            if k != numar_elemente_per_linie - 1:
                f.write(str(castiguri[k]) + ",")
            else:
                f.write(str(castiguri[k]))
        f.write('\n')
        for l in range(numar_elemente_per_linie):
            if l != numar_elemente_per_linie - 1:
                f.write(str(greutati[l]) + ",")
            else:
                f.write(str(greutati[l]))
        f.write('\n' + str(greutate))
        castiguri.clear()
        greutati.clear()
        greutate = None


generare_fisiere()
