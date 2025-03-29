# infrastructure/web/app.py
from infrastructure.config.flask_config import crear_app

app = crear_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)