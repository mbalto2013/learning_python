from Persona import *


class Profesion(Persona):
    def __init__(self, ssn, name, dob, weight, height, profession):
        super().__init__(ssn, name, dob, weight, height)
        self.profession = profession

    @property
    def profession(self) -> str:
        return self.profession

    @profession.setter
    def profession(self, new_profession: str):
        if new_profession.isalpha():
            self.__profession = new_profession

ingeniero_milton = Profesion(
    ssn=701860575,
    name='Milton',
    dob='06/09/1988',
    weight=180,
    height=183,
    profession='Engineer')
