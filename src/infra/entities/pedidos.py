import enum

from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.orm import relationship
from src.infra.config import Base


class StatusTypes(enum.Enum):
    na_fila = 'Na fila',
    em_preparo = 'Em preparo',
    pronto = 'Pronto',
    entregue = 'Entregue'

class Pedidos(Base):
    ''' Entidade de Pedidos'''

    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True)
    status = Column(Enum(StatusTypes), nullable=False)
    
    def __rep__(self):
        return f'Pedido: {self.id} - Status: {self.status}'
