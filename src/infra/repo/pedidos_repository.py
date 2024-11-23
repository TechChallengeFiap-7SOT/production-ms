from typing import List

from src.domain.models import Pedidos
from src.data.interfaces import PedidoRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pedidos as PedidosModel

class PedidosRepository(PedidoRepositoryInterface):
    @classmethod
    def insert_pedido(cls, id: int, status: int) -> Pedidos:
        with DBConnectionHandler() as db_connection:
            try:
                pedido = PedidosModel(id=id, status=status)
                db_connection.session.add(pedido)
                db_connection.session.commit()
                
                return Pedidos(id=id, status=status)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get_pedidos(cls, pedido_id: int = None, status: str = None) -> List[Pedidos]:
        try:
            with DBConnectionHandler() as db_connection:
                query_data = db_connection.session.query(PedidosModel)
                if pedido_id:
                    query_data = query_data.filter_by(id=pedido_id)

                if status:
                    query_data = query_data.filter_by(status=status)
                
                return query_data.all()
        except:
            raise
        finally:
            db_connection.session.close()
        