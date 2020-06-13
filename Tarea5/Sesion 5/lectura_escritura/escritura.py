# -*- coding: utf-8 -*-

import logging

logging.basicConfig(filename="escritura.log", level=logging.DEBUG)

# Archivos binarios que contienen estructuras de datos de Python. 
# Es necesario leerlos desde python con la libreria picke
import pickle

# Archivos separados por coma. Son similares a las tablas cada coma separa un valor
# y cada cambio de linea es una fila nueva
import csv

# json JavaScript Object Notation. 
import json


# os nos permite utilizar funciones relacionadas el Systema operativo en el 
# que corremos, por ejemplo para concatenar paths de sistema de archivo
# o revisar si un archivo existe o no
import os


# Texto plano 
# no ocupa ningun import

# Definimos el directorio donde se van a guardar las puntuaciones
# Hay que reemplazar este path para que funcione en sus computadoras
# debido a que el path debe de existir en sus computadoras para que funcione
DIRECTORIO = 'C:/Users/andre/Sesion 5/puntuaciones'

# Nombres de cada archivo
ARCHIVO_TEXTO_PLANO = "puntuacion.txt"
ARCHIVO_CSV = "puntuacion.csv"
ARCHIVO_JSON = "puntuacion.json"
ARCHIVO_PICKLE = "puntuacion.pickle"

# open(DIR, ACCESS)
# DIR: Direccion a donde esta el archivo que queremos abrir
# ACCESS: El tipo de acceso con el que queremos abrir el archivo
#     'r': lectura
#     'w': escritura
#     'rw': lectura escritura
#     'w+': escritura concatenada
#     'rb'/'wb': lectura/escritura binaria 


# file = open(ARCHIVO_TEXTO_PLANO, 'w')
# file.writelines(['a', 'b', 'c'])
# file.close()

# with open(ARCHIVO_TEXTO_PLANO, 'w') as file:
#     file.writelines(['a', 'b', 'c'])

# with open(ARCHIVO_TEXTO_PLANO, 'r') as file:
#     texto = file.readlines()
#     for linea in texto:
#         print(linea.replace('\n', ''))



def guardar_puntuaciones_texto_plano(puntuacion):
    path_completo = os.path.join(DIRECTORIO, ARCHIVO_TEXTO_PLANO)
    logging.debug("Escribiendo a archivo: " + path_completo)
    with open(path_completo, 'a') as archivo:
        archivo.writelines(puntuacion.nombre + " " + str(puntuacion.intentos) + "\n")



def guardar_puntuaciones_csv(puntuacion):
    path_completo = os.path.join(DIRECTORIO, ARCHIVO_CSV)
    logging.debug("Escribiendo a archivo: " + path_completo)
    with open(path_completo, 'a') as archivo:
        csv_writer = csv.writer(archivo)
        csv_writer.writerow([puntuacion.nombre, puntuacion.intentos])


def guardar_puntuaciones_json(puntuacion):
    path_completo = os.path.join(DIRECTORIO, ARCHIVO_JSON)
    logging.debug("Escribiendo a archivo: " + path_completo)
    
    # Si el archivo no existe hay que crear una variable vacia
    # para evitar el error de que el json no existe
    try:
        with open(path_completo, 'r') as archivo:
            puntuaciones = json.load(archivo)
    except:
        puntuaciones = {
            "puntuaciones": []
        }
    
    puntuaciones['puntuaciones'].append({
        'nombre': puntuacion.nombre,
        'intentos': puntuacion.intentos
    })
    
    with open(path_completo, 'w') as archivo:
        json.dump(puntuaciones, archivo)


def guardar_puntuaciones_pickle(puntuacion):
    path_completo = os.path.join(DIRECTORIO, ARCHIVO_PICKLE)
    logging.debug("Escribiendo a archivo: " + path_completo)
    
    # Si el archivo no existe hay que crear una variable vacia
    # para evitar el error de que el pickle no existe
    try:
        with open(path_completo, 'rb') as archivo:
            puntuaciones = pickle.load(archivo)
    except:
        puntuaciones = {
            "puntuaciones": []
        }
    
    puntuaciones['puntuaciones'].append({
        'nombre': puntuacion.nombre,
        'intentos': puntuacion.intentos
    })
    
    with open(path_completo, 'wb') as archivo:
        pickle.dump(puntuaciones, archivo)