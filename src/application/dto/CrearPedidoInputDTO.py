from typing import List
from domain.value_objects.Direccion import Direccion
from dataclasses import dataclass


@dataclass
class CrearPedidoInputDTO:
    id_cliente: str
    direccion_entrega: Direccion
    id_items: List[str]