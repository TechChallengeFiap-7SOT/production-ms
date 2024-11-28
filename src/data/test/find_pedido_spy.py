from typing import Dict

class FindPedidoSpy:
    def __init__(self) -> None:
        self.find_pedidos_params = {}

    def by_status(self, status: str) -> Dict:
        self.find_pedidos_params["status"] = status

        return {
            "Success": True,
            "Data": [
                { "pedid_id": 123, "status": status }
            ]
        }
