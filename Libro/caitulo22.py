## los operadores +,-,*, potencia, /, //, %, < pueden tener un significado no explicito
# ejemplo: Lo ideal es crear una nuevo objeto cada vez que invoquemos
# dichos operadores en una clase
# estos se usan para extender aritmeticamente nuestras clases

class Quantity:
    def __init__(self, value=0):
        self.value = value
    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)
    def __sub__(self,other):
        new_value = self.value - other.value
        return Quantity(new_value)
    def __str__(self):
        return 'Quantity[' + str(self.value) + ']'



q1 = Quantity(5)
q2 = Quantity(10)
print('qi =', q1, ', q2 =', q2)

q3 = q1 + q2
print('q3=', q3)
print(type(q3))


"""
Note that we have made the class Quantity immutable; that is once a Quantity instance has been created its value cannot be changed (it is fixed).
This means that when two quantities are added tougher a new instance of the class Quantity is created. This is analogous to how integers work, if you add together 2 + 3 then you get 5; neither 2 or 3 are modified however; instead a new integer 5 is generated—this is an example of the general design principle; developers should follow the semantics of built in types; Quantity objects act like number objects.


Operator
Expression
Method

Addition
q1 + q2
__add__(self, q2)

Subtraction
q1 – q2
__sub__(self, q2)


Multiplication
q1 * q2
__mul__(self, q2)


Power
q1 ** q2
__pow__(self, q2)


Division
q1 / q2
__truediv__(self, q2)


Floor Division
q1 // q2
__floordiv__(self, q2)


Modulo (Remainder)
q1 % q2
__mod__(self, q2)


Bitwise Left Shift
q1 ≪ q2
__lshift__(self, q2)


Bitwise Right Shift
q1 ≫ q2
__rshift__(self, q2)


Less than
q1 < q2
__lt__(q1, q2)


Less than or equal to
q1 <= q2
__le__(q1, q2)


Equal to
q1 == q2
__eq__(q1, q2)


Not Equal to
q1 != q2
__ne__(q1, q2)


Greater than
q1 > q2
__gt__(q1, q2)


Greater than or equal to
q1 >= q2
__ge__(q1, q2)



AND
q1 & q2
__and__(q1, q2)


OR
q1 | q2
__or__(q1, q2)


XOR
q1 ^ q2
__xor__(q1, q2)


NOT
~q1
__invert__()

"""