from datetime import datetime
import uuid

from ItemPedido import ItemPedido
from Cliente import Cliente
from value_objects.Direccion import Direccion
from value_objects.TotalPedido import TotalPedido
from value_objects.EstadoPedido import EstadoPedido
from Services.ServiceCalcularTotalPedido import ServicioCalcularTotalPedido



class Pedido:
    def __init__(self,cliente,items,direccion_entrega):
        self.id: str = str(uuid.uuid4())
        self.cliente: Cliente = cliente
        self.estado_pedido: EstadoPedido = EstadoPedido.CREADO
        self.fecha_creacion: datetime = datetime.now()
        self.fecha_ultima_actualizacion: datetime = self.fecha_creacion 
        self.items: list[ItemPedido] = items
        self.direccion_entrega: Direccion = direccion_entrega
        self.total_pedido: TotalPedido = self.calcular_total_pedido()

    def actualizar_estado_pedido(self, nuevo_estado: EstadoPedido):
        self.estado_pedido = nuevo_estado
        self.fecha_ultima_actualizacion = datetime.now()

    def calcular_total_pedido(self)->TotalPedido:
        return ServicioCalcularTotalPedido.calcular_total_pedido(self.items)


    def __str__(self):
        return f'Pedido: {self.id} - Cliente: {self.cliente.nombre} - Fecha Pedido: {self.fecha_pedido} - Total Pedido: {self.total_pedido}'