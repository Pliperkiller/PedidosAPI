from domain.entities.Pedido import Pedido
from domain.value_objects.Direccion import Direccion
from typing import List

class FabricaPedido:
    @staticmethod
    def crear(  id_cliente: str,
                direccion_entrega: Direccion,
                id_items: List[str]) -> Pedido:
        return Pedido(id_cliente, direccion_entrega, id_items)