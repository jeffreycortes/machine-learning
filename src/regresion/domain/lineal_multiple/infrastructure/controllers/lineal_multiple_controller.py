from ...aplication.lineal_multiple_service import linealMultipleService

class LinealMultipleController:
    def __init__(self, app, jsonify):
        
        @app.route("/api/regresion/lineal_multiple")
        def index_lineal_multiple():
            return jsonify('Hello from Regresion Lineal Múltiple')

        @app.route("/api/regresion/lineal_multiple/ping")
        def ping_lineal_multiple():
            return jsonify('Ping from ' + linealMultipleService.printState())
