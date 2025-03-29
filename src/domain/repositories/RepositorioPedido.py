from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.Pedido import Pedido

class RepositorioPedido(ABC):
    @abstractmethod
    def guardar(self, pedido: Pedido) -> Pedido:
        """
        Guarda un pedido en la base de datos
        """
        pass

    @abstractmethod
    def modificar(self, pedido_id: str) -> Pedido:
        """
        Modifica un pedido en la base de datos
        """
        pass

    @abstractmethod
    def buscar_por_id(self, pedido_id: str) -> Optional[Pedido]:
        """
        Busca un pedido por su id en la base de datos
        """
        pass

    @abstractmethod
    def listar(self, lista_pedidos: List[str]) -> List[Pedido]:
        """
        Busca varios pedidos la base de datos
        """
        pass

    @abstractmethod
    def borrar(self, pedido_id: str) -> None:
        """
        Borra un pedido de la base de datos
        """
        pass
