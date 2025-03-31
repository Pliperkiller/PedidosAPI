from flask import Blueprint, jsonify
from datetime import datetime
import os

class HealthCheckBlueprint:
    def __init__(self):
        self.bp = Blueprint('health_check', __name__)
        self._register_routes()

    def _register_routes(self):
        self.bp.add_url_rule(
            '/health',
            'health_check',
            self.health_check,
            methods=['GET']
        )

    def health_check(self):
        """Endpoint para verificar el estado de la API"""
        try:
            return jsonify({
                "status": "available",
                "message": "API en funcionamiento",
                "version": os.getenv("API_VERSION", "1.0.0"),
                "environment": os.getenv("FLASK_ENV", "development"),
                "timestamp": datetime.utcnow().isoformat()
            }), 200
        except Exception as e:
            return jsonify({
                "status": "unavailable",
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }), 500

    def get_blueprint(self):
        return self.bp

def crear_health_check_blueprint() -> Blueprint:
    return HealthCheckBlueprint().get_blueprint()