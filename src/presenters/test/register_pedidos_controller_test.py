from src.presenters.controllers.register_pedidos import RegisterPedidosController
from src.data.test.register_pedidos_spy import RegisterPedidosSpy
from src.presenters.helpers import HttpRequest

 
def test_handler():
    register_pedido_use_case = RegisterPedidosSpy()
    register_pedido_controller = RegisterPedidosController(register_pedido_use_case)
    
    http_request = HttpRequest(body={'pedido_id': 123})
    
    response = register_pedido_controller.handle(http_request)

    assert register_pedido_use_case.register_pedidos_params['pedido_id'] == 123
    assert response.status_code == 200
    assert response.body

def test_handler_no_query_error():
    register_pedido_use_case = RegisterPedidosSpy()
    register_pedido_controller = RegisterPedidosController(register_pedido_use_case)
    
    http_request = HttpRequest()
    
    response = register_pedido_controller.handle(http_request)

    assert register_pedido_use_case.register_pedidos_params == {}
    assert response.status_code == 400
    assert response.body['error'] == 'Bad Request'

def test_handler_no_status_error():
    register_pedido_use_case = RegisterPedidosSpy()
    register_pedido_controller = RegisterPedidosController(register_pedido_use_case)
    
    http_request = HttpRequest(body={'wrong_body': 'na_fila'})
    
    response = register_pedido_controller.handle(http_request)

    assert register_pedido_use_case.register_pedidos_params == {}
    assert response.status_code == 422
    assert response.body['error'] == 'Unprocessable Entity'
