from ..infrastructure.repositories.lineal_simple_repository import linealSimpleRepository
from ..domain.lineal_simple import linealSimple

class LinealSimpleService:
    def __init__(self, linealSimple, linealSimpleRepository):
        self.state = "Lineal Simple App Service on!!!"
        self._lineal_simple = linealSimple
        self._linealSimpleRepository = linealSimpleRepository

    def printState(self):
        return self.state

    def print_demo_chart(self):
        return self._lineal_simple.print_demo_chart()

    def save(self):
        return self._linealSimpleRepository.save()

linealSimpleService = LinealSimpleService(linealSimple, linealSimpleRepository)
