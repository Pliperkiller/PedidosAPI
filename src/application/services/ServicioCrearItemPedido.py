from domain.entities.ItemPedido import ItemPedido
from domain.repositories.RepositorioItemPedido import RepositorioItemPedido
from domain.repositories.RepositorioProducto import RepositorioProducto
from domain.factories.FabricaItemPedido import FabricaItemPedido
from domain.services.ICrearItemPedido import ICrearItemPedido


class ServicioCrearItemPedido(ICrearItemPedido):
    def __init__(self, repositorio_item_pedido: RepositorioItemPedido, repositorio_producto: RepositorioProducto):
        self.repositorio_item_pedido = repositorio_item_pedido
        self.repositorio_producto = repositorio_producto
        
    def crear_item_pedido(self, id_producto: str, cantidad: int) -> ItemPedido:
        producto = self.repositorio_producto.buscar_por_id(id_producto)
        item_pedido = FabricaItemPedido.crear(producto, cantidad)
        self.repositorio_item_pedido.guardar(item_pedido)
        return item_pedido