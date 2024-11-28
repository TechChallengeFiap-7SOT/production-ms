from src.main.interface import RouterInteface
from src.presenters.controllers import FindPedidosController
from src.data.use_cases import FindPedidos
from src.infra.repo.pedidos_repository import PedidosRepository


def find_pedidos_composer() -> RouterInteface:
    repository = PedidosRepository()
    use_case = FindPedidos(repository)
    find_pedido_route = FindPedidosController(use_case)
    
    return find_pedido_route
