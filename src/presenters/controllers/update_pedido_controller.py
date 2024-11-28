from typing import Type

from src.main.interface import RouterInteface
from src.domain.use_cases import UpdatePedidos
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors.http_erros import HttpErros


class UpdatePedidoController(RouterInteface):
    def __init__(self, update_pedido_use_case: Type[UpdatePedidos]):
        self.update_pedido_use_case = update_pedido_use_case
        
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        if not http_request.body:
            response = HttpErros.error_400()
            return HttpResponse(status_code=response['status_code'], body=response['body'])
        
        pedido_id = http_request.body.get('pedido_id')
        status = http_request.body.get('status')

        if not pedido_id or not status:
            response = HttpErros.error_422()
            return HttpResponse(status_code=response['status_code'], body=response['body'])

        response = self.update_pedido_use_case.by_id(pedido_id=pedido_id, status=status)
        
        return HttpResponse(status_code=200, body=response['Data'])
 