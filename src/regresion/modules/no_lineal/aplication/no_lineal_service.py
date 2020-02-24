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

    def no_lineal_demo(self):
        return self._no_lineal.no_lineal_demo()

    def no_lineal_demo2(self):
        return self._no_lineal.no_lineal_demo2()

    def print_sigmoid_chart(self):
        beta_1 = 0.10
        beta_2 = 1990.0

        return self._no_lineal.print_sigmoid_chart(beta_1, beta_2)

    def print_regresion_model_chart(self):
        beta_1 = 0.10
        beta_2 = 1990.0

        return self._no_lineal.print_regresion_model_chart(beta_1, beta_2)

    def save(self):
        return self._linealSimpleRepository.save()



noLinealService = NoLinealService(noLinealRepository)
