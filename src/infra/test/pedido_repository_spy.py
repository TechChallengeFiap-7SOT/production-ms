from typing import List

from src.domain.models import Pedidos
from src.domain.test import mock_pedido


class PedidoRepositorySpy:
    def __init__(self):
        self.insert_pedido_params = {}
        self.get_pedidos_params = {}
        self.update_pedido_params = {}
        
    def insert_pedido(self, id: int, status: int) -> Pedidos:
        self.insert_pedido_params['id'] = id
        self.insert_pedido_params['status'] = status

        return mock_pedido()
    
    def get_pedidos(self, pedido_id: int = None, status: str = None) -> List[Pedidos]:
        self.get_pedidos_params['pedido_id'] = pedido_id
        self.get_pedidos_params['status'] = status
        
        return [mock_pedido()]
        
    def update_pedido(self, pedido_id: int, status: str) -> Pedidos:
        self.update_pedido_params['pedido_id'] = pedido_id
        self.update_pedido_params['status'] = status
        
        return mock_pedido()
