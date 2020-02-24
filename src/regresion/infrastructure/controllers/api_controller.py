from abc import ABC, abstractmethod
from ..rest_client.app import app, jsonify

class ApiController(ABC):
    def __init__(self, app = app, jsonify = jsonify):
        self._register_route_map(app, jsonify)

    @abstractmethod
    def _register_route_map(self, app, jsonify):
        # EN: Implement the route assignment in your controller by overwriting this method.
        # ES: Implemente la asignación de ruta en su controlador sobreescribiendo este método.
        pass
