from typing import Dict, List

from abc import ABC, abstractmethod
from src.domain.models import Pedidos


class UpdatePedidos(ABC):
    
    @abstractmethod
    def by_id(self, pedido_id: int, status: str) -> Dict[bool, Pedidos]:
        raise Exception('Method not implemented') 
