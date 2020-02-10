from ...infrastructure.repositories.no_lineal_repository import noLinealRepository

class NoLinealService:
    def __init__(self, linealSimpleRepository):
        self.state = "No Lineal App Service on!!!"
        self._linealSimpleRepository = noLinealRepository

    def printState(self):
        return self.state

    def save(self):
        return self._linealSimpleRepository.save()

noLinealService = NoLinealService(noLinealRepository)
