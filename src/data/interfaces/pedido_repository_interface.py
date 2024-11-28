from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pedidos

class PedidoRepositoryInterface(ABC):
    @abstractmethod
    def insert_pedido(self, id: int, status: int) -> Pedidos:
        raise Exception('Method not implemented')
    
    @abstractmethod
    def get_pedidos(self, pedido_id: int = None, status: str = None) -> List[Pedidos]:
        raise Exception('Method not implemented')
    
    @abstractmethod
    def update_pedido(cls, pedido_id: int, status: str) -> Pedidos:
        raise Exception('Method not implemented')
