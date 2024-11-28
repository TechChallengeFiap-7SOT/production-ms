from typing import Dict

class RegisterPedidosSpy:
    def __init__(self) -> None:
        self.register_pedidos_params = {}

    def register_pedido(self, pedido_id: int) -> Dict:
        self.register_pedidos_params["pedido_id"] = pedido_id

        return {
            "Success": True,
            "Data": [
                { "pedido_id": pedido_id, "status": 'na_fila' }
            ]
        }
