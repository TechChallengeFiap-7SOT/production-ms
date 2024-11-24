import random

from faker import Faker
from src.domain.models import Pedidos

faker = Faker()

def mock_pedido() -> Pedidos:
    return Pedidos(id=random.randint(0, 9999), status='na_fila')
