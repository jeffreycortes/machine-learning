from ..rest_client.app import app, jsonify
from ...aplication.services.no_lineal_service import noLinealService

class NoLinealController:
    @app.route("/api/regresion/no_lineal")
    def index_no_lineal():
        return jsonify('Hello from Regresion No Lineal')

    @app.route("/api/regresion/no_lineal/ping")
    def ping_no_lineal():
        return jsonify('Ping from ' + noLinealService.printState())
