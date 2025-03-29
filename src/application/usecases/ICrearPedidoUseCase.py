from abc import ABC, abstractmethod
from domain.entities.Pedido import Pedido
from application.dto.CrearPedidoInputDTO import CrearPedidoInputDTO

class ICrearPedidoUseCase(ABC):
    @abstractmethod
    def ejecutar(self, crear_pedido_dto = CrearPedidoInputDTO) -> Pedido:
        pass