import random

from faker import Faker
from ..use_cases.find_pedidos import FindPedidos
from src.infra.test import PedidoRepositorySpy

faker = Faker()

def test_find_pedidos():
    pedido_repository = PedidoRepositorySpy()
    find_pedidos = FindPedidos(pedido_repository)

    response = find_pedidos.by_status(status=['na_fila'])
    
    assert pedido_repository.get_pedidos_params['status'] == ['na_fila']
    assert response['Success'] is True
    assert response['Data']


def test_find_pedidos_failure():
    pedido_repository = PedidoRepositorySpy()
    find_pedidos = FindPedidos(pedido_repository)

    response = find_pedidos.by_status(status='na_fila')
    
    assert pedido_repository.get_pedidos_params == {}
    assert response['Success'] is False
    assert response['Data'] is None
