def mari_mici(a):
    contor = 0
    for letter in a:
        if letter.upper() == letter:
            contor += 1
    if contor >= len(a) / 4:
        for char in a:
            if char.upper() == char:
                print(char.lower(), end = '')
            else:
                print(char.upper(), end = '')
    else:
        print(a)

a=str(input('a='))
print(mari_mici(a))