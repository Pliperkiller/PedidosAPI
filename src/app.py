from flask import Flask
from infrastructure.adapters.web.blueprints.CrearPedidoBP import crear_pedido_blueprint, PedidoBlueprint
from infrastructure.adapters.web.blueprints.HealthCheckBP import crear_health_check_blueprint, HealthCheckBlueprint
from infrastructure.adapters.web.blueprints.DBHealthCheckBP import crear_db_health_blueprint, DBHealthBlueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

def create_app():
    database_uri = os.getenv("DATABASE_URI")

    # Configurar la sesión de SQLAlchemy
    engine = create_engine(database_uri)
    Session = sessionmaker(bind=engine)
    
    # Crear blueprints inyectando Session factory
    pedido_bp = crear_pedido_blueprint(Session)
    health_check_bp = crear_health_check_blueprint()
    db_health_bp = crear_db_health_blueprint(Session)

    
    # Configurar la aplicación Flask
    app = Flask(__name__)
    app.register_blueprint(pedido_bp)
    app.register_blueprint(health_check_bp)
    app.register_blueprint(db_health_bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)