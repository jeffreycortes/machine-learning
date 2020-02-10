from ..rest_client.app import app, jsonify
from ...aplication.services.lineal_multiple_service import linealMultipleService

class LinealMultipleController:
    @app.route("/api/regresion/lineal_multiple")
    def index_lineal_multiple():
        return jsonify('Hello from Regresion Lineal Múltiple')

    @app.route("/api/regresion/lineal_multiple/ping")
    def ping_lineal_multiple():
        return jsonify('Ping from ' + linealMultipleService.printState())
