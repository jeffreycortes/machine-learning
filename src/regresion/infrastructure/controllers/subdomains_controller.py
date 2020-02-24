from .api_controller import ApiController
from ...modules.lineal_simple.infrastructure.controllers.lineal_simple_controller import LinealSimpleController
from ...modules.lineal_multiple.infrastructure.controllers.lineal_multiple_controller import LinealMultipleController
from ...modules.no_lineal.infrastructure.controllers.no_lineal_controller import NoLinealController

class SubdomainsController(ApiController):
    def __init__(self):
        ApiController.__init__(self)

    def _register_route_map(self, app, jsonify):
        LinealSimpleController()
        LinealMultipleController()
        NoLinealController()
