import random

from faker import Faker
from ..use_cases.update_pedido import UpdatePedido
from src.infra.test import PedidoRepositorySpy

faker = Faker()


def test_update_pedido():
    pedido_repository = PedidoRepositorySpy()
    update_pedido = UpdatePedido(pedido_repository)

    pedido_id = random.randint(0, 9999)

    response = update_pedido.by_id(pedido_id=pedido_id, status='na_fila')
    
    assert pedido_repository.update_pedido_params['pedido_id'] == pedido_id
    assert pedido_repository.update_pedido_params['status'] == 'na_fila'
    assert response['Success'] is True
    assert response['Data']


def test_find_pedidos_failure():
    pedido_repository = PedidoRepositorySpy()
    update_pedido = UpdatePedido(pedido_repository)

    pedido_id = random.randint(0, 9999)

    response = update_pedido.by_id(pedido_id=pedido_id, status=['na_fila'])
    
    assert pedido_repository.update_pedido_params == {}
    assert response['Success'] is False
    assert response['Data'] is None
