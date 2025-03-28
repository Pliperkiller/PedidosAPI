from domain.entities.ItemPedido import ItemPedido

class FabricaItemPedido:
    @staticmethod
    def crear(producto_id: str, cantidad: int) -> ItemPedido:
        return ItemPedido(producto_id, cantidad)