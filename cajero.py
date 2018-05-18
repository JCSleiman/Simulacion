reloj=0
nEventos=0
nLlegadas=0
cajero=True
fila = []
def Abrir():
    #Actualizar reloj


    #incrementar contador de numero de eventos
    nEventos+=1

    #poner el estatus en abierto
    status='Abierto'

    #Generar Evento llegada en el tiempo Reloj + Aleatorio de tiempo entre llegadas


    #Desplegar evento en su caso


def Cerrar():
    #Actualizar reloj

    #incrementar contador de numero de eventos
    nEventos+=1

    #Poner Estatus Cerrado
    status="Cerrado"

    #Desplegar evento en su caso

def LlegadaCliente():
    #Actualizar reloj

    #Incrementar contador de numero de eventos
    nEventos=1

    #Incrementar numero de llegadas
    nLlegadas+=1

    #Si estatus abierto, Generar Evento llegada en el tiempo Reloj ´Aleatorio de tiempo entre llegadas
    if status=="Abierto":
        pass
    if Cajero==True and status =="Abierto":
        if nLlegadas < 8:
            #agregar clente a lista alimentando numero de llegada y tiempo de llegada
            fila.append(nLlegadas)
            #incrementar numero de clienteses en el sistema
            nLlegadas+=1
            if Cajero==False
