from src.regresion.infrastructure.controllers.api_controller import ApiController
from ...aplication.lineal_simple_service import linealSimpleService

class LinealSimpleController(ApiController):
    def __init__(self):
        ApiController.__init__(self)

    def _register_route_map(self, app, jsonify):
        @app.route("/api/regresion/lineal_simple")
        def index_lineal_simple():
            return jsonify('Hello from Regresion Lineal Simple')

        @app.route("/api/regresion/lineal_simple/ping")
        def ping_lineal_simple():
            return jsonify('Ping from ' + linealSimpleService.printState())

        @app.route("/api/regresion/lineal_simple/demo_chart")
        def lineal_demo_chart():
            resp = '<h5>Chart Line Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + linealSimpleService.print_demo_chart() + '">'
            return resp
