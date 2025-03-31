from domain.entities.Producto import Producto
from decimal import Decimal
from datetime import datetime

import uuid

class ItemPedido:
    def __init__(self,id_producto: str, cantidad: int):
        self.id: str = str(uuid.uuid4())
        self.id_producto: str = id_producto
        self.cantidad: int = cantidad
        self.fecha_creacion: datetime = datetime.now()