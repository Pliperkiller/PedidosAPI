# application/usecases/obtener_pedido_use_case.py
from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.Pedido import Pedido

class IObtenerPedidoUseCase(ABC):
    @abstractmethod
    def ejecutar(self, pedido_id: str) -> Optional[Pedido]:
        pass