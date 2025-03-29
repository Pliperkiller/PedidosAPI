from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.Cliente import Cliente

class RepositorioCliente(ABC):
    @abstractmethod
    def guardar(self, cliente: Cliente) -> Cliente:
        pass

    @abstractmethod
    def modificar(self, cliente_id: str) -> Cliente:
        pass

    @abstractmethod
    def buscar_por_id(self, cliente_id: str) -> Optional[Cliente]:
        pass

    @abstractmethod
    def listar(self) -> List[Cliente]:
        pass

    @abstractmethod
    def borrar(self, cliente_id: str) -> None:
        pass
