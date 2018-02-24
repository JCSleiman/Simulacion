import numpy as np
import random
n = 100
a = 20.00
b = 30.00
muestra = np.random.uniform(low=a, high=30.0001, size=100)
suma = 0
for number in muestra:
    suma+=number
media = suma/muestra.size
print(muestra)

def func(media):
    muestra = np.random.uniform(low=0, high=10.0001, size=100)
    foo = x / 50
    for num in muestra:
        y = num
        x = np.sqrt(100*y)
        return x

#Media analitica Real
def MediaAnalitica(a, b):
    MA = (a+b)/2
    return MA
#Varianza analitica Real
def VarianzaAnalitica(a, b):
    VA = ((b-a)**2)/12
    return VA

#Media muestral
def MediaMuestral(a, muestra):

    suma = 0
    media = 0
    for number in muestra:
        suma+=number
    media = suma/muestra.size
    #print("Este es la media/promedio: " + str(media))
    return media

#Varianza Muestral
def VarianzaMuestral(a, muestra):
    #print("Revisando VarianzaMuestral")
    s=0
    suma = 0
    up = 0    #up es la parte de arriba de la formula de Varianza Muestral (La sumatoria de (xi - x testada)**2)
    p = 0    #p = a cada valor de mi lista menos la media
    pL =[]       #PL serían los indexes de xi - x testada
    sqdL = []    # sqL será la lista que almacene los squared
    #print("media VM = " + str(media))
    for number in muestra:
        #creo que hay un problema en la p
        p = (number) - (media)
        pL.append(p)

        sqdL.append(p**2)
    for number in sqdL:
        up += number

    #Calculando la Varianza
    varianza = up/(len(muestra)-1)
    #Desviación std
    stddev = varianza ** (0.5)
    return varianza

#Llamando la MediaMuestral
MA = MediaAnalitica(a,b)
MM = MediaMuestral(a, muestra)
VA = VarianzaAnalitica(a,b)
VM = VarianzaMuestral(a, muestra)
#foo = func(media, muestra)
print("Media Analitica: ",MA)
print("Media Muestral: ",MM)
print("Varianza Analitica: ",VA)
print("Varianza Muestral: ",VM)
#print("Foo: ", foo)
