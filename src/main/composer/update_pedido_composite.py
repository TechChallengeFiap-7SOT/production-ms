from src.main.interface import RouterInteface
from src.presenters.controllers import UpdatePedidoController
from src.data.use_cases import UpdatePedido
from src.infra.repo.pedidos_repository import PedidosRepository


def update_pedido_composer() -> RouterInteface:
    repository = PedidosRepository()
    use_case = UpdatePedido(repository)
    update_pedido_route = UpdatePedidoController(use_case)
    
    return update_pedido_route
