from numpy import zeros
n=int(input('n='))
xss=zeros((n),dtype=float)
yss=zeros((n),dtype=float)
xdj=zeros((n),dtype=float)
ydj=zeros((n),dtype=float)
for i in range(0, n):
 print('XSS[', i ,']=')
 xss[i]=eval(input())
 print('YSS[', i ,']=')
 yss[i]=eval(input())
 print('XDJ[', i ,']=')
 xdj[i]=eval(input())
 print('YDJ[', i ,']=')
 ydj[i]=eval(input())
xst=xss[0]
ysus=yss[0]
xdr=xdj[0]
yjos=ydj[0]
for i in range(1, n):
 if xst < xss[i]:
     xst=xss[i]
 if ysus>yss[i]:
     yst=yss[i]
 if xdr>xdj[i]:
     xdr=xdj[i]
 if yjos<ydj[i]:
   yjos=ydj[i]
if((xdr<xst) or (yjos>ysus)):
    print('Intersectie vida')
else :
    print('Aria suprafetei este: ',(xdr-xst)*(ysus-yjos))