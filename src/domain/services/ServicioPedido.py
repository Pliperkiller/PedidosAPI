from abc import ABC, abstractmethod
from typing import List, Optional

from ports.RepositorioPedido import RepositorioPedido
from entities.Pedido import Pedido
from entities.ItemPedido import ItemPedido
from entities.Cliente import Cliente
from value_objects.Direccion import Direccion
from value_objects.TotalPedido import TotalPedido 
from ServicioCalcularTotalPedido import ServicioCalcularTotalPedido

class IServicioPedido(ABC):
    @abstractmethod
    def crear_pedido(self)->Pedido:
        pass

    @abstractmethod
    def buscar_pedido(self)->Optional[Pedido]:
        pass

    @abstractmethod
    def obtener_todos(self)->List[Pedido]:
        pass

    @abstractmethod
    def borrar_pedido(self, id_pedido: str)->None:
        pass


class ServicioPedido:
    def __init__(self, repositorio, servicio_total):
        self.repositorio: RepositorioPedido = repositorio
        self.servicio_total: ServicioCalcularTotalPedido = servicio_total

    def crear_pedido(self,cliente: Cliente,items: List[ItemPedido],direccion_entrega: Direccion):
        pedido = Pedido(cliente,items,direccion_entrega)
        pedido.total_pedido = ServicioCalcularTotalPedido.calcular_total_pedido(items)