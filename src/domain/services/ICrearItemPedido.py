from abc import ABC, abstractmethod
from domain.entities.ItemPedido import ItemPedido

class ICrearItemPedido(ABC):
    @abstractmethod
    def crear_item_pedido(self, id_producto: str, cantidad: int) -> ItemPedido:
        pass
