from typing import Type, Dict

from src.domain.use_cases import RegisterPedido as RegisterPedidosInterface
from src.data.interfaces import PedidoRepositoryInterface as PedidoRepository
from src.domain.models import Pedidos

class RegisterPedido(RegisterPedidosInterface):
    def __init__(self, pedido_repository: Type[PedidoRepository]):
        self.pedido_repository = pedido_repository

    def register_pedido(self, pedido_id: int) -> Dict[bool, Pedidos]:
        validate_id = isinstance(pedido_id, int)
        
        if not validate_id:
            return {'Success': False, 'Info': 'pedido_id must be a integer'}
        
        response = self.pedido_repository.insert_pedido(pedido_id, "na_fila")
        
        if not response:
            return {'Success': False, 'Info': f'error while inserting id: {pedido_id}'}
        
        return {'Success': validate_id, 'Data': response}
