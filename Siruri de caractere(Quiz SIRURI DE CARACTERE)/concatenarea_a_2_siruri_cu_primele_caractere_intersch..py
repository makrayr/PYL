def concatenare(prim,doi):
    tmp_prim=doi[0]+prim[1:]
    tmp_doi=prim[0]+doi[1:]
    print(tmp_prim +' '+tmp_doi)
sir1=str(input('sir1='))
sir2=str(input('sir2='))
print(concatenare(sir1,sir2))