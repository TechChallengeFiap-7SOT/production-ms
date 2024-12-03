from typing import Dict

class UpdatePedidoSpy:
    def __init__(self) -> None:
        self.update_pedido_params = {}

    def by_id(self, pedido_id: str, status: str) -> Dict:
        self.update_pedido_params["pedido_id"] = pedido_id
        self.update_pedido_params["status"] = status

        return {
            "Success": True,
            "Data": [
                { "pedido_id": pedido_id, "status": status }
            ]
        }
