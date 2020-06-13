"""

resultados.py: Este modulo debe contener los siguientes atributos:
Una clase Resultado con los atributos fecha (datetime), jugador (str) y puntos (int),
 y un metodo imprimir que imprima la informacion contenida en el objeto.
Una funcion guardar_resultados que almacene dentro de un archivo pickle una lista de objetos Resultado.
Una funcion cargar_resultados que extraiga de un archivo pickle una lista de objetos Resultado.
"""
from datetime import datetime
import os
import pickle

class Resultado:
    def __init__(self,fecha, jugador, puntos):
        self.fecha = fecha 
        self.jugador = jugador
        self.puntos = puntos

    def informacion(self):
        str_fecha = datetime.strftime(self.fecha, '%d/%m/%Y %H:%M:%S') 
        return {
            'fecha': str_fecha,
            'jugador': self.jugador,
            'puntos' : self.puntos
            }
    def guardar_resultados(self):
        directorio = '/tmp/'
        nombre_archivo_pickle = 'resultados.pickle'
        path_archivo_pickle = os.path.join(directorio, nombre_archivo_pickle)
        try:
            with open(path_archivo_pickle, 'rb') as archivo:
                resultados = pickle.load(archivo)
        except:
            resultados = { 'resultados': [] }
            resultados['resultados'].append(self.informacion())
            
            with open(path_archivo_pickle, 'wb') as archivo:
                pickle.dump(resultados, path_archivo_pickle)

Resultado1 = Resultado(datetime.now(),'Milton', 30)
Resultado2 = Resultado(datetime.now(),'Milton', 30)
Resultado3 = Resultado(datetime.now(),'Milton', 30)
Resultado1.guardar_resultados()