from Cliente import Cliente
from Producto import Producto
from ItemPedido import ItemPedido
from datetime import datetime

from value_objects.Direccion import Direccion


class Pedido:
    def __init__(self, id: int, cliente: Cliente, fecha: datetime, items: list[ItemPedido], direccion_entrega: Direccion):
        self.id = id
        self.cliente = cliente
        self.fecha = fecha
        self.items = items
        self.direccion_entrega = direccion_entrega

    def __str__(self):
        return f'Pedido: {self.id} {self.cliente} {self.fecha} {self.items} {self.direccion_entrega}'