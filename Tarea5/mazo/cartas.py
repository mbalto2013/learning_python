import random 
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def informacion(self):
        return f'{self.valor} de {self.palo}'

    def crear_mazo(self):
        lista_valores = [ valor for valor in range(2, 15)]
        lista_palos = ['Espadas', 'Corazones', 'Diamantes', 'Flores' ]
        mazo = []
        for palo in lista_palos:
            for valor in lista_valores:
                mazo.append((valor,palo))
        return mazo
    
    def revolver_mazo(self, mazo):
        random.shuffle(mazo)
        return(mazo) 

    def sacar_cartas(self,mazo, numero_de_cartas):
        cartas_seleccionadas = mazo[0:numero_de_cartas]
        cartas_no_seleccionadas = mazo[numero_de_cartas +1 : -1]
        return((cartas_seleccionadas, cartas_no_seleccionadas))
