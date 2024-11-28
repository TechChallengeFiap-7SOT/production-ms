from src.main.interface import RouterInteface
from src.presenters.controllers import RegisterPedidosController
from src.data.use_cases import RegisterPedido
from src.infra.repo.pedidos_repository import PedidosRepository


def register_pedido_composer() -> RouterInteface:
    repository = PedidosRepository()
    use_case = RegisterPedido(repository)
    register_pedido_route = RegisterPedidosController(use_case)
    
    return register_pedido_route
    