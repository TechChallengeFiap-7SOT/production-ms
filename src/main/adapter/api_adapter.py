from typing import Type
from src.main.interface import RouterInteface as Route
from src.presenters.helpers import HttpRequest


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    
    http_request = HttpRequest(body=request.json, query=request.args)
    response = api_route.handle(http_request)
    
    return response
