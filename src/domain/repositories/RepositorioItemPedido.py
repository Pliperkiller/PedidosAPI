from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.ItemPedido import ItemPedido

class RepositorioItemPedido(ABC):
    @abstractmethod
    def guardar(self, pedido: ItemPedido) -> ItemPedido:
        """
        Guarda un item de pedido en la base de datos
        """
        pass

    @abstractmethod
    def buscar_por_id(self, pedido_id: str) -> Optional[ItemPedido]:
        """
        Busca un item de pedido por su id en la base de datos
        """
        pass

    @abstractmethod
    def listar(self, lista_pedidos: List[str]) -> List[ItemPedido]:
        """
        Busca varios item de pedido la base de datos
        """
        pass

    @abstractmethod
    def borrar(self, pedido_id: str) -> None:
        """
        Borra un item de pedido de la base de datos
        """
        pass
