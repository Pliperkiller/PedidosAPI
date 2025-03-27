from datetime import datetime
import uuid
from typing import List, Optional
from value_objects.Direccion import Direccion
from value_objects.TotalPedido import TotalPedido
from value_objects.EstadoPedido import EstadoPedido




class Pedido:
    def __init__(self,id_cliente,direccion_entrega):
        self.id: str = str(uuid.uuid4())
        self.id_cliente: str = id_cliente
        self.id_items: List[str] = None
        self.estado_pedido: EstadoPedido = EstadoPedido.CREADO
        self.fecha_creacion: datetime = datetime.now()
        self.fecha_ultima_actualizacion: datetime = self.fecha_creacion 
        self.direccion_entrega: Direccion = direccion_entrega
        self.total_pedido: TotalPedido = None