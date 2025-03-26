from enum import Enum

class EstadoPedido(Enum):
    CREADO = "Creado"
    EN_PREPARACION = "En preparación"
    LISTO_PARA_ENVIAR = "Listo para enviar"
    EN_RUTA = "En ruta"
    ENTREGADO = "Entregado"
    CANCELADO = "Cancelado"
