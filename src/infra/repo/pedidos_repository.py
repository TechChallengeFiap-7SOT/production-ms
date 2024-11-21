from src.infra.config import DBConnectionHandler
from src.infra.entities import Pedidos

class PedidosRepository:
    
    @classmethod
    def insert_pedido(cls, id: int, status: int):
        with DBConnectionHandler() as db_connection:
            try:
                pedido = Pedidos(id=id, status=status)
                db_connection.session.add(pedido)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
