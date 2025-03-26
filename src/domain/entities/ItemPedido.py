from Producto import Producto
from value_objects.Descuento import Descuento
from decimal import Decimal

import uuid

class ItemPedido:
    def __init__(self,producto, cantidad, descuento):
        self.id: str = str(uuid.uuid4())
        self.producto: Producto = producto
        self.cantidad: int = cantidad
        self.descuento: Descuento = descuento

    def calcular_subtotal(self):
        return self.cantidad * self.producto.precio
    
    def calcular_total(self):
        return self.calcular_subtotal()* (1 - self.descuento.valor)