import random 

LISTA_PALOS = ['Espadas', 'Corazones', 'Diamantes', 'Flores' ]
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def informacion(self):
        return f'{self.valor} de {self.palo}'

    def get_valor(self):
        return self.valor

    def get_palo(self):
        return self.palo

def crear_mazo():
    lista_valores = [ valor for valor in range(2, 15)]
    mazo = []
    for palo in LISTA_PALOS:
        for valor in lista_valores:
            mazo.append(Carta(valor,palo))
    return mazo
    
def revolver_mazo(mazo):
    random.shuffle(mazo)
    return(mazo) 

def criterio_de_orden(s):
    return s[0]

def sacar_cartas(lista_de_cartas, numero_de_cartas):
    cartas_seleccionadas = []
    while numero_de_cartas !=0:
        cartas_seleccionadas.append(lista_de_cartas.pop())
        numero_de_cartas = numero_de_cartas -1
    return(cartas_seleccionadas)

    #return((cartas_seleccionadas,lista_de_cartas))



