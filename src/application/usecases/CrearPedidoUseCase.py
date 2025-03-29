from application.usecases.ICrearPedidoUseCase import ICrearPedidoUseCase
from domain.services.ICrearPedido import ICrearPedido
from domain.entities.Pedido import Pedido
from domain.value_objects.Direccion import Direccion
from typing import List

class CrearPedidoUseCase(ICrearPedidoUseCase):
    def __init__(self, servicio_crear_pedido: ICrearPedido):
        self._servicio_crear_pedido = servicio_crear_pedido

    def ejecutar(self, id_cliente: str, direccion_entrega: Direccion, id_items: List[str]) -> Pedido:
        if not id_items:
            raise ValueError("El pedido debe contener al menos un item.")
        
        pedido = self._servicio_crear_pedido.crear_pedido(id_cliente, direccion_entrega, id_items)
        return pedido