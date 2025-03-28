from enum import Enum

class EstadoPedido(Enum):
    CREADO = "Creado" #Cliente confirma la orden con los items a solicitar
    EN_CONSULTA = "En consulta" #El microservicio consulta el inventario en el almacén
    CONFIRMADO = "Confirmado" #Se confirma el inventario
    EN_PREPARACION = "En preparación" #Se notifica al cliente y se inicia preparacion
    COMPLETADO = "Completado" # Pedido preparado
