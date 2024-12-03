import random

from faker import Faker
from .pedidos_repository import PedidosRepository
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pedidos as PedidosModel

faker = Faker()
pedido_repository = PedidosRepository()
db_connection_handler = DBConnectionHandler()

PEDIDO_STATUS = {
    1: 'na_fila',
    2: 'em_preparo',
    3: 'pronto',
    4: 'entregue'
}

def test_pedido_repository():
    pedido_id = str(random.randint(0, 9999))
    status = faker.name()
    engine = db_connection_handler.get_engine()

    pedido_repository.insert_pedido(pedido_id, status)
    pedido = engine.execute(f"SELECT * FROM pedidos WHERE id = '{pedido_id}'").first()
    
    engine.execute(f"DELETE FROM pedidos WHERE id = '{pedido_id}'")
    
    assert pedido.id == pedido_id
    assert pedido.status == status


def test_get_pedidos():
    pedido_id = str(random.randint(0, 9999))
    status = random.randint(1, 4)
    status = PEDIDO_STATUS[status]
    
    
    data = PedidosModel(id=pedido_id, status=status)
    
    engine = db_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO pedidos VALUES('{pedido_id}', '{status}')"
    )
    
    query_pedido_id = pedido_repository.get_pedidos(pedido_id=pedido_id)
    query_pedido_status = pedido_repository.get_pedidos(status=[status])
    query_pedido = pedido_repository.get_pedidos(pedido_id=pedido_id, status=[status])

    assert data in query_pedido_id
    assert data in query_pedido_status
    assert data in query_pedido


def test_update_pedido():
    pedido_id = str(random.randint(0, 9999))
    status = random.randint(1, 4)
    status = PEDIDO_STATUS[status]
    new_status = random.randint(1, 4)
    new_status = PEDIDO_STATUS[new_status]

    engine = db_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO pedidos VALUES('{pedido_id}', '{status}')"
    )
    
    pedido_repository.update_pedido(pedido_id=pedido_id, status=new_status)
    
    pedido = engine.execute(f"SELECT * FROM pedidos WHERE id = '{pedido_id}'").first()
    
    assert pedido.id == pedido_id
    assert pedido.status == new_status
    
    engine.execute(f"DELETE FROM pedidos WHERE id = '{pedido_id}'")
