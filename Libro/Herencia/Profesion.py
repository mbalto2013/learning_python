from Persona import *


class Profesion(Persona):
    def __init__(self, cedula, nombre, fecha_nacimiento,
                 peso, altura, profesion):
        super().__init__(cedula, nombre, fecha_nacimiento, peso, altura)
        self.profesion = profesion

    @property
    def profesion(self) -> str:
        return self.profesion

    @profesion.setter
    def profesion(self, new_profesion: str):
        if new_profesion.isalpha():
            self.__profesion = new_profesion


ingeniero_milton = Profesion(
    cedula=101250252,
    nombre='Lucas',
    fecha_nacimiento='12/09/1999',
    peso=170,
    altura=180,
    profesion='Arquitecto')
