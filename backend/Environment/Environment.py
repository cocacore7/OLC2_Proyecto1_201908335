from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol


class Environment:

    def __init__(self, father):
        # Usamos un diccionario para nuestra tabla de simbolos, Funciones Creadas, Accesos locales y glovales
        self.variable = {}
        self.function = {}
        self.globalAccess = {}
        self.localAccess = {}
        # Father es el entorno exterior al cual podemos acceder
        self.father = father

    def getGlobal(self):
        tempEnv: Environment = self
        while tempEnv.father is not None:
            tempEnv = tempEnv.father
        return tempEnv

    def saveVariable(self, id: str, value, type: typeExpression, isArray: bool, entorno: str, tipoD: str):
        if self.father is not None:
            if tipoD == "F":
                if entorno == "G":
                    globalenv = self.getGlobal()
                    if globalenv.variable.get(id) is not None:
                        tempVar: Symbol = globalenv.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        globalenv.variable[id] = tempVar
                        self.globalAccess[id] = id
                        if self.variable.get(id) is not None:
                            del self.variable[id]
                        return
                    tempVar = Symbol(id, value, type)
                    tempVar.array = isArray
                    globalenv.variable[id] = tempVar
                    self.globalAccess[id] = id
                    if self.variable.get(id) is not None:
                        del self.variable[id]
                    return
                elif entorno == "L":
                    if self.globalAccess.get(id) is None:
                        if self.variable.get(id) is not None:
                            tempVar: Symbol = self.variable.get(id)
                            tempVar.value = value
                            tempVar.type = value.getType()
                            tempVar.array = value.isArray()
                            self.variable[id] = tempVar
                            return
                        tempVar = Symbol(id, value, type)
                        tempVar.array = isArray
                        self.variable[id] = tempVar
                        return
                    else:
                        globalenv = self.getGlobal()
                        tempVar: Symbol = globalenv.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        globalenv.variable[id] = tempVar
                        return
            elif tipoD == "C":
                if entorno == "G":
                    if self.localAccess.get(id) is None:
                        tempEnv = self.father
                        while tempEnv is not None:
                            if tempEnv.variable.get(id) is not None:
                                tempVar: Symbol = tempEnv.variable.get(id)
                                tempVar.value = value
                                tempVar.type = value.getType()
                                tempVar.array = value.isArray()
                                tempEnv.variable[id] = tempVar
                                return
                            tempEnv = tempEnv.father
                        globalenv = self.getGlobal()
                        tempVar = Symbol(id, value, type)
                        tempVar.array = isArray
                        globalenv.variable[id] = tempVar
                        return
                    else:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        self.variable[id] = tempVar
                        return
                elif entorno == "L":
                    if self.variable.get(id) is not None:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        self.variable[id] = tempVar
                        self.localAccess[id] = id
                        return
                    tempVar = Symbol(id, value, type)
                    tempVar.array = isArray
                    self.variable[id] = tempVar
                    self.localAccess[id] = id
                    return
        else:
            if self.variable.get(id) is not None:
                tempVar: Symbol = self.variable.get(id)
                tempVar.value = value
                tempVar.type = value.getType()
                tempVar.array = value.isArray()
                self.variable[id] = tempVar
                return
            tempVar = Symbol(id, value, type)
            tempVar.array = isArray
            self.variable[id] = tempVar

    def alterArray(self, id: str, value, entorno: str, tipoD: str):
        if self.father is not None:
            if tipoD == "F":
                if entorno == "G":
                    globalenv = self.getGlobal()
                    if globalenv.variable.get(id) is not None:
                        tempVar: Symbol = globalenv.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        globalenv.variable[id] = tempVar
                        self.globalAccess[id] = id
                        if self.variable.get(id) is not None:
                            del self.variable[id]
                    else:
                        print("Arreglo: " + id + ", No Existe")
                elif entorno == "L":
                    if self.globalAccess.get(id) is None:
                        if self.variable.get(id) is not None:
                            tempVar: Symbol = self.variable.get(id)
                            tempVar.value = value
                            tempVar.type = value.getType()
                            tempVar.array = value.isArray()
                            self.variable[id] = tempVar
                        else:
                            print("Arreglo: " + id + ", No Existe")
                    else:
                        globalenv = self.getGlobal()
                        tempVar: Symbol = globalenv.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        globalenv.variable[id] = tempVar
            elif tipoD == "C":
                if entorno == "G":
                    if self.localAccess.get(id) is None:
                        tempEnv = self.father
                        while tempEnv is not None:
                            if tempEnv.variable.get(id) is not None:
                                tempVar: Symbol = tempEnv.variable.get(id)
                                tempVar.value = value
                                tempVar.type = value.getType()
                                tempVar.array = value.isArray()
                                tempEnv.variable[id] = tempVar
                                return
                            tempEnv = tempEnv.father
                        print("Arreglo: " + id + ", No Existe")
                    else:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        self.variable[id] = tempVar
                elif entorno == "L":
                    if self.variable.get(id) is not None:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        self.variable[id] = tempVar
                        self.localAccess[id] = id
                    else:
                        print("Arreglo: " + id + ", No Existe")
        else:
            if self.variable.get(id) is not None:
                tempVar: Symbol = self.variable.get(id)
                tempVar.value = value
                tempVar.type = value.getType()
                tempVar.array = value.isArray()
                self.variable[id] = tempVar
            else:
                print("Arreglo: " + id + ", No Existe")
        return

    def PopPushArray(self, id: str, value):
        tempEnv = self
        while tempEnv is not None:
            if tempEnv.variable.get(id) is not None:
                tempVar: Symbol = self.variable.get(id)
                tempVar.value = value
                tempVar.type = value.getType()
                tempVar.array = value.isArray()
                self.variable[id] = tempVar
                return
            tempEnv = tempEnv.father
        print("Error: la variable " + id + " no existe")
        return

    def saveParameter(self, id: str, value, type: typeExpression, isArray: bool):
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
