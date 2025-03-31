from sqlalchemy.orm import Session
from domain.entities.Pedido import Pedido
from domain.repositories.RepositorioPedido import RepositorioPedido
from domain.value_objects import EstadoPedido
from domain.exceptions import PedidoNoEncontradoError
from infrastructure.adapters.persistence.models.PedidoModel import PedidoModel
from typing import Callable, List

class PedidoRepositorySQLalchemy(RepositorioPedido):
    def __init__(self, session_factory: Callable[[], Session]):
        self.session_factory = session_factory

    def _to_entity(self, model: PedidoModel) -> Pedido:
        """Mapea el modelo de SQLAlchemy a la entidad de dominio"""
        return Pedido(
            id=model.id,
            id_cliente=model.id_cliente,
            direccion_entrega=model.direccion_entrega,
            id_items=model.id_items,
            estado_pedido=EstadoPedido(model.estado),
            fecha_creacion=model.fecha_creacion,
            fecha_ultima_actualizacion=model.fecha_ultima_actualizacion,
            total_pedido=model.total
        )

    def _to_model(self, entity: Pedido) -> PedidoModel:
        """Mapea la entidad de dominio al modelo de SQLAlchemy"""
        return PedidoModel(
            id=entity.id,
            id_cliente=entity.id_cliente,
            direccion_entrega=entity.direccion_entrega,
            id_items=entity.id_items,
            estado=entity.estado_pedido.value,
            fecha_creacion=entity.fecha_creacion,
            fecha_ultima_actualizacion=entity.fecha_ultima_actualizacion,
            total=entity.total_pedido
        )

    def guardar(self, pedido: Pedido) -> Pedido:
        with self.session_factory() as session:
            pedido_model = self._to_model(pedido)
            session.add(pedido_model)
            session.commit()
            return self._to_entity(pedido_model)

    def buscar_por_id(self, pedido_id: str) -> Pedido:
        with self.session_factory() as session:
            pedido_model = session.query(PedidoModel)\
                .filter_by(id=pedido_id)\
                .first()
            
            if not pedido_model:
                raise PedidoNoEncontradoError(pedido_id=pedido_id)
                
            return self._to_entity(pedido_model)

    def borrar(self, pedido_id: str) -> None:
        """Elimina un pedido por su ID"""
        with self.session_factory() as session:
            pedido_model = session.query(PedidoModel)\
                .filter_by(id=pedido_id)\
                .first()
            
            if not pedido_model:
                raise PedidoNoEncontradoError(pedido_id=pedido_id)
            
            session.delete(pedido_model)
            session.commit()

    def listar(self) -> List[Pedido]:
        """Lista todos los pedidos"""
        with self.session_factory() as session:
            modelos = session.query(PedidoModel).all()
            return [self._to_entity(modelo) for modelo in modelos]

    def modificar(self, pedido: Pedido) -> Pedido:
        """Modifica un pedido existente"""
        with self.session_factory() as session:
            pedido_model = session.query(PedidoModel)\
                .filter_by(id=pedido.id)\
                .first()
            
            if not pedido_model:
                raise PedidoNoEncontradoError(pedido_id=pedido.id)
            
            # Actualizar los campos del modelo
            pedido_model.id_cliente = pedido.id_cliente
            pedido_model.direccion_entrega = pedido.direccion_entrega
            pedido_model.id_items = pedido.id_items
            pedido_model.estado = pedido.estado_pedido.value
            pedido_model.fecha_ultima_actualizacion = pedido.fecha_ultima_actualizacion
            pedido_model.total = pedido.total_pedido
            
            session.commit()
            return self._to_entity(pedido_model)