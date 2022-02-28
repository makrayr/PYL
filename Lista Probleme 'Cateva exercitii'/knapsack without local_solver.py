import os
import random


def generare_fisiere():
    try:
        os.mkdir("date_de_intrare")
    except:
        print(f"Locatia folderului: {os.path.abspath('date_de_intrare')}")
    nr_fisiere=random.randint(10,20)
    for i in range(nr_fisiere):
        print(i, end='\n')
        greutati = []
        castiguri = []
        greutate = random.randint(nr_fisiere ** 2, nr_fisiere ** 5)
        format_fisier="Testul cu numarul " + str(i) +".txt"
        cale_completa = os.path.join(os.path.abspath('date_de_intrare'), format_fisier)
        f=open(cale_completa, 'w')
        numar_elemente_per_linie=random.randint(nr_fisiere**2,nr_fisiere**5)
        for j in range(numar_elemente_per_linie):
            greutati.append(random.randint(20,numar_elemente_per_linie))
            castiguri.append(random.randint(15,numar_elemente_per_linie))
        for j in range(numar_elemente_per_linie):
            if j!=numar_elemente_per_linie-1:
               f.write(str(castiguri[j]) + ",")
            else:
               f.write(str(castiguri[j]))
        f.write('\n')
        for j in range(numar_elemente_per_linie):
            if j!=numar_elemente_per_linie-1:
               f.write(str(greutati[j]) + ",")
            else:
               f.write(str(greutati[j]))
        f.write('\n' + str(greutate))
        castiguri.clear()
        greutati.clear()
        greutate=None

if '__name__' == '__main__':
    generare_fisiere()