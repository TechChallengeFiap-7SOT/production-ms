from typing import Type, List, Dict

from src.domain.use_cases.find_pedidos import FindPedidos as FindPedidosInterface
from src.data.interfaces import PedidoRepositoryInterface as PedidoRepository
from src.domain.models import Pedidos


VALID_STATUS = ['na_fila', 'em_preparo', 'pronto', 'entregue']


class FindPedidos(FindPedidosInterface):
    def __init__(self, pedido_repository: Type[PedidoRepository]):
        self.pedido_repository = pedido_repository
        
    def by_status(self, status: List[str]) -> Dict[bool, List[Pedidos]]:
        
        valid_status = isinstance(status, list)
        
        if not valid_status:
            return {'Success': valid_status, 'Data': None}
        
        valid_list = True
        for item in status:
            if item not in status:
                valid_list = False
        
        if not valid_list:
            return {'Success': valid_list, 'Data': None}
        
        response = self.pedido_repository.get_pedidos(status=status)
        
        return {'Success': True, 'Data': response}   
