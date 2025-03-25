from Producto import Producto

class ItemPedido:
    def __init__(self, id: int ,producto: Producto, cantidad: int):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad