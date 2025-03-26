from enum import Enum

class EstadoPedido(Enum):
    CREADO = "Creado" #Cliente crea el pedido
    RECIBIDO = "Recibido" #El microservicio recibe la solicitud
    EN_CONSULTA = "En consulta" #consulta al inventario
    CONFIRMADO = "Confirmado" #Se confirma el inventario
    EN_PREPARACION = "En preparación" #Se notifica al cliente y se inicia preparacion
    COMPLETADO = "Completado" # Pedido preparado
