from typing import List

from src.domain.models import Pedidos
from src.data.interfaces import PedidoRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pedidos as PedidosModel

class PedidosRepository(PedidoRepositoryInterface):
    @classmethod
    def insert_pedido(cls, pedido_id: str, status: int) -> Pedidos:
        with DBConnectionHandler() as db_connection:
            try:
                pedido = PedidosModel(id=pedido_id, status=status)
                db_connection.session.add(pedido)
                db_connection.session.commit()
                
                return Pedidos(id=pedido_id, status=status)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            
        return None

    @classmethod
    def get_pedidos(cls, pedido_id: str = None, status: str = None) -> List[Pedidos]:
        try:
            with DBConnectionHandler() as db_connection:
                query_data = db_connection.session.query(PedidosModel)
                if pedido_id:
                    query_data = query_data.filter_by(id=pedido_id)

                if status:
                    query_data = query_data.filter(PedidosModel.status.in_(status))
                    
                response = []
                for item in query_data.all():
                    response.append(Pedidos(id=item.id, status=item.status._name_))
                
                return response
        except:
            raise
        finally:
            db_connection.session.close()
            
    @classmethod
    def update_pedido(cls, pedido_id: int, status: str) -> Pedidos:
        with DBConnectionHandler() as db_connection:
            try:
                pedido = db_connection.session.query(PedidosModel).filter_by(id=pedido_id).first()
                pedido.status = status
                db_connection.session.commit()
                
                return Pedidos(id=pedido_id, status=status)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            
        return None
