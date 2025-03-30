# app.py
from flask import Flask
from infrastructure.adapters.web.routes import create_pedido_blueprint
from infrastructure.adapters.persistence import SQLAlchemyPedidoRepository
from application.usecases import (
    CrearPedidoUseCase,
    ObtenerPedidoUseCase,
    ActualizarEstadoUseCase
)

def create_app():
    app = Flask(__name__)
    
    # Configurar repositorios
    pedido_repo = SQLAlchemyPedidoRepository()
    
    # Inicializar casos de uso
    crear_pedido_uc = CrearPedidoUseCase(pedido_repo)
    obtener_pedido_uc = ObtenerPedidoUseCase(pedido_repo)
    actualizar_estado_uc = ActualizarEstadoUseCase(pedido_repo)
    
    # Registrar blueprint
    pedido_bp = create_pedido_blueprint(
        crear_pedido_uc,
        obtener_pedido_uc,
        actualizar_estado_uc
    )
    app.register_blueprint(pedido_bp)
    
    return app