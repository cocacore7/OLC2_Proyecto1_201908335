from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol


class Environment:

    def __init__(self, father):
        # Usamos un diccionario para nuestra tabla de simbolos, guardara el id como clave y como cuerpo un simbolo
        self.variable = {}
        self.function = {}
        # Father es el entorno exterior al cual podemos acceder
        self.father = father

    def getGlobal(self):
        tempEnv: Environment = self;
        while tempEnv.father is not None:
            tempEnv = tempEnv.father
        return tempEnv

    def saveVariable(self, id: str, value, type: typeExpression, isArray: bool):
        tempEnv = self
        while tempEnv is not None:
            if tempEnv.variable.get(id) is not None:
                tempVar: Symbol = tempEnv.variable.get(id)
                if tempVar.getType() == value.getType().value:
                    tempVar.value = value
                    self.variable[id] = tempVar
                    return
                else:
                    # CASTEOS IMPLICITOS
                    print("Error: la variable " + id + " no puede ser cambiada de tipo")
                    return
            tempEnv = tempEnv.father
        tempVar = Symbol(id, value, type)
        tempVar.array = isArray
        self.variable[id] = tempVar

    def getVariable(self, id: str) -> Symbol:
        tempEnv = self
        while tempEnv is not None:
            if tempEnv.variable.get(id) is not None:
                return tempEnv.variable.get(id).getValue()
            tempEnv = tempEnv.father
        print("Error: la variable " + id + " no existe")
        return None

    def saveFunction(self, id: str, function):
        if self.function.get(id) is not None:
            print("La función " + id + " ya existe")
            return
        self.function[id] = function

    def getFunction(self, id: str):
        tempEnv = self
        while tempEnv is not None:
            if tempEnv.function.get(id) is not None:
                return tempEnv.function.get(id)
            tempEnv = tempEnv.father
        print("Error: la función " + id + " no existe")
        return None
