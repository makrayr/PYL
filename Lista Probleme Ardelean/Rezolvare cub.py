from math import *
lc=float(input("lc="))
atot=6*(lc**2)
vol=lc**3
asfera=atot
rsfera1=sqrt(asfera/(4*pi))
volsf=vol
rsfera2=(3*volsf)/(4*pi)
rsfera2**=1/3
print('Solutia la pct a este: ',rsfera1)
print('Solutia la pct b este: ',rsfera2)