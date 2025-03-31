# infrastructure/adapters/persistence/models.py
from sqlalchemy import Column, String, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class ProductoModel(Base):
    __tablename__ = 'productos'
    

    id = Column(UUID(as_uuid=True), 
                primary_key=True, 
                default=uuid.uuid4, 
                unique=True, 
                nullable=False)
        
    nombre = Column(String(100), 
                nullable=False, 
                index=True)
    
    precio = Column(Numeric(10, 2),
                nullable=False)