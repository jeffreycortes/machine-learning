from src.regresion.infrastructure.controllers.api_controller import ApiController
from ...aplication.no_lineal_service import noLinealService

class NoLinealController(ApiController):
    def __init__(self):
        ApiController.__init__(self)

    def _register_route_map(self, app, jsonify):
        @app.route("/api/regresion/no_lineal")
        def index_no_lineal():
            return jsonify('Hello from Regresion No Lineal')

        @app.route("/api/regresion/no_lineal/ping")
        def ping_no_lineal():
            return jsonify('Ping from ' + noLinealService.printState())
