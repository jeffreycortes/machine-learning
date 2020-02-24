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

        @app.route("/api/regresion/no_lineal/cubic_chart_demo")
        def no_lineal_cubic_chart_demo():
            resp = '<h5>Cubic No Lineal Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + noLinealService.print_cubic_chart_demo() + '">'
            return resp

        @app.route("/api/regresion/no_lineal/quad_chart_demo")
        def no_lineal_quad_chart_demo():
            resp = '<h5>Quad No Lineal Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + noLinealService.print_quad_chart_demo() + '">'
            return resp

        @app.route("/api/regresion/no_lineal/exponential_chart_demo")
        def no_lineal_exponential_chart_demo():
            resp = '<h5>Exponential No Lineal Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + noLinealService.print_exponential_chart_demo() + '">'
            return resp

        @app.route("/api/regresion/no_lineal/logarithmic_chart_demo")
        def no_lineal_logarithmic_chart_demo():
            resp = '<h5>Exponential No Lineal Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + noLinealService.print_logarithmic_chart_demo() + '">'
            return resp

        @app.route("/api/regresion/no_lineal/sigmoidal_chart_demo")
        def no_lineal_sigmoidal_chart_demo():
            resp = '<h5>Exponential No Lineal Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + noLinealService.print_sigmoidal_chart_demo() + '">'
            return resp

        @app.route("/api/regresion/no_lineal/demo")
        def no_lineal_demo():
            resp = '<h5>Exponential No Lineal Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + noLinealService.no_lineal_demo() + '">'
            return resp

        @app.route("/api/regresion/no_lineal/demo2")
        def no_lineal_demo2():
            resp = '<h5>Exponential No Lineal Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + noLinealService.no_lineal_demo2() + '">'
            return resp

        @app.route("/api/regresion/no_lineal/chart/sigmoid")
        def no_lineal_print_sigmoid_chart():
            resp = '<h5>Exponential No Lineal Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + noLinealService.print_sigmoid_chart() + '">'
            return resp

        @app.route("/api/regresion/no_lineal/chart/regresion_model")
        def no_lineal_print_regresion_model_chart():
            resp = '<h5>Exponential No Lineal Demo</h5>  <img alt="line chart" src="data:image/png;base64,' + noLinealService.print_regresion_model_chart() + '">'
            return resp
