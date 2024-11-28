import enum

from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.orm import relationship
from src.infra.config import Base


class StatusTypes(enum.Enum):
    na_fila = 'na_fila',
    em_preparo = 'em_preparo',
    pronto = 'pronto',
    entregue = 'entregue'

class Pedidos(Base):
    ''' Entidade de Pedidos'''

    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True)
    status = Column(Enum(StatusTypes), nullable=False)
    
    def __rep__(self):
        return f'Pedido: {self.id} - Status: {self.status}'

    def __eq__(self, other):
        if self.id == other.id and self.status == other.status:
            return True
        return False
