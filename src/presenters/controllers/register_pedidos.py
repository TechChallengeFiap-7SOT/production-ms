from typing import Type

from src.main.interface import RouterInteface
from src.domain.use_cases import RegisterPedido
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors.http_erros import HttpErros


class RegisterPedidosController(RouterInteface):
    def __init__(self, register_pedidos_use_case: Type[RegisterPedido]):
        self.register_pedidos_use_case = register_pedidos_use_case
        
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        if not http_request.body:
            response = HttpErros.error_400()
            return HttpResponse(status_code=response['status_code'], body=response['body'])
        
        pedido_id = http_request.body.get('pedido_id')

        if not pedido_id:
            response = HttpErros.error_422()
            return HttpResponse(status_code=response['status_code'], body=response['body'])
        

        response = self.register_pedidos_use_case.register_pedido(pedido_id=pedido_id)
        
        return HttpResponse(status_code=200, body=response['Data'])
 