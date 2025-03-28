from Producto import Producto
from decimal import Decimal
from datetime import datetime

import uuid

class ItemPedido:
    def __init__(self,producto: Producto, cantidad: int):
        self.id: str = str(uuid.uuid4())
        self.producto: Producto = producto
        self.cantidad: int = cantidad
        self.subtotal: Decimal = producto.precio * cantidad
        self.fecha_creacion: datetime = datetime.now()