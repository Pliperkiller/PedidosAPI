from abc import ABC, abstractmethod
from domain.entities.Pedido import Pedido
from domain.value_objects.Direccion import Direccion
from typing import List

class ICrearPedidoUseCase(ABC):
    @abstractmethod
    def ejecutar(self, id_cliente: str, direccion_entrega: Direccion, id_items: List[str]) -> Pedido:
        pass