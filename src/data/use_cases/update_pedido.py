from typing import Type, Dict

from src.domain.use_cases.update_pedido import UpdatePedidos as UpdatePedidosInterface
from src.data.interfaces import PedidoRepositoryInterface as PedidoRepository
from src.domain.models import Pedidos


VALID_STATUS = ['na_fila', 'em_preparo', 'pronto', 'entregue']


class UpdatePedido(UpdatePedidosInterface):
    def __init__(self, pedido_repository: Type[PedidoRepository]):
        self.pedido_repository = pedido_repository
        
    def by_id(self, pedido_id: str, status: str) -> Dict[bool, Pedidos]:
        
        valid_input = isinstance(status, str) and isinstance(pedido_id, str) and status in VALID_STATUS

        if not valid_input:
            return {'Success': valid_input, 'Data': None}
        
        response = self.pedido_repository.update_pedido(pedido_id=pedido_id, status=status)
        
        return {'Success': True, 'Data': response}
