from domain.entities.Pedido import Pedido
from domain.value_objects.Direccion import Direccion

class FabricaPedido:
    @staticmethod
    def crear(id_cliente: str, direccion_entrega: Direccion) -> Pedido:
        return Pedido(id_cliente, direccion_entrega)