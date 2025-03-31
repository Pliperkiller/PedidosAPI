# infrastructure/adapters/persistence/repositories/producto_repository_sqlalchemy.py
from sqlalchemy.orm import Session
from domain.entities.Producto import Producto
from domain.repositories.RepositorioProducto import RepositorioProducto
from domain.exceptions import ProductoNoEncontradoError
from infrastructure.adapters.persistence.models import ProductoModel

class ProductoRepositorySQLalchemy(RepositorioProducto):
    def __init__(self, session_factory: callable):
        self.session_factory = session_factory

    def _model_to_entity(self, model: ProductoModel) -> Producto:
        return Producto(
            id=str(model.id),
            nombre=model.nombre,
            precio=model.precio
        )

    def _entity_to_model(self, entity: Producto) -> ProductoModel:
        return ProductoModel(
            id=entity.id,
            nombre=entity.nombre,
            precio=entity.precio
        )

    def guardar(self, producto: Producto) -> Producto:
        with self.session_factory() as session:
            producto_model = self._entity_to_model(producto)
            
            existing = session.query(ProductoModel).get(producto.id)
            if existing:
                existing.nombre = producto_model.nombre
                existing.precio = producto_model.precio
            else:
                session.add(producto_model)
            
            session.commit()
            return self._model_to_entity(producto_model)

    def buscar_por_id(self, producto_id: str) -> Producto:
        with self.session_factory() as session:
            producto_model = session.query(ProductoModel).get(producto_id)
            if not producto_model:
                raise ProductoNoEncontradoError(producto_id=producto_id)
            return self._model_to_entity(producto_model)

    def listar_todos(self) -> list[Producto]:
        with self.session_factory() as session:
            productos_model = session.query(ProductoModel).all()
            return [self._model_to_entity(p) for p in productos_model]

    def modificar(self, producto: Producto) -> Producto:
        return self.guardar(producto)

    def borrar(self, producto_id: str) -> None:
        with self.session_factory() as session:
            producto_model = session.query(ProductoModel).get(producto_id)
            if not producto_model:
                raise ProductoNoEncontradoError(producto_id=producto_id)
            session.delete(producto_model)
            session.commit()