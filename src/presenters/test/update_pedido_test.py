from src.presenters.controllers.update_pedido_controller import UpdatePedidoController
from src.data.test.update_pedido_spy import UpdatePedidoSpy
from src.presenters.helpers import HttpRequest

 
def test_handler():
    update_pedido_use_case = UpdatePedidoSpy()
    update_pedido_controller = UpdatePedidoController(update_pedido_use_case)
    
    http_request = HttpRequest(body={'pedido_id': 123, 'status': 'em_preparo'})
    
    response = update_pedido_controller.handle(http_request)

    assert update_pedido_use_case.update_pedido_params['pedido_id'] == 123
    assert update_pedido_use_case.update_pedido_params['status'] == 'em_preparo'
    assert response.status_code == 200
    assert response.body

def test_handler_no_query_error():
    update_pedido_use_case = UpdatePedidoSpy()
    update_pedido_controller = UpdatePedidoController(update_pedido_use_case)
    
    http_request = HttpRequest()
    
    response = update_pedido_controller.handle(http_request)

    assert update_pedido_use_case.update_pedido_params == {}
    assert response.status_code == 400
    assert response.body['error'] == 'Bad Request'

def test_handler_no_status_error():
    update_pedido_use_case = UpdatePedidoSpy()
    update_pedido_controller = UpdatePedidoController(update_pedido_use_case)
    
    http_request = HttpRequest(body={'wrong_body': 'na_fila'})
    
    response = update_pedido_controller.handle(http_request)

    assert update_pedido_use_case.update_pedido_params == {}
    assert response.status_code == 422
    assert response.body['error'] == 'Unprocessable Entity'
