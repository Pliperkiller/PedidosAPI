from abc import ABC, abstractmethod
from domain.entities.Pedido import Pedido
from domain.entities.ItemPedido import ItemPedido

class IPedidoService(ABC):

    @abstractmethod
    def agregar_item(self, pedido: Pedido, item: ItemPedido):
        """ Agrega un ítem a un pedido. """
        pass

    @abstractmethod
    def eliminar_item(self, pedido: Pedido, item_id: str):
        """ Elimina un ítem de un pedido. """
        pass

    @abstractmethod
    def recalcular_total(self, pedido: Pedido):
        """ Recalcula el total del pedido. """
        pass
