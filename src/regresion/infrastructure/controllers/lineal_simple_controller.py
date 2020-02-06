from ..rest_client.app import app, jsonify
from ...aplication.services.lineal_simple_service import linealSimpleService

class LinealSimpleController:
    @app.route("/api/regresion/lineal_simple")
    def index_lineal_simple():
        return jsonify('Hello from Regresion Lineal Simple')

    @app.route("/api/regresion/lineal_simple/ping")
    def ping_lineal_simple():
        return jsonify('Ping from ' + linealSimpleService.printState())
