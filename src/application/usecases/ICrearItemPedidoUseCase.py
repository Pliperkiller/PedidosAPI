from abc import ABC, abstractmethod
from domain.entities.ItemPedido import ItemPedido

class ICrearItemPedidoUseCase(ABC):
    @abstractmethod
    def ejecutar(self, id_producto: str, cantidad: int) -> ItemPedido:
        pass