# infrastructure/web/config/flask_config.py
from flask import Flask
from infrastructure.adapters.web.routes import crear_pedido_blueprint
from infrastructure.adapters.web.middleware import error_handler

def crear_app():
    app = Flask(__name__)
    
    # Configuración básica
    app.config['JSON_SORT_KEYS'] = False
    app.config['ENV'] = 'development'
    
    # Registrar blueprints
    app.register_blueprint(
        crear_pedido_blueprint(crear_pedido_use_case()),
        url_prefix='/api/v1'
    )
    
    # Registrar manejadores de errores
    app.register_error_handler(400, error_handler.handle_bad_request)
    app.register_error_handler(404, error_handler.handle_not_found)
    
    return app