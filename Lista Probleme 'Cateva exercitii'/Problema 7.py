def determine_type_of_triangle(laturilor_triunghi, area):
    if laturilor_triunghi[0] == laturilor_triunghi[1] and laturilor_triunghi[0] ==laturilor_triunghi[2]:
        print('echilateral')

    elif ((laturilor_triunghi[0] * laturilor_triunghi[1]) / 2 == area or
        (laturilor_triunghi[0] * laturilor_triunghi[2]) / 2 == area or
        (laturilor_triunghi[2] * laturilor_triunghi[1]) / 2 == area)and\
        (laturilor_triunghi[0]==laturilor_triunghi[1]
         or laturilor_triunghi[0] ==laturilor_triunghi[2] or
         laturilor_triunghi[1] == laturilor_triunghi[2]) :
        print('triunghiului  dreptunghic isoscel')
    elif (laturilor_triunghi[0] == laturilor_triunghi[1]
          or laturilor_triunghi[0] == laturilor_triunghi[2] or
          laturilor_triunghi[1] == laturilor_triunghi[2]):
        print('isoscel')

    elif (laturilor_triunghi[0]*laturilor_triunghi[1])/2 == area or\
        (laturilor_triunghi[0]*laturilor_triunghi[2])/2 == area or\
        (laturilor_triunghi[2]*laturilor_triunghi[1])/2 == area:
        print("triunghiului  dreptunghic")
    else:
        print('oarecare ')


def my_function(laturilor_triunghi):
    s = (laturilor_triunghi[0] + laturilor_triunghi[1] + laturilor_triunghi[2]) / 2
    area = (s * (s - laturilor_triunghi[0]) * (s - laturilor_triunghi[1]) * (s - laturilor_triunghi[2])) ** 0.5
    print('area =', area)
    inaltimilor_triunghiului=[]
    for i in range(0, 3):
        inaltimilor_triunghiului.append((2 * area) / laturilor_triunghi[i])
        print(inaltimilor_triunghiului[i], end=' ')
    print('\n')
    if __name__ == '__main__':
        determine_type_of_triangle(laturilor_triunghi, area)


laturilor_triunghi=[]
for i in range(0,3):
    print('laturilor triunghi', i+1, '=',end=' ')
    laturilor_triunghi.append(float(input()))
if __name__ == '__main__':
    my_function(laturilor_triunghi)