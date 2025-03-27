from flask import Flask
from infrastructure.config.database import db
from infrastructure.adapters.api import pedido_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:5432/tu_base_de_datos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(pedido_blueprint)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
