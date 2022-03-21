import numpy as np
import transport
import os


def extract_data(fname):
    try:
        myFile = open(fname, "r")
    except FileNotFoundError:
        print("File not found.\n")
        return

        # initializam parametrii problemei
    instance_name = "null"
    no_storages = 0
    no_shops = 0
    storage_capacity = []
    shop_capacity = []
    cost = []

    lineCount = 0
    thing = []

    # parcurgem fiecare linie din fisier
    for line in myFile:
        # daca pe o linie avem instance_name(numele instantei)
        # extragem numele instantei
        if line.startswith("instance_name"):
            instance_name = line.split("=")[1]
            instance_name = instance_name[2:len(instance_name) - 3]

        # extragem nr de depozite
        if line[0] == "d":
            temp = line.split("=")[1]
            temp = temp.replace("\n", "")
            temp = temp.replace(";", "")
            no_storages = int(temp)

        # extragem nr magazine
        if line[0] == "r":
            temp = line.split("=")[1]
            temp = temp.replace("\n", "")
            temp = temp.replace(";", "")
            no_shops = int(temp)

            # extragem capacitatea fiecarui depozit

        if line.startswith("SCj"):
            temp = line.split("=")[1]  # [x1 x2 ... xn]
            temp = temp.replace("\n", "")
            temp = temp.replace(";", "")
            temp = temp.replace("[", "")
            temp = temp.replace("]", "")
            temp = temp.lstrip()
            temp = temp.rstrip()
            temp = temp.split(" ")
            storage_capacity = [int(n) for n in temp]

        # extragem cerinta fiecarui depozit
        if line.startswith("Dk"):
            temp = line.split("=")[1]  # [x1 x2 ... xn]
            temp = temp.replace("\n", "")
            temp = temp.replace(";", "")
            temp = temp.replace("[", "")
            temp = temp.replace("]", "")
            temp = temp.lstrip()
            temp = temp.rstrip()
            temp = temp.split(" ")
            shop_capacity = [int(n) for n in temp]

        # extragem costul

        if lineCount >= 13:
            tempLine = line.replace("\n", "")
            tempLine = tempLine.lstrip()
            tempLine = tempLine.rstrip()
            if tempLine.startswith("Cjk = "):
                tempLine = tempLine.replace("Cjk = ", "")

            if tempLine.startswith("[["):
                temp = tempLine.replace("[[", "")
                if temp.endswith("]"):
                    temp = temp.replace("]", "")
                temp = temp.split(" ")
                thing += [int(x) for x in temp]
            elif tempLine[0] == "[" and not tempLine.endswith("]];"):
                temp = tempLine.replace("[", "")
                if temp.endswith("]"):
                    temp = temp.replace("]", "")
                temp = temp.split(" ")
                thing += [int(x) for x in temp]
            elif tempLine.endswith("]"):
                temp = tempLine.rstrip("]")
                temp = temp.split(" ")
                thing += [int(x) for x in temp]
                cost.append(thing)
                thing = []
            elif tempLine.endswith("]];"):
                temp = tempLine.replace("]];", "")
                if temp.startswith("["):
                    temp = temp.replace("[", "")
                temp = temp.split(" ")
                thing += [int(x) for x in temp]
                cost.append(thing)
            else:
                if tempLine.startswith("[") and tempLine.endswith("]"):
                    temp = temp.replace("[", "")
                    temp = temp.replace("]", "")
                temp = tempLine.split(" ")
                thing += [int(x) for x in temp]

        lineCount += 1

    # pentru instantele medii si mici, extractia nu se face corect
    # aici se face corectura

    if len(cost) != no_storages:
        tempCost = cost[0][:]
        tempCost = np.reshape(tempCost, (no_storages, no_shops))
        tempCost = tempCost.tolist()

        cost.clear()
        cost = tempCost[:]

    return instance_name, no_storages, no_shops, storage_capacity, shop_capacity, cost