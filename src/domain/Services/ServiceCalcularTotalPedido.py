from entities import Pedido

class ServicioCalcularTotalPedido:
    """Encapsula la lógica de negocio para calcular el valor total a pagar de un pedido"""
    @staticmethod
    def calcular_total_pedido(self, pedido: Pedido):
        for item in pedido.items:
            total += item.total_item()
            pedido.total_pedido = total