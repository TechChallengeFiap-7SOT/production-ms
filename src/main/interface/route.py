from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RouterInteface(ABC):
    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        raise Exception('Method not implemented')
