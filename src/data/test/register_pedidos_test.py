import random

from faker import Faker
from ..use_cases.register_pedidos import RegisterPedido
from src.infra.test import PedidoRepositorySpy

faker = Faker()

def test_register():
    pedido_repository = PedidoRepositorySpy()
    register_pedido = RegisterPedido(pedido_repository)
    
    pedido_id = random.randint(0, 9999)

    response = register_pedido.register_pedido(pedido_id=pedido_id)
    
    assert pedido_repository.insert_pedido_params['id'] == pedido_id
    assert response['Success'] is True
    assert response['Data']


def test_register_failure():
    pedido_repository = PedidoRepositorySpy()
    register_pedido = RegisterPedido(pedido_repository)
    
    pedido_id = 'not int'

    response = register_pedido.register_pedido(pedido_id=pedido_id)
    
    assert pedido_repository.insert_pedido_params == {}
    assert response['Success'] is False
    assert response['Info'] == 'pedido_id must be a integer'
