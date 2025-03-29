from datetime import datetime
from uuid import UUID
from typing import List, Dict, Any
from domain.value_objects import Direccion, EstadoPedido, TotalPedido
from domain.entities import Pedido

class PedidoInputDTO:
    def __init__(self, 
                id_cliente: str,
                direccion_entrega: Dict[str, Any],
                id_items: List[str]):
        
        if not id_cliente:
            raise ValueError("El ID de cliente es requerido")
        if not direccion_entrega or not isinstance(direccion_entrega, dict):
            raise ValueError("Dirección de entrega inválida")
        if not id_items or len(id_items) == 0:
            raise ValueError("El pedido debe contener al menos un item")

        self.id_cliente = id_cliente
        self.direccion_entrega = direccion_entrega
        self.id_items = id_items

    def to_entity(self) -> Pedido:
        """Convierte el DTO a entidad de dominio"""
        return Pedido(
            id_cliente=self.id_cliente,
            direccion_entrega=Direccion(**self.direccion_entrega),
            id_items=self.id_items
        )

class PedidoOutputDTO:
    def __init__(self, pedido: Pedido):
        self.id = pedido.id
        self.id_cliente = pedido.id_cliente
        self.direccion_entrega = self._serialize_direccion(pedido.direccion_entrega)
        self.id_items = pedido.id_items
        self.estado = pedido.estado_pedido.value
        self.fecha_creacion = pedido.fecha_creacion.isoformat()
        self.fecha_actualizacion = pedido.fecha_ultima_actualizacion.isoformat()
        self.total = float(pedido.total_pedido.valor)

    def _serialize_direccion(self, direccion: Direccion) -> Dict[str, Any]:
        return {
            "calle": direccion.calle,
            "numero": direccion.numero,
            "ciudad": direccion.ciudad,
            "codigo_postal": direccion.codigo_postal
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "id_cliente": self.id_cliente,
            "direccion_entrega": self.direccion_entrega,
            "items": self.id_items,
            "estado": self.estado,
            "fecha_creacion": self.fecha_creacion,
            "fecha_actualizacion": self.fecha_actualizacion,
            "total": self.total
        }
