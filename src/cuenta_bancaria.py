class CuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo):
        
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
        self.tipoInteres = 1.5


    def getTitular(self):
        return self.titular

    def setTitular(self, titular):
        self.titular = titular

    def getNumeroCuenta(self):
        return self.numeroCuenta

    def getSaldo(self):
        return self.saldo

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"El número ingresado es {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a ingresar debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No se puede retirar más saldo del actual en la cuenta.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
        else:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad}. Saldo actual: {self.saldo}")

    def calcularInteres(self):
        saldo_con_interes = self.saldo + (self.saldo * self.tipoInteres / 100)
        return saldo_con_interes

    def setTipoInteres(self, tipoInteres):
        if 0 <= tipoInteres <= 10:
            self.tipoInteres = tipoInteres
            print(f"El nuevo tipo de interés  es: {self.tipoInteres}%")
        else:
            print("El tipo de interés debe estar entre 0% y 10%.")

cuenta = CuentaBancaria("Laura Correa", "00012345", 10000.0)

print(cuenta.getTitular())  
cuenta.setTitular("Andrea Duarte")  
print(cuenta.getTitular())  

print(cuenta.getNumeroCuenta())  
print(cuenta.getSaldo())  

cuenta.ingresar(2000)  
cuenta.retirar(500)  
print(f"El saldo con interés aplicado: {cuenta.calcularInteres()}") 

cuenta.setTipoInteres(2.8) 
cuenta.setTipoInteres(11)
