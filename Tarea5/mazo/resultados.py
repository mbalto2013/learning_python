from datetime import datetime
import os
import pickle

ARCHIVO_PICKLE = 'resultados.pickle'
class Resultado:
    def __init__(self,fecha, jugador, puntos):
        self.fecha = fecha 
        self.jugador = jugador
        self.puntos = puntos

    def informacion(self):
        str_fecha = datetime.strftime(self.fecha, '%d/%m/%Y %H:%M:%S')
        return(f'{str_fecha} - {self.jugador} {self.puntos}pts') 

def guardar_resultados(lista_resultados):
    try:
        with open(ARCHIVO_PICKLE, 'rb') as archivo:
            resultados = pickle.load(archivo)
    except:
        resultados = { 'resultados': [] }
        resultados['resultados'].append(lista_resultados)
            
    with open(ARCHIVO_PICKLE, 'wb') as archivo:
        pickle.dump(lista_resultados, archivo)

def cargar_resultados():
    lista_resultados = []
    if not os.path.exists(ARCHIVO_PICKLE):
        return lista_resultados
    with open(ARCHIVO_PICKLE, 'rb') as archivo:
        resultados = pickle.load(archivo)
        lista_resultados = resultados
    return resultados
