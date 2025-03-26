from typing import List
from decimal import Decimal
from entities.ItemPedido import ItemPedido
from value_objects import TotalPedido

class ServicioCalcularTotalPedido:
    """Encapsula la lógica de negocio para calcular el valor total a pagar de un pedido"""
    
    @staticmethod
    def calcular_subtotal(item: ItemPedido) -> Decimal:
        """Calcula el subtotal de un ítem de pedido"""
        return item.cantidad * item.producto.precio
    
    @staticmethod
    def calcular_total(item: ItemPedido) -> Decimal:
        """Calcula el total de un ítem de pedido considerando descuentos"""
        subtotal = ServicioCalcularTotalPedido.calcular_subtotal(item)
        return subtotal * (1 - item.descuento.valor)

    @staticmethod
    def calcular_total_pedido(items: List[ItemPedido]) -> TotalPedido:
        """Calcula el total de todos los ítems en el pedido"""
        total = sum(
            ServicioCalcularTotalPedido.calcular_total(item) 
            for item in items
        )
        return TotalPedido(total)