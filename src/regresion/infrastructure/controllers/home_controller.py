from .api_controller import ApiController

class HomeController(ApiController):
    def __init__(self):
        ApiController.__init__(self)

    def _register_route_map(self, app, jsonify):
        print('HomeController __register_route_map')
        @app.route("/")
        def index():
            return jsonify('Hello from Index')

        @app.route("/api")
        def indexAPI():
            return jsonify('Hello from API')
