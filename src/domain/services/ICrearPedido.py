from abc import ABC, abstractmethod
from domain.entities.Pedido import Pedido
from domain.value_objects.Direccion import Direccion
from domain.value_objects.TotalPedido import TotalPedido
from typing import List


class ICrearPedido(ABC):
    @abstractmethod
    def _calcular_total(self, pedido: Pedido) -> TotalPedido:
        pass

    @abstractmethod
    def crear_pedido(self, id_cliente: str, direccion_entrega: Direccion, id_items: List[str]) -> Pedido:
        pass