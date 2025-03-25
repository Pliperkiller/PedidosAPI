from Cliente import Cliente
from Producto import Producto
from ItemPedido import ItemPedido
from datetime import datetime

from value_objects.Direccion import Direccion
from value_objects.TotalPedido import TotalPedido


class Pedido:
    def __init__(self, 
                 id: int, 
                 cliente: Cliente, 
                 fecha_pedido: datetime, 
                 items: list[ItemPedido], 
                 direccion_entrega: Direccion,
                 total_pedido: TotalPedido):
        self.id = id
        self.cliente = cliente
        self.fecha_pedido = fecha_pedido
        self.items = items
        self.direccion_entrega = direccion_entrega

    def calcular_total_pedido(self):
        total = 0
        for item in self.items:
            total += item.producto.precio * item.cantidad
        return total

    def __str__(self):
        return f'Pedido: {self.id} {self.cliente} {self.fecha_pedido} {self.items} {self.direccion_entrega}'