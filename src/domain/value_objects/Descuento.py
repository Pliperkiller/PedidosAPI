import decimal

class Descuento:
    def __init__(self, nombre: str, valor: decimal):
        self.nombre = nombre
        self.valor = valor

    def __str__(self):
        return f'Descuento: {self.nombre} {self.valor}'