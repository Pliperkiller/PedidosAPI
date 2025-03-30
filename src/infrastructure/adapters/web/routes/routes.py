from flask import Blueprint
from infrastructure.adapters.web.controllers.ControladorPedido import register_routes

def crear_pedido_blueprint(crear_pedido_use_case):
    """Crea y configura el blueprint para pedidos"""
    bp = Blueprint('pedidos', __name__)
    register_routes(bp, crear_pedido_use_case)
    return bp