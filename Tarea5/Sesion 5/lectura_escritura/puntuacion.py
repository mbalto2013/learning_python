# -*- coding: utf-8 -*-

# Esta es una definicion de clase para la clase Puntuacion.
# Una instancia de la clase tiene un nombre de jugador y una puntuacion.
# Ademas de un metodo sencillo para imprimirlo.
class Puntuacion:
    def __init__(self, nombre, intentos):
        self.nombre = nombre
        self.intentos = intentos
    
    def imprimir(self):
        print(self.nombre + " | " + str(self.intentos))