def penultim_secund(sir):
    print(sir[0]+sir[-2]+sir[2:len(sir)-2]+sir[1]+sir[-1])
sir=str(input('sir='))
print(penultim_secund(sir))