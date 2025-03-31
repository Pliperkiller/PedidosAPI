from abc import ABC, abstractmethod
from typing import List
from domain.entities.Pedido import Pedido

class RepositorioPedido(ABC):
    @abstractmethod
    def guardar(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def buscar_por_id(self, pedido_id: str) -> Pedido:
        pass

    @abstractmethod
    def borrar(self, pedido_id: str) -> None:
        pass

    @abstractmethod
    def listar(self) -> List[Pedido]:
        pass

    @abstractmethod
    def modificar(self, pedido: Pedido) -> Pedido:
        pass