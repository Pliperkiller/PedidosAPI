from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.Producto import Producto

class RepositorioProducto(ABC):
    @abstractmethod
    def guardar(self, producto: Producto) -> Producto:
        pass

    @abstractmethod
    def modificar(self, producto_id: str) -> Producto:
        pass

    @abstractmethod
    def buscar_por_id(self, producto_id: str) -> Optional[Producto]:
        pass

    @abstractmethod
    def borrar(self, producto_id: str) -> None:
        pass
