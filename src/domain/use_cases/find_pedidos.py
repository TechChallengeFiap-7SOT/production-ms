from typing import Dict, List

from abc import ABC, abstractmethod
from src.domain.models import Pedidos


class FindPedidos(ABC):
    
    @abstractmethod
    def by_status(self, status: List[str]) -> Dict[bool, List[Pedidos]]:
        raise Exception('Method not implemented') 
