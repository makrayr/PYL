def cel_mai_lung(nr_p, list):
    l_way=0
    l_way2=0
    for i in range(1, nr_p-1) :
        if list[i][0] >=list[i-1][0]:
            l_way += list[i][1]
        elif l_way > l_way2:
                l_way2=l_way
                l_way=0
    if l_way > l_way2:
        l_way2=l_way
    print(l_way2)
list=[]
nr_p = int(input('borne succesive ='))
for i in range(0, nr_p):
    list.append([])
    print('borna ', i+1)
    print('high =',end='')
    list[i].append(int(input()))
    print('distance =', end='')
    list[i].append(int(input()))
if __name__ == '__main__':
    cel_mai_lung(nr_p,list)