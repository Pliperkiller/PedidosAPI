from enum import Enum

class EstadoPedido(Enum):
    PENDIENTE = "Pendiente"
    EN_PREPARACION = "En preparación"
    LISTO_PARA_ENTREGAR = "Listo para entregar"
    ENTREGADO = "Entregado"
    CANCELADO = "Cancelado"