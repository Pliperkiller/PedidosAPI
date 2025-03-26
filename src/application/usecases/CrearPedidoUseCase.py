from dataclasses import dataclass
from typing import List
from ...domain.entities.Pedido import Pedido
from ...domain.entities.Cliente import Cliente
from ...domain.entities.ItemPedido import ItemPedido
from ...domain.ports.IPedidoRepository import IPedidoRepository
from ...domain.value_objects.Direccion import Direccion

@dataclass
class CrearPedidoRequest:
    cliente: Cliente
    items: List[ItemPedido]
    direccion_entrega: Direccion

class CrearPedidoUseCase:
    def __init__(self, pedido_repository: IPedidoRepository):
        self.pedido_repository = pedido_repository

    def execute(self, request: CrearPedidoRequest) -> Pedido:
        pedido = Pedido(
            cliente=request.cliente,
            items=request.items,
            direccion_entrega=request.direccion_entrega
        )
        return self.pedido_repository.save(pedido)
