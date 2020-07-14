class Persona:
    def __init__(self, cedula: int, nombre: str, fecha_nacimiento: str,
                 peso: float, altura: float) -> None:
        self.cedula = cedula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.altura = altura

    @property
    def cedula(self):
        return self.cedula

    @cedula.setter
    def cedula(self, numero_cedula: int) -> None:
        if 777777777 > numero_cedula > 1:
            self.__cedula = numero_cedula
        else:
            raise CedulaInvalidaException(numero_cedula)

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, new_nombre: str) -> None:
        if new_nombre.isalpha():
            self.__nombre = new_nombre

    @property
    def fecha_nacimiento(self):
        return self.fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, new_fecha_nacimiento: str) -> None:
        self.__fecha_nacimiento = new_fecha_nacimiento

    @property
    def peso(self):
        return self.peso

    @peso.setter
    def peso(self, new_peso: float) -> None:
        if 400 > new_peso > 2:
            self.__peso = new_peso

    @property
    def altura(self):
        return self.altura

    @altura.setter
    def altura(self, new_altura: float) -> None:
        if 400 > new_altura > 25:
            self.__altura = new_altura

    @property
    def _condicion(self) -> str:
        if self.__peso > 200:
            print('Problema serio de salud')
        else:
            print('Estas bien de salud! :D')


class CedulaInvalidaException(Exception):
    """ cedula invalida. Debe ser un  valor > 0 y < 777777777"""

    def __init__(self):
        pass

    def __str__(self):
        return f'Cedula invalida, debe proveer un numero > 0 y < 777777777'


try:
    Milton = Persona(777777778, 'Milton', '12/31/999', 222, 444)
except CedulaInvalidaException:
    print('revise')