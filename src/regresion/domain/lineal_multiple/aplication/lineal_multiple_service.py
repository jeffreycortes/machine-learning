from ..infrastructure.repositories.lineal_multiple_repository import linealMultipleRepository

class LinealMultipleService:
    def __init__(self, linealSimpleRepository):
        self.state = "Lineal Múltiple App Service on!!!"
        self._linealSimpleRepository = linealMultipleRepository

    def printState(self):
        return self.state

    def save(self):
        return self._linealSimpleRepository.save()

linealMultipleService = LinealMultipleService(linealMultipleRepository)
