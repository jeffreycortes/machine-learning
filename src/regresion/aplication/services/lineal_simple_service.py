class LinealSimpleService:
    state = "Lineal Simple App Service"

    def __init__(self):
        self.state += " on!!!"

    def printState(self):
        return self.state
