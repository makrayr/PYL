import localsolver
import os
import random

def sorteaza_fisiere(a):  # criteriul de sortare al fisierelor
    return len(a)


def generare_fisiere():
    nr_fisiere = 10
    try:
        os.mkdir('date_de_intrare_kp_with_LocalSolver')
    except:
        pass
    os.chdir('date_de_intrare_kp_with_LocalSolver')
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

def rezolva():
    c,g,gma=[],[],[]
    fisiere = os.listdir(os.getcwd())
    fisiere.sort(key=sorteaza_fisiere)
    date = []
    for fisier in fisiere:
        with open(fisier, 'r') as f:
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

    for i in range(len(c)):
        with localsolver.LocalSolver() as ls:
            weights = g[i]
            values = c[i]
            knapsack_bound = gma[i]

            #
            # Declares the optimization model
            #
            model = ls.model

            # 0-1 decisions
            x = [model.bool() for i in range(len(c))]

            # weight constraint
            knapsack_weight = model.sum(g[i] * x[i] for i in range(len(c)))
            model.constraint(knapsack_weight <= knapsack_bound)

            # maximize value
            knapsack_value = model.sum(values[i] * x[i] for i in range(len(c)))
            model.maximize(knapsack_value)

            model.close()

            #
            # Parameterizes the solver
            #
            ls.param.time_limit = 20

            ls.solve()
            print('\n')


generare_fisiere()
rezolva()