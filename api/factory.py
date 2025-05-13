from abc import ABC, abstractmethod

class Endpoint(ABC):
    @abstractmethod
    def get_data(self, **kwargs):
        pass

class EndpointFactory:
    @staticmethod
    def create_endpoint(name):
        if name == "leagues":
            from .leagues import LeaguesEndpoint
            return LeaguesEndpoint()
        raise ValueError(f"Unknown endpoint: {name}")
