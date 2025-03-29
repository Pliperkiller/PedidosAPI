from application.usecases.ICrearItemPedidoUseCase import ICrearItemPedidoUseCase
from domain.services.ICrearItemPedido import ICrearItemPedido
from domain.entities.ItemPedido import ItemPedido

class CrearItemPedidoUseCase(ICrearItemPedidoUseCase):
    def __init__(self, servicio_crear_item_pedido: ICrearItemPedido):
        self._servicio_crear_item_pedido = servicio_crear_item_pedido

    def ejecutar(self, id_producto: str, cantidad: int) -> ItemPedido:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        
        # Delegar la lógica al servicio
        item_pedido = self._servicio_crear_item_pedido.crear_item_pedido(id_producto, cantidad)
        return item_pedido