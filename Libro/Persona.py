class Persona:
    def __init__(self, ssn: int, name: str, dob: str,
                 weight: float, height: float) -> None:
        self.ssn = ssn
        self.name = name
        self.dob = dob
        self.weight = weight
        self.height = height

    @property
    def ssn(self):
        return self.ssn

    @ssn.setter
    def ssn(self, new_ssn: int) -> None:
        if 999999999 > new_ssn > 1:
            self.__ssn = new_ssn

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name: str) -> None:
        if new_name.isalpha():
            self.__name = new_name

    @property
    def dob(self):
        return self.dob

    @dob.setter
    def dob(self, new_dob: str) -> None:
        self.__dob = new_dob

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, new_weight: float) -> None:
        if 400 > new_weight > 2:
            self.__weight = new_weight

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, new_height: float) -> None:
        if 400 > new_height > 25:
            self.__height = new_height

    @property
    def _condicion(self) -> str:
        if self.__weight > 200:
            print('Problema serio de salud')
        else:
            print('Estas bien de salud! :D')
