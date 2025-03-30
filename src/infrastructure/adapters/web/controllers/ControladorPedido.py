# infrastructure/web/controllers/pedido_controller.py
from flask import Blueprint, request, jsonify
from application.usecases.CrearPedidoUseCase import CrearPedidoUseCase
from application.dto.PedidoDTO import PedidoInputDTO, PedidoOutputDTO

class PedidoController:
    def __init__(self, crear_pedido_use_case: CrearPedidoUseCase):
        self.crear_pedido_use_case = crear_pedido_use_case

    def crear_pedido(self):
        """Manejador para la creación de pedidos"""
        try:
            # Obtener y validar datos del request
            data = request.get_json()
            
            # Crear DTO de entrada
            input_dto = PedidoInputDTO(
                id_cliente=data.get('id_cliente'),
                direccion_entrega=data.get('direccion_entrega'),
                id_items=data.get('id_items')
            )

            # Ejecutar caso de uso
            pedido = self.crear_pedido_use_case.ejecutar(input_dto)

            # Convertir a DTO de salida
            output_dto = PedidoOutputDTO(pedido)
            
            return jsonify(output_dto.to_dict()), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500

def registrar_rutas(blueprint: Blueprint, crear_pedido_use_case: CrearPedidoUseCase):
    """Registra las rutas relacionadas con pedidos"""
    controller = PedidoController(crear_pedido_use_case)
    
    blueprint.add_url_rule(
        '/pedidos',
        'crear_pedido',
        controller.crear_pedido,
        methods=['POST']
    )