# infrastructure/adapters/persistence/repositories/item_pedido_repository_sqlalchemy.py
from sqlalchemy.orm import Session
from domain.entities import ItemPedido
from domain.repositories.RepositorioItemPedido import RepositorioItemPedido
from domain.exceptions import ItemNoEncontradoError
from infrastructure.adapters.persistence.models import ItemPedidoModel
from datetime import datetime
from typing import List

class ItemPedidoRepositorySQLalchemy(RepositorioItemPedido):
    def __init__(self, session_factory: callable):
        self.session_factory = session_factory

    def _model_to_entity(self, model: ItemPedidoModel) -> ItemPedido:
        item = ItemPedido(
            id_producto=model.id_producto,
            cantidad=model.cantidad
        )
        item.id = model.id
        item.fecha_creacion = model.fecha_creacion

        return item

    def _entity_to_model(self, entity: ItemPedido) -> ItemPedidoModel:
        return ItemPedidoModel(
            id=entity.id,
            id_producto=entity.id_producto,
            cantidad=entity.cantidad,
            fecha_creacion=entity.fecha_creacion,
            pedido_id=entity.pedido_id if hasattr(entity, 'pedido_id') else None
        )

    def guardar(self, item: ItemPedido) -> ItemPedido:
        with self.session_factory() as session:
            item_model = self._entity_to_model(item)
            
            existing_item = session.query(ItemPedidoModel).get(item.id)
            if existing_item:
                existing_item.cantidad = item_model.cantidad
                existing_item.id_producto = item_model.id_producto
                existing_item.pedido_id = item_model.pedido_id
            else:
                session.add(item_model)
            
            session.commit()
            return self._model_to_entity(item_model)

    def buscar_por_id(self, item_id: str) -> ItemPedido:
        with self.session_factory() as session:
            item_model = session.query(ItemPedidoModel).get(item_id)
            if not item_model:
                raise ItemNoEncontradoError(item_id=item_id)
            return self._model_to_entity(item_model)

    def listar_por_pedido(self, pedido_id: str) -> list[ItemPedido]:
        with self.session_factory() as session:
            items_model = session.query(ItemPedidoModel)\
                .filter_by(pedido_id=pedido_id)\
                .all()
            return [self._model_to_entity(item) for item in items_model]

    def eliminar(self, item_id: str) -> None:
        with self.session_factory() as session:
            item_model = session.query(ItemPedidoModel).get(item_id)
            if not item_model:
                raise ItemNoEncontradoError(item_id=item_id)
            session.delete(item_model)
            session.commit()

    def borrar(self, item_id: str) -> None:
        """Elimina un item de pedido por su ID"""
        with self.session_factory() as session:
            item_model = session.query(ItemPedidoModel).filter_by(id=item_id).first()
            if item_model:
                session.delete(item_model)
                session.commit()

    def listar(self, ids: List[str]) -> List[ItemPedido]:
        """Lista los items de pedido por sus IDs"""
        with self.session_factory() as session:
            modelos = session.query(ItemPedidoModel).filter(ItemPedidoModel.id.in_(ids)).all()
            return [self._to_entity(modelo) for modelo in modelos]
