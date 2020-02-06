from ...infrastructure.repositories.lineal_simple_repository import linealSimpleRepository

class LinealSimpleService:
    def __init__(self, linealSimpleRepository):
        self.state = "Lineal Simple App Service on!!!"
        self._linealSimpleRepository = linealSimpleRepository

    def printState(self):
        return self.state

    def save(self):
        return self._linealSimpleRepository.save()

linealSimpleService = LinealSimpleService(linealSimpleRepository)
