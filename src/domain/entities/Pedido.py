from datetime import datetime
import uuid
from typing import List
from value_objects.Direccion import Direccion
from value_objects.TotalPedido import TotalPedido
from value_objects.EstadoPedido import EstadoPedido


class Pedido:
    def __init__(self,
                 id_cliente: str,
                 direccion_entrega: Direccion,
                 id_items: List[str]):
        
        self.id: str = str(uuid.uuid4())
        self.id_cliente: str = id_cliente
        self.direccion_entrega: Direccion = direccion_entrega
        self.id_items: List[str] = id_items
        self.estado_pedido: EstadoPedido = EstadoPedido.CREADO
        self.fecha_creacion: datetime = datetime.now()
        self.fecha_ultima_actualizacion: datetime = self.fecha_creacion
        self.total_pedido: TotalPedido = TotalPedido(0.0)

    def actualizar_total_pedido(self, total_pedido: TotalPedido):
        self.total_pedido = total_pedido