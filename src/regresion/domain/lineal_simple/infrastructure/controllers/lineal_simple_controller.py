from ...aplication.lineal_simple_service import linealSimpleService

class LinealSimpleController:
    def __init__(self, app, jsonify):

        @app.route("/api/regresion/lineal_simple")
        def index_lineal_simple():
            return jsonify('Hello from Regresion Lineal Simple')

        @app.route("/api/regresion/lineal_simple/ping")
        def ping_lineal_simple():
            return jsonify('Ping from ' + linealSimpleService.printState())
