from domain.entities.ItemPedido import ItemPedido

class FabricaItemPedido:
    @staticmethod
    def crear(id_producto: str, cantidad: int) -> ItemPedido:
        return ItemPedido(id_producto, cantidad)