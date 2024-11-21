import random

from faker import Faker
from .pedidos_repository import PedidosRepository
from src.infra.config import DBConnectionHandler

faker = Faker()
pedido_repository = PedidosRepository()
db_connection_handler = DBConnectionHandler()

def test_pedido_repository():
    pedido_id = random.randint(0, 9999)
    status = faker.name()
    engine = db_connection_handler.get_engine()

    pedido_repository.insert_pedido(pedido_id, status)
    pedido = engine.execute(f'SELECT * FROM pedidos WHERE id = {pedido_id}').fetchone()
    
    engine.execute(f'DELETE FROM pedidos WHERE id = {pedido_id}')
    
    assert pedido.id == pedido_id
    assert pedido.status == status
