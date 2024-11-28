from typing import Type

from src.main.interface import RouterInteface
from src.domain.use_cases import FindPedidos
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors.http_erros import HttpErros


class FindPedidosController(RouterInteface):
    def __init__(self, find_pedidos_use_case: Type[FindPedidos]):
        self.find_pedidos_use_case = find_pedidos_use_case
        
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        if not http_request.body:
            response = HttpErros.error_400()
            return HttpResponse(status_code=response['status_code'], body=response['body'])
        
        status = http_request.body.get('status')
        
        if not status:
            response = HttpErros.error_422()
            return HttpResponse(status_code=response['status_code'], body=response['body'])
        

        response = self.find_pedidos_use_case.by_status(status=status)
        
        return HttpResponse(status_code=200, body=response['Data'])
 