from typing import Dict

from abc import ABC, abstractmethod
from src.domain.models import Pedidos

class RegisterPedido(ABC):
    
    @abstractmethod
    def register_pedido(self, id_pedido: int = None) -> Dict[bool, Pedidos]:
        raise Exception('Method not implemented')