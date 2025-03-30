# application/usecases/obtener_pedido_use_case.py
from domain.repositories.RepositorioPedido import RepositorioPedido
from domain.exceptions.PedidoNoEncontradoError import PedidoNoEncontradoError
from application.usecases.IObtenerPedidoUseCase import IObtenerPedidoUseCase
from domain.entities.Pedido import Pedido

class ObtenerPedidoUseCase(IObtenerPedidoUseCase):
    def __init__(self, pedido_repository: RepositorioPedido):
        self.pedido_repository = pedido_repository
        
    def ejecutar(self, pedido_id: str) -> Pedido:
        if not pedido_id or not isinstance(pedido_id, str):
            raise ValueError("ID de pedido inválido")
            
        pedido = self.pedido_repository.buscar_por_id(pedido_id)
        
        if not pedido:
            raise PedidoNoEncontradoError(f"Pedido {pedido_id} no encontrado")
            
        return pedido