from numpy import zeros
CNP=zeros((13),dtype=int)
SC=zeros((12),dtype=int)
print("Dati cifrele CNP-ului")
for i in range (0,13):
 print('CNP[',i,']= ', end=' ')
 CNP[i]=eval(input())
print("CNP-ul este",CNP)
S=0
SC[0],SC[1],SC[2],SC[3],SC[4],SC[5]=2,7,9,1,4,6
SC[6],SC[7],SC[8],SC[9],SC[10],SC[11]=3,5,8,2,7,9
for i in range (0,12):
  S=S+CNP[i]*SC[i]
R=S%11
if ((R == 10) and (CNP[12] == 1))or((R<10) and CNP[12]==R):
     print("CNP corect")
else:
     print("CNP incorect")