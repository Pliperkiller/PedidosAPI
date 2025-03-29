from typing import Dict
from PedidosAPI.src.domain.ports.usecases.CasoCrearItemPedido import CasoCrearItemPedido
from PedidosAPI.src.domain.ports.usecases.CasoCrearPedido import CasoCrearPedido


class ControladorCrearPedido:
    def __init__(
        self,
        servicio_crear_pedido: CasoCrearPedido,
        servicio_crear_item_pedido: CasoCrearItemPedido
    ):
        self._servicio_crear_pedido = servicio_crear_pedido
        self._servicio_crear_item_pedido = servicio_crear_item_pedido    

    def ejecutar(self, datos_pedido: Dict):
        # Datos pedido:{
        # 'id_cliente': 'a1b2c3d4-5678-90ef-1234-567890abcdef', 
        # 'direccion_entrega': {alias: Casa, pais: Argentina, ciudad: Buenos Aires, estado: Buenos Aires, calle: Av. Siempreviva, calle2: 123, codigo_postal: 1234, coordenadas: -34.603722, -58.381592},
        # 'items': [{'id_producto': '1', 'cantidad': 2}, {'id_producto': '2', 'cantidad': 3}]
        # }
        id_cliente = datos_pedido['id_cliente']
        direccion_entrega = datos_pedido['direccion_entrega']
        items = datos_pedido['items'] 
        id_items = []

        # Crear los items pedido
        for item in items:
            id_producto = item['id_producto']
            cantidad = item['cantidad']
            item_pedido = self._servicio_crear_item_pedido.crear_item_pedido(id_producto, cantidad)
            id_items.append(item_pedido.id)

        # Crear el pedido
        self._servicio_crear_pedido.crear_pedido(id_cliente, direccion_entrega, id_items)