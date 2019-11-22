def inloc_fara_prima_aparitie(sir,car):
    p_index = sir.find(car)
    print(sir[:p_index+1]+sir[p_index+1:].replace(car,'*'))
sir = str(input('sir='))
caracter = str(input('caracter='))
print(inloc_fara_prima_aparitie(sir,caracter))