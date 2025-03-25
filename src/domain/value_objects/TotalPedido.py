import decimal

class TotalPedido:
    def __init__(self, subtotal: decimal, impuestos: decimal = None, descuentos: decimal = None):
        self.subtotal = subtotal
        self.impuestos = impuestos
        self.descuentos = descuentos
        self.total = self.calcular_total()

    def calcular_total(self):
        return self.subtotal + self.impuestos - self.descuentos
    
    def __str__(self):
        return f'Total Pedido: {self.subtotal} {self.impuestos} {self.descuentos} {self.total}'