from ..rest_client.app import app, jsonify
from ...domain.lineal_simple.infrastructure.controllers.lineal_simple_controller import LinealSimpleController
from ...domain.lineal_multiple.infrastructure.controllers.lineal_multiple_controller import LinealMultipleController
from ...domain.no_lineal.infrastructure.controllers.no_lineal_controller import NoLinealController

LinealSimpleController(app, jsonify)
LinealMultipleController(app, jsonify)
NoLinealController(app, jsonify)
