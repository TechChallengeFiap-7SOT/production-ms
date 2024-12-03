from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pedidos

class PedidoRepositoryInterface(ABC):
    @abstractmethod
    def insert_pedido(self, id: str, status: int) -> Pedidos:
        raise Exception('Method not implemented')
    
    @abstractmethod
    def get_pedidos(self, pedido_id: str = None, status: str = None) -> List[Pedidos]:
        raise Exception('Method not implemented')
    
    @abstractmethod
    def update_pedido(cls, pedido_id: str, status: str) -> Pedidos:
        raise Exception('Method not implemented')
