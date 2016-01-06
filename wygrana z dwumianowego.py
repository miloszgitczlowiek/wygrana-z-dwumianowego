import math
import numpy as np

f=math.factorial

def bin1(n):
    return f(40)/f(n)/f(40-n)*0.7**n*0.3**(40-n)
     
P=[]
for i in range(40):
    P.append(bin1(i+1))

n=int(input('Podaj liczbe rund: '))

for i in range(1,n+1):
    
    x=np.random.binomial(40,0.7)
    print('Runda nr: {0}\nProponowana wygrana to: {1} \nPozostalo {2} rund.'.format(i,x,n-i))
    
    if n-i==0:
        break
    
    t1=0.0
    t2=0.0
    for a in range(n-i-1):
        t1+=np.cumsum(P)[27]**a
    for a in range(29,41):
        t2+=a*P[a-1]
    ex=t1*t2+28*np.cumsum(P)[27]**(n-i-1)
    
    print('Wartosc oczekiwana wygranej w nastepnych rundach to: {0} \n'.format(ex))
    
    if x>ex:
        break
    
print('Gra zakonczona z wygrana = {0}'.format(x))


