from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.ItemPedido import ItemPedido

class RepositorioItemPedido(ABC):
    @abstractmethod
    def guardar(self, item_pedido: ItemPedido) -> ItemPedido:
        pass

    @abstractmethod
    def modificar(self, id_item_pedido: str) -> ItemPedido:
        pass

    @abstractmethod
    def buscar_por_id(self, id_item_pedido: str) -> Optional[ItemPedido]:
        pass

    @abstractmethod
    def listar(self) -> List[ItemPedido]:
        pass

    @abstractmethod
    def borrar(self, id_item_pedido: str) -> None:
        pass
