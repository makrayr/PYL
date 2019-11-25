def the_longest_high(nr_of_p, my_list):
    longer_way=0
    longer_way2=0
    for i in range(1, nr_of_p-1) :
        if my_list[i][0] >=my_list[i-1][0]:
            longer_way += my_list[i][1]
        else:
            if longer_way > longer_way2:
                longer_way2=longer_way
                longer_way=0
    if longer_way > longer_way2:
        longer_way2=longer_way
    print( longer_way2)


my_list=[]
nr_of_p = int(input('borne succesive ='))
for i in range(0, nr_of_p):
    my_list.append([])
    print('borna ', i+1)
    print('high =',end='')
    my_list[i].append(int(input()))
    print('disase =', end='')
    my_list[i].append(int(input()))
if __name__ == '__main__':
    the_longest_high(nr_of_p,my_list)