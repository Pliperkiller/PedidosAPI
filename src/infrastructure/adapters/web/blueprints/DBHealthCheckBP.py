from flask import Blueprint, jsonify
from datetime import datetime
import time
from sqlalchemy import text
from typing import Dict, Any

class DBHealthBlueprint:
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.bp = Blueprint('db_health', __name__)
        self._register_routes()

    def _register_routes(self):
        self.bp.add_url_rule(
            '/db-health',
            'check_db_health',
            self.check_db_health,
            methods=['GET']
        )

    def check_db_health(self) -> Dict[str, Any]:
        """Endpoint para verificar el estado de la base de datos"""
        start_time = time.time()
        status = {
            "status": "OK",
            "timestamp": datetime.utcnow().isoformat(),
            "database": {}
        }

        try:
            with self.session_factory() as session:

                result = session.execute(text("SELECT 1")).scalar()
                
                status["database"].update({
                    "connection_test": "successful" if result == 1 else "failed",
                    "response_time_ms": round((time.time() - start_time) * 1000, 2),
                    "engine": str(session.bind.engine.url),
                    "pool_status": {
                        "checked_out": session.bind.pool.checkedout(),
                        "checked_in": session.bind.pool.checkedin(),
                        "size": session.bind.pool.size()
                    }
                })

                if self._test_write_operation(session):
                    status["database"]["write_test"] = "successful"
                else:
                    status["database"]["write_test"] = "failed"
                    status["status"] = "WARNING"

        except Exception as e:
            status.update({
                "status": "ERROR",
                "error": str(e),
                "database": {
                    "connection_test": "failed",
                    "response_time_ms": round((time.time() - start_time) * 1000, 2)
                }
            })
            return jsonify(status), 500

        return jsonify(status), 200

    def _test_write_operation(self, session) -> bool:
        """Test de operación de escritura en la base de datos"""
        try:
            test_table = text("""
                CREATE TABLE IF NOT EXISTS health_check (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP NOT NULL
                )
            """)
            session.execute(test_table)
            
            insert = text("INSERT INTO health_check (timestamp) VALUES (NOW())")
            session.execute(insert)
            
            session.commit()
            return True
        except:
            session.rollback()
            return False

    def get_blueprint(self):
        return self.bp

def crear_db_health_blueprint(session_factory) -> Blueprint:
    return DBHealthBlueprint(session_factory).get_blueprint()