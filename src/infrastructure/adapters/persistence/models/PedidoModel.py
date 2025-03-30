from sqlalchemy import Column, String, JSON, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PedidoModel(Base):
    """Modelo SQLAlchemy para la tabla de pedidos"""
    __tablename__ = 'pedidos'
    
    id = Column(String(36), primary_key=True)
    id_cliente = Column(String(36), nullable=False)
    direccion_entrega = Column(JSON, nullable=False)
    id_items = Column(JSON, nullable=False)
    estado = Column(String(20), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_ultima_actualizacion = Column(DateTime, default=datetime.utcnow, 
                                      onupdate=datetime.utcnow)
    total = Column(Numeric(10, 2), nullable=False)