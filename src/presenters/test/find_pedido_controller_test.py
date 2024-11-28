from src.presenters.controllers.find_pedido_controller import FindPedidosController
from src.data.test.find_pedido_spy import FindPedidoSpy
from src.presenters.helpers import HttpRequest

 
def test_handler():
    find_pedido_use_case = FindPedidoSpy()
    find_pedido_controller = FindPedidosController(find_pedido_use_case)
    
    http_request = HttpRequest(body={'status': ['na_fila']})
    
    response = find_pedido_controller.handle(http_request)

    assert find_pedido_use_case.find_pedidos_params['status'] == ['na_fila']
    assert response.status_code == 200
    assert response.body

def test_handler_no_query_error():
    find_pedido_use_case = FindPedidoSpy()
    find_pedido_controller = FindPedidosController(find_pedido_use_case)
    
    http_request = HttpRequest()
    
    response = find_pedido_controller.handle(http_request)

    assert find_pedido_use_case.find_pedidos_params == {}
    assert response.status_code == 400
    assert response.body['error'] == 'Bad Request'

def test_handler_no_status_error():
    find_pedido_use_case = FindPedidoSpy()
    find_pedido_controller = FindPedidosController(find_pedido_use_case)
    
    http_request = HttpRequest(body={'wrong_status': 'na_fila'})
    
    response = find_pedido_controller.handle(http_request)

    assert find_pedido_use_case.find_pedidos_params == {}
    assert response.status_code == 422
    assert response.body['error'] == 'Unprocessable Entity'
