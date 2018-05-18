import math
import random

def uniforme(a,b):
    x=0
    y=0
    y=random()/32767.0
    x=y*(b-a)+a
    return x

def exponencial(m):
    x=0
    y=0
    y=uniforme(0,1)
    x=-1*m*math.log(1-y)
    return x

def erlang(k,m):
    x=0
    me=m/k
    for i in range(1, k+1):
        x+=exponencial(me)
    return x

def normal(m,v):
    i=0
    x=0
    z=0
    sum=0
    for i in range(1,13):
        sum+=uniforme(0,1);
    z=sum - 6
    x=sqrt(v)*z+m
    return x

def geometrica(p):
    x=1
    f=0
    s=0
    y=0
    f=p
    s=f
    y=uniforme(0,1)
    while y > s:
        f=f*(1-p)
        s+=f
        x+=1
    return x

def poisson(lam):
    x=0
    f=0
    s=0
    y=0
    f=math.exp(-1*lam)
    s=f
    y=uniforme(0,1)
    while y > s:
        f=(f*lam)/x+1
        s+=f
        x+=1
    return x

def binomial(n,p):
    x=0
    f=math.exp(n*math.log(1-p))
    s=f
    y=uniforme(0,1)
    while y > s:
        f = f*p*(n-x)/((x+1)*(1-p))
        s+=f
        x+=1
    return x

def aleatoria(tipo,par1,par2):
    x=0
    switcher = {
        0: x=poisson(par1),break
        1: x=erlang(tipo,par1),break
        2: x=erlang(tipo,par1),break
        3: x=erlang(tipo,par1),break
        4: x=erlang(tipo,par1),break
        5: x=erlang(tipo,par1),break
        6: x=erlang(tipo,par1),break
        7: x=erlang(tipo,par1),break
        8: x=erlang(tipo,par1),break
        9: x=erlang(tipo,par1),break
        10: x=normal(par1,par2),break
        11: x=binomial(par1,par2),break
        12: x=uniforme(par1,par2),break
        13: x=geometrica(par1),break
    return x
    }

def main():
    i=1
    x=0
    for i in range(1,11):
        x=aleatoria(11,10,0.1)
        print("%f\n", x)


if __name__ == '__main__':
    main()
