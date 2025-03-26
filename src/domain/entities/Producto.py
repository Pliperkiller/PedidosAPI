from decimal import Decimal
import uuid

class Producto:
    def __init__(self, nombre, precio):
        self.id: str = str(uuid.uuid4())
        self.nombre: str = nombre
        self.precio: Decimal = precio

    def __str__(self):
        return f'Producto: {self.id} {self.nombre} {self.precio} {self.stock}'