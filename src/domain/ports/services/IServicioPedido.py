from abc import ABC, abstractmethod
from domain.entities.Pedido import Pedido
from domain.value_objects.EstadoPedido import EstadoPedido

class IServicioPedido(ABC):
    @abstractmethod
    def calcular_total(self, pedido: Pedido) -> float:
        pass

    @abstractmethod
    def actualizar_estado(self, pedido: Pedido, nuevo_estado: EstadoPedido) -> None:
        pass

    @abstractmethod
    def validar_pedido(self, pedido: Pedido) -> bool:
        pass