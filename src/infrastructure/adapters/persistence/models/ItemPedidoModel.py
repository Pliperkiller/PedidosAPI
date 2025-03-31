# infrastructure/adapters/persistence/models.py
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class ItemPedidoModel(Base):
    __tablename__ = 'items_pedido'
    
    id = Column(String(36), 
             primary_key=True, 
             default=lambda: str(uuid.uuid4()))
    
    id_producto = Column(String(36), 
                       ForeignKey('productos.id'), 
                       nullable=False)
    
    cantidad = Column(Integer, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now())
    pedido_id = Column(String(36), 
                   ForeignKey('pedidos.id'), 
                   nullable=True)