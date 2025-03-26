from datetime import datetime
import uuid

from ItemPedido import ItemPedido
from Cliente import Cliente
from value_objects.Direccion import Direccion
from value_objects.TotalPedido import TotalPedido



class Pedido:
    def __init__(self,cliente,items,direccion_entrega,total_pedido):
        self.id: str = str(uuid.uuid4())
        self.cliente: Cliente = cliente
        self.fecha_creacion: datetime = datetime.now()
        self.fecha_ultima_actualizacion: datetime = self.fecha_creacion 
        self.items: list[ItemPedido] = items
        self.direccion_entrega: Direccion = direccion_entrega
        self.total_pedido: TotalPedido = total_pedido

    def __str__(self):
        return f'Pedido: {self.id} - Cliente: {self.cliente.nombre} - Fecha Pedido: {self.fecha_pedido} - Total Pedido: {self.total_pedido}'