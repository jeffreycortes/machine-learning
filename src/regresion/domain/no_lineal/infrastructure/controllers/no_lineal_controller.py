from ...aplication.no_lineal_service import noLinealService

class NoLinealController:
    def __init__(self, app, jsonify):
        self.__register_route_map(app, jsonify)

    def __register_route_map(self, app, jsonify):
        @app.route("/api/regresion/no_lineal")
        def index_no_lineal():
            return jsonify('Hello from Regresion No Lineal')

        @app.route("/api/regresion/no_lineal/ping")
        def ping_no_lineal():
            return jsonify('Ping from ' + noLinealService.printState())
