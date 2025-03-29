from application.usecases.ICrearPedidoUseCase import ICrearPedidoUseCase
from application.dto.CrearPedidoInputDTO import CrearPedidoInputDTO
from domain.services.ICrearPedido import ICrearPedido
from domain.entities.Pedido import Pedido

class CrearPedidoUseCase(ICrearPedidoUseCase):
    def __init__(self, servicio_crear_pedido: ICrearPedido):
        self._servicio_crear_pedido = servicio_crear_pedido

    def ejecutar(self, input_dto: CrearPedidoInputDTO) -> Pedido:
        if not input_dto.id_items:
            raise ValueError("El pedido debe contener al menos un item.")
        
        pedido = self._servicio_crear_pedido.crear_pedido(input_dto.id_cliente, input_dto.direccion_entrega, input_dto.id_items)
        return pedido