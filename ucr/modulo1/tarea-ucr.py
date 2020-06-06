class CajeroAutomatico:
    def __init__(self):
        self.denominaciones = (2000, 5000, 10000, 20000)
        self.monto_minimo = min(self.denominaciones)
    
    def multiplo_de_1000(self, monto):
        return bool(monto%1000 == 0)

    def validar_retiro(self, monto):
        retirar_monto_minimo =  monto == self.monto_minimo
        retirar_otro_monto = (
            monto >= self.monto_minimo *2 
            and self.multiplo_de_1000(monto)
            )
        return retirar_monto_minimo or retirar_otro_monto

    def multiplo_de_1000(self, monto):
        return bool(monto%1000 == 0)
    
    def billetes_20mil(self, monto):
        return monto//20000

    def billetes_10mil(self, monto):
        return monto//10000
    
    def billetes_5mil(self,monto):
        return monto//5000

    def billetes_2mil(self,monto):
        return monto//2000

    def calcular_billetes_una_denominacion(self,monto):
        qty_billetes = [
            self.billetes_2mil(monto),
            self.billetes_5mil(monto),
            self.billetes_10mil(monto),
            self.billetes_20mil(monto)
            ]
        return qty_billetes
    
    def dispensar_una_denominacion(self, monto):
        qty_billetes = self.calcular_billetes_una_denominacion(monto)
        resultado = sorted(
            list(zip(self.denominaciones, qty_billetes)),
            reverse=True)

        for result in resultado:
            if result[1] > 0:
                return(result)
                break

    def varias_denominaciones(self,monto):
        print(f'Varias denominaciones: {monto}')

    def determinar_cantidad_billetes(self, monto):
        resultado = []
        for denominacion in self.denominaciones:
            qty_billetes = monto // denominacion
            if (qty_billetes * denominacion == monto
                or monto in self.denominaciones):

                resultado = self.dispensar_una_denominacion(monto)
                break
            else:
                self.varias_denominaciones(monto)
                break
        print(resultado)

    def dispensar_dinero(self, monto):
        if self.validar_retiro(monto):
            self.determinar_cantidad_billetes(monto)
        else:
            print('Este cajero unicamente cuentas con billetes de:')
            print(self.denominaciones)

cajero = CajeroAutomatico()
cajero.dispensar_dinero(5000)