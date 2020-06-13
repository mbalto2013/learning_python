# -*- coding: utf-8 -*-

import logging

logging.basicConfig(filename="lectura.log", level=logging.DEBUG)

# Archivos binarios que contienen estructuras de datos de Python. 
# Es necesario leerlos desde python con la libreria picke
import pickle

# Archivos separados por coma. Son similares a las tablas cada coma separa un valor
# y cada cambio de linea es una fila nueva
import csv

# json JavaScript Object Notation. 
import json

import os

from lectura_escritura.puntuacion import Puntuacion

# Texto plano 
# no ocupa ningun import

DIRECTORIO = 'C:/Users/andre/Sesion 5/puntuaciones'

ARCHIVO_TEXTO_PLANO = "puntuacion.txt"
ARCHIVO_CSV = "puntuacion.csv"
ARCHIVO_JSON = "puntuacion.json"
ARCHIVO_PICKLE = "puntuacion.pickle"


def lectura_puntuaciones_texto_plano():
    path_completo = os.path.join(DIRECTORIO, ARCHIVO_TEXTO_PLANO)
    logging.debug("Leyendo archivo: " + path_completo)
    lista_puntuaciones = []
    
    # Revisamos si el archivo no existe aun, retornamos una lista vacia
    if not os.path.exists(path_completo):
        return lista_puntuaciones
    
    with open(path_completo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            lista_linea = linea.split()
            nombre = lista_linea[0]
            intentos = int(lista_linea[1].replace('\n', ''))
            lista_puntuaciones.append(Puntuacion(nombre, intentos))
    return lista_puntuaciones


def lectura_puntuaciones_csv():
    path_completo = os.path.join(DIRECTORIO, ARCHIVO_CSV)
    logging.debug("Leyendo archivo csv: " + path_completo)
    lista_puntuaciones = []
    
    # Revisamos si el archivo no existe aun, retornamos una lista vacia
    if not os.path.exists(path_completo):
        return lista_puntuaciones
    
    with open(path_completo, 'r') as archivo:
        csv_reader = csv.reader(archivo)
        for linea in csv_reader:
            logging.debug("Linea: " + str(linea))
            try:
                nombre = linea[0]
                intentos = int(linea[1])
                lista_puntuaciones.append(Puntuacion(nombre, intentos))
            except IndexError:
                # El error ocurria cuando habia una linea vacia 
                # esto causaba que el linea[0] y linea[1] estuviera fuera
                # de los valores validos
                logging.error("Linea vacia")
    return lista_puntuaciones


def lectura_puntuaciones_json():
    path_completo = os.path.join(DIRECTORIO, ARCHIVO_JSON)
    logging.debug("Leyendo archivo: " + path_completo)
    lista_puntuaciones = []
    
    # Revisamos si el archivo no existe aun, retornamos una lista vacia
    if not os.path.exists(path_completo):
        return lista_puntuaciones
    
    
    with open(path_completo, 'r') as archivo:
        puntuaciones = json.load(archivo)
        for puntuacion in puntuaciones["puntuaciones"]:
            nombre = puntuacion["nombre"]
            intentos = puntuacion["intentos"]
            lista_puntuaciones.append(Puntuacion(nombre, intentos))
    
    return lista_puntuaciones


def lectura_puntuaciones_pickle():
    path_completo = os.path.join(DIRECTORIO, ARCHIVO_PICKLE)
    logging.debug("Leyendo archivo: " + path_completo)
    lista_puntuaciones = []
    
    # Revisamos si el archivo no existe aun, retornamos una lista vacia
    if not os.path.exists(path_completo):
        return lista_puntuaciones
    
    
    with open(path_completo, 'rb') as archivo:
        puntuaciones = pickle.load(archivo)
        for puntuacion in puntuaciones["puntuaciones"]:
            nombre = puntuacion["nombre"]
            intentos = puntuacion["intentos"]
            lista_puntuaciones.append(Puntuacion(nombre, intentos))
    
    return lista_puntuaciones
