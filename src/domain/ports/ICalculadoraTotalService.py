from abc import ABC, abstractmethod
from decimal import Decimal
from ..entities.ItemPedido import ItemPedido
from ..value_objects.TotalPedido import TotalPedido
from typing import List

class ICalculadoraTotalService(ABC):
    @abstractmethod
    def calcular_total_pedido(self, items: List[ItemPedido]) -> TotalPedido:
        pass

    @abstractmethod
    def calcular_subtotal(self, item: ItemPedido) -> Decimal:
        pass
