from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol


class Environment:

    def __init__(self, father) -> None:
        self.father = father
        self.variable = {}
        self.size = 0

        if father is not None:
            self.size = father.size

    def saveVariable(self, id: str, type: typeExpression):
        if self.variable.get(id) is not None:
            print("La variable " + id + " ya existe")
            return

        tempVar = Symbol(id, type, self.size)
        self.size = self.size + 1
        self.variable[id] = tempVar
        return tempVar

    def getVariable(self, id: str) -> Symbol:
        tempEnv = self
        while tempEnv is not None:
            if tempEnv.variable.get(id) is not None:
                return tempEnv.variable.get(id)
            tempEnv = tempEnv.father
        print("Error: la variable " + id + " no existe")
        return None
