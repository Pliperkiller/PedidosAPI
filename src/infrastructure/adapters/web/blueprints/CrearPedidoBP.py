# infrastructure/adapters/web/blueprints/pedido_blueprint.py
from flask import Blueprint, request, jsonify
from application.usecases.CrearPedidoUseCase import CrearPedidoUseCase
from application.dto import CrearPedidoInputDTO
from domain.exceptions import PedidoInvalidoError

class PedidoBlueprint:
    def __init__(self, crear_pedido_use_case: CrearPedidoUseCase):
        self.crear_pedido_use_case = crear_pedido_use_case
        self.bp = Blueprint('pedidos', __name__, url_prefix='/pedidos')
        self._register_routes()

    def _register_routes(self):
        self.bp.add_url_rule(
            '/',
            'crear_pedido',
            self.crear_pedido,
            methods=['POST']
        )

    def crear_pedido(self):
        """Endpoint para creación de nuevos pedidos"""
        try:

            data: dict = request.get_json()
            input_dto = CrearPedidoInputDTO(
                id_cliente=data.get('id_cliente'),
                direccion_entrega=data.get('direccion_entrega'),
                id_items=data.get('items')
            )


            pedido = self.crear_pedido_use_case.ejecutar(input_dto)


            return jsonify({
                'id': pedido.id,
                'estado': pedido.estado_pedido.value,
                'total': float(pedido.total_pedido.valor),
                'fecha_creacion': pedido.fecha_creacion.isoformat()
            }), 201

        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except PedidoInvalidoError as e:
            return jsonify({'error': str(e)}), 422
        except Exception as e:
            return jsonify({'error': 'Error interno del servidor'}), 500

    def get_blueprint(self):
        return self.bp


def crear_pedido_blueprint(session_factory) -> Blueprint:

    from infrastructure.adapters.persistence.repositories.PedidoRepositorySQLalchemy import PedidoRepositorySQLalchemy
    from infrastructure.adapters.persistence.repositories.ItemPedidoRepositorySQLalchemy import ItemPedidoRepositorySQLalchemy
    from infrastructure.adapters.persistence.repositories.ProductoRepositorySQLalchemy import ProductoRepositorySQLalchemy
    from application.services.ServicioCrearPedido import ServicioCrearPedido 
    
    pedido_repository = PedidoRepositorySQLalchemy(session_factory)
    item_pedido_repository = ItemPedidoRepositorySQLalchemy(session_factory)
    producto_repository = ProductoRepositorySQLalchemy(session_factory)

    pedido_service = ServicioCrearPedido(
        repositorio_item_pedido=item_pedido_repository,
        repositorio_pedido=pedido_repository,
        repositorio_producto=producto_repository
    )

    use_case = CrearPedidoUseCase(pedido_service)

    return PedidoBlueprint(use_case).get_blueprint()