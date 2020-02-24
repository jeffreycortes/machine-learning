from ..infrastructure.repositories.no_lineal_repository import noLinealRepository
from ..domain.no_lineal import noLineal

class NoLinealService:
    def __init__(self, linealSimpleRepository):
        self.state = "No Lineal App Service on!!!"
        self._no_lineal = noLineal
        self._linealSimpleRepository = noLinealRepository

    def printState(self):
        return self.state

    def print_cubic_chart_demo(self):
        return self._no_lineal.print_cubic_chart_demo()

    def print_quad_chart_demo(self):
        return self._no_lineal.print_quad_chart_demo()

    def print_exponential_chart_demo(self):
        return self._no_lineal.print_exponential_chart_demo()

    def print_logarithmic_chart_demo(self):
        return self._no_lineal.print_logarithmic_chart_demo()

    def print_sigmoidal_chart_demo(self):
        return self._no_lineal.print_sigmoidal_chart_demo()

    def save(self):
        return self._linealSimpleRepository.save()



noLinealService = NoLinealService(noLinealRepository)
