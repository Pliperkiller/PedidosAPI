from domain.ports.services.IServicioPedido import IServicioPedido
from domain.entities.Pedido import Pedido
from domain.value_objects.EstadoPedido import EstadoPedido
from domain.ports.repositories.RepositorioItemPedido import RepositorioItemPedido
from datetime import datetime

class ServicioPedido(IServicioPedido):
    def __init__(self, item_pedido_repositorio: RepositorioItemPedido):
        self._repositorio_item = item_pedido_repositorio

    def calcular_total(self, pedido: Pedido) -> float:
        total = 0.0
        for item_id in pedido.id_items:
            item = self._repositorio_item.buscar_por_id(item_id)
            total += item.subtotal
        return total

    def actualizar_estado(self, pedido: Pedido, nuevo_estado: EstadoPedido) -> None:
        pedido.estado_pedido = nuevo_estado
        pedido.fecha_ultima_actualizacion = datetime.now()

    def validar_pedido(self, pedido: Pedido) -> bool:
        return (
            len(pedido.id_items) > 0 and
            pedido.id_cliente is not None and
            pedido.direccion_entrega is not None
        )