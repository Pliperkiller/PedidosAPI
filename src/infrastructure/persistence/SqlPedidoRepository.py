from typing import List, Optional
from ...domain.ports.RepositorioPedido import IPedidoRepository
from ...domain.entities.Pedido import Pedido

class SqlPedidoRepository(IPedidoRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def save(self, pedido: Pedido) -> Pedido:
        # Implementación específica para SQL
        pass

    def find_by_id(self, pedido_id: str) -> Optional[Pedido]:
        # Implementación específica para SQL
        pass

    def find_all(self) -> List[Pedido]:
        # Implementación específica para SQL
        pass

    def delete(self, pedido_id: str) -> None:
        # Implementación específica para SQL
        pass
