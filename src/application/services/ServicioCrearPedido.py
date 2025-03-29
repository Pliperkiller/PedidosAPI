from domain.services.ICrearPedido import ICrearPedido
from domain.entities.Pedido import Pedido
from domain.value_objects.Direccion import Direccion
from domain.value_objects.TotalPedido import TotalPedido
from domain.repositories.RepositorioItemPedido import RepositorioItemPedido
from domain.repositories.RepositorioPedido import RepositorioPedido
from domain.repositories.RepositorioProducto import RepositorioProducto
from domain.factories.FabricaPedido import FabricaPedido

from decimal import Decimal
from typing import List


class ServicioCrearPedido(ICrearPedido):
    def __init__(self,
                repositorio_item_pedido: RepositorioItemPedido,
                repositorio_pedido: RepositorioPedido,
                repositorio_producto: RepositorioProducto,
                ):

        self._repositorio_item = repositorio_item_pedido
        self._repositorio_pedido = repositorio_pedido
        self._repositorio_producto = repositorio_producto


    def crear_pedido(self, id_cliente: str, direccion_entrega: Direccion, id_items: List[str]) -> Pedido:
        pedido = FabricaPedido.crear(id_cliente, direccion_entrega, id_items)
        total_pedido = self._calcular_total(pedido)
        pedido.actualizar_total_pedido(total_pedido)
        pedido = self._repositorio_pedido.guardar(pedido)
        return pedido

    def _calcular_total(self, pedido: Pedido) -> TotalPedido:
        total = Decimal(0)
        id_items = pedido.id_items
        items = self._repositorio_item.listar(id_items)
        total = sum(item.subtotal for item in items)
        return TotalPedido(total)
