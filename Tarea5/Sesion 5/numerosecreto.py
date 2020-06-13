# -*- coding: utf-8 -*-
"""
Created on Sat May 30 08:26:36 2020

@author: andres
"""

import random

# El modulo logging contiene funciones que ayudan a generar archivos que contienen lineas de "log", usadas para reportar
# acerca del performance del script, potenciales situaciones de error, o inconsistencias que haya encontrado durante la
# ejecucion del mismo.
import logging

# El modulo sys provee acceso a variables internas del interprete
import sys

# Aca importamos los modulos lectura y escritura del paquete de modulos lectura_escritura. Ambos modulos son scripts que se
# encuentran dentro de la carpeta lectura_escritura, que representa el paquete que los contiene.
from lectura_escritura import escritura, lectura
from lectura_escritura.puntuacion import Puntuacion


# Esta sentencia determina parametros opcionales dentro de la libreria de logging. El primer parametro determina el nombre
# de archivo al que se va a escribir el log (por defecto, se escribe a la salida estandar). El segundo parametro determina
# el nivel de logging minimo para que la linea de reporte se escriba al archivo. En este caso, el nivel DEBUG hace que todos
# los mensajes se escriban al log, al ser el nivel minimo.
logging.basicConfig(filename="juego.log", level=logging.DEBUG)


# Funcion principal del juego.
def juego():
    nombre_usuario = input("Ingrese su nombre: ")
    
    numerosecreto = random.randint(rango_inicio, rango_final)
    
    # Esta llamada agrega al log una linea de debugging indicando el numero secreto generado.
    logging.debug("El numero secreto es: " + str(numerosecreto))
    
    numero_intentos = 0
    
    while True:
        intento = input("Ingresar numero: ")
        numero_intentos = numero_intentos + 1
        
        try:
            numero = int(intento)
        except:
             # Esta llamada agrega al log una linea de error indicando que el usuario ingreso un valor invalido.
            logging.error("El usuario escribio un valor invalido: " + intento)
            print("Debe escribir un numero!")
            continue
        
        if numero > numerosecreto:
            print("Mas abajo")
        elif numero < numerosecreto:
            print("Mas arriba")
        else:
            print("Felicidades!\nHa encontrado el numero!")
            break
    
    # Retornamos el nombre y numero de intentos.
    return nombre_usuario, numero_intentos



if __name__ == "__main__":
    # Por medio de la variable sys.argv, es posible manejar los parametros suministrados por medio de la linea de comando.
    # Esta variable es una lista de strings, que contiene el nombre del programa y todos los argumentos suministrados en la linea
    # que lo ejecuto. Es por esto que los parametros pueden recuperarse a partir de la posicion con indice 1 de la lista.
    try:
        # En este caso, el programa tiene 2 parametros obligatorios:
        # los dos extremos del rango que determina el numero secreto
        rango_inicio = int(sys.argv[1])
        rango_final = int(sys.argv[2])
        
        logging.debug("rango inicio: " + str(rango_inicio))
        logging.debug("rango final: " + str(rango_final))
        
        if rango_inicio > rango_final:
            logging.error("Rango inicial es mayor al rango final")
            print("El rango inicial debe ser menor al rango final")
            raise ValueError("Rangos no soportados")
            
        
    except:
         # Si los parametros que se recibe son incorrectos (o no se reciben), se imprimen instrucciones
        print("Para jugar, debe especificar el rango de inicio y final")
        print("Ejemplo: python numerosecreto.py 0 10")
        exit(0)
    
    
    # Cargamos e imprimimos las puntuaciones de los diferentes archivos de puntuaciones
    print("Puntuaciones Texto: ")
    for puntuacion in lectura.lectura_puntuaciones_texto_plano():
        puntuacion.imprimir()
    
    print("Puntuaciones JSON: ")
    for puntuacion in lectura.lectura_puntuaciones_json():
        puntuacion.imprimir()
    
    print("Puntuaciones CSV: ")
    for puntuacion in lectura.lectura_puntuaciones_csv():
        puntuacion.imprimir()
    
    print("Puntuaciones PICKLE: ")
    for puntuacion in lectura.lectura_puntuaciones_pickle():
        puntuacion.imprimir()
        
    nombre, intentos = juego()
    
    # Esta llamada agrega al log una linea de information indicando el resultado del juego.
    logging.debug("Usuario: " + nombre + "|" + str(intentos))
    
    # Creamos un objeto de puntuacion y lo imprimimos
    puntuacion = Puntuacion(nombre, intentos)
    puntuacion.imprimir()
    
    # Guardamos la nueva puntuacion en los diferentes archivos
    escritura.guardar_puntuaciones_texto_plano(puntuacion)
    escritura.guardar_puntuaciones_csv(puntuacion)
    escritura.guardar_puntuaciones_json(puntuacion)
    escritura.guardar_puntuaciones_pickle(puntuacion)

