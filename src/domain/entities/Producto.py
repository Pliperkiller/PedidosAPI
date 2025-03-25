import decimal

class Producto:
    def __init__(self, id: int, nombre: str, precio: decimal, stock: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f'Producto: {self.id} {self.nombre} {self.precio} {self.stock}'