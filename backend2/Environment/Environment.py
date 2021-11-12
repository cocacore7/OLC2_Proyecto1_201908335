from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Value import Value
from Globales.Tablas import Errores, Simbolos
from datetime import datetime


class Environment:

    def __init__(self, father) -> None:
        self.father = father
        self.variable = {}
        self.size = 0
        self.localSize = 0
        self.function = {}
        self.globalAccess = {}
        self.localAccess = {}

        if father is not None:
            self.size = father.size

    def getGlobal(self):
        tempEnv: Environment = self
        while tempEnv.father is not None:
            tempEnv = tempEnv.father
        return tempEnv

    def saveVariable(self, id: str, type: typeExpression, isArray: bool, entorno: str, tipoD: str, ref: str):
        if self.father is not None:
            if tipoD == "F":
                if entorno == "G":
                    globalenv = self.getGlobal()
                    if globalenv.variable.get(id) is not None:
                        tempVar: Symbol = self.getGlobal().variable.get(id)
                        tempVar.type = type
                        tempVar.array = isArray
                        if tempVar.ref == "":
                            tempVar.ref = ref

                        tempVar = Symbol(id, type, self.size)
                        self.size = self.size + 1
                        globalenv.variable[id] = tempVar
                        self.globalAccess[id] = id
                        if self.variable.get(id) is not None:
                            del self.variable[id]
                        return tempVar
                    tempVar = Symbol(id, type, self.size)
                    self.size = self.size + 1
                    tempVar.array = isArray
                    if tempVar.ref == "":
                        tempVar.ref = ref
                    globalenv.variable[id] = tempVar
                    self.globalAccess[id] = id
                    if self.variable.get(id) is not None:
                        del self.variable[id]
                    Simbolos.append(
                        {'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Global", 'Linea': "0", 'Columna': "0"})
                    return tempVar
                elif entorno == "L":
                    if self.globalAccess.get(id) is None:
                        if self.variable.get(id) is not None:
                            tempVar: Symbol = self.variable.get(id)
                            tempVar.type = type
                            tempVar.array = isArray
                            if tempVar.ref == "":
                                tempVar.ref = ref
                            self.variable[id] = tempVar
                            return tempVar
                        elif self.father.variable.get(id) is not None:
                            tempVar: Symbol = self.father.variable.get(id)
                            tempVar.type = type
                            tempVar.array = isArray
                            if tempVar.ref == "":
                                tempVar.ref = ref
                            self.father.variable[id] = tempVar
                            return tempVar
                        tempVar = Symbol(id, type, self.size)
                        self.size = self.size + 1
                        tempVar.array = isArray
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.variable[id] = tempVar
                        if ComprobarParam(id):
                            Simbolos.append({'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Local", 'Linea': "0",
                                             'Columna': "0"})
                        return tempVar
                    else:
                        tempVar: Symbol = self.getGlobal().variable.get(id)
                        tempVar.type = type
                        tempVar.array = isArray
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.getGlobal().variable[id] = tempVar
                        return tempVar
            elif tipoD == "C":
                if entorno == "G":
                    if self.localAccess.get(id) is None:
                        tempEnv = self.father
                        while tempEnv is not None:
                            if tempEnv.variable.get(id) is not None:
                                tempVar: Symbol = tempEnv.variable.get(id)
                                tempVar.type = type
                                tempVar.array = isArray
                                if tempVar.ref == "":
                                    tempVar.ref = ref
                                tempEnv.variable[id] = tempVar
                                return tempVar
                            tempEnv = tempEnv.father
                        tempVar = Symbol(id, type, self.size)
                        self.size = self.size + 1
                        tempVar.array = isArray
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.getGlobal().variable[id] = tempVar
                        Simbolos.append(
                            {'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Global", 'Linea': "0", 'Columna': "0"})
                        return tempVar
                    else:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.type = type
                        tempVar.array = isArray
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.variable[id] = tempVar
                        return tempVar
                elif entorno == "L":
                    if self.variable.get(id) is not None:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.type = type
                        tempVar.array = isArray
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.variable[id] = tempVar
                        self.localAccess[id] = id
                        return tempVar
                    tempVar = Symbol(id, type, self.size)
                    self.size = self.size + 1
                    self.localSize = self.localSize + 1
                    tempVar.array = isArray
                    if tempVar.ref == "":
                        tempVar.ref = ref
                    self.variable[id] = tempVar
                    self.localAccess[id] = id
                    if ComprobarParam(id):
                        Simbolos.append(
                            {'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Local", 'Linea': "0", 'Columna': "0"})
                    return tempVar
        else:
            if self.variable.get(id) is not None:
                tempVar: Symbol = self.variable.get(id)
                tempVar.type = type
                tempVar.array = isArray
                if tempVar.ref == "":
                    tempVar.ref = ref
                self.variable[id] = tempVar
                return tempVar
            tempVar = Symbol(id, type, self.size)
            self.size = self.size + 1
            tempVar.array = isArray
            if tempVar.ref == "":
                tempVar.ref = ref
            self.variable[id] = tempVar
            Simbolos.append({'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Global", 'Linea': "0", 'Columna': "0"})
            return tempVar

    def saveParameter(self, id: str, type: typeExpression, isArray: bool, ref: str):
        tempVar = Symbol(id, type, self.size)
        self.size = self.size + 1
        self.localSize = self.localSize + 1
        tempVar.array = isArray
        if tempVar.ref == "":
            tempVar.ref = ref
        if ComprobarParam(id):
            Simbolos.append({'Nombre': id, 'Tipo': "Parametro", 'Ambito': "Local", 'Linea': "0", 'Columna': "0"})
        self.variable[id] = tempVar
        return tempVar

    def saveFunction(self, id: str, value, type: typeExpression):
        tempVar = Value(value, True, type)
        if ComprobarParam(id):
            Simbolos.append({'Nombre': id, 'Tipo': "Funcion", 'Ambito': "Global", 'Linea': "0", 'Columna': "0"})
        self.getGlobal().function[id] = tempVar
        return tempVar

    def getVariable(self, id: str) -> Symbol:
        tempEnv = self
        while tempEnv is not None:
            if tempEnv.variable.get(id) is not None:
                return tempEnv.variable.get(id)
            tempEnv = tempEnv.father
        Errores.append({'Descripcion': "Error: la variable " + id + " no existe", 'Linea': "0", 'Columna': "0",
                        'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return None

    def getFunction(self, id: str) -> Symbol:
        if self.getGlobal().function.get(id) is not None:
            return self.getGlobal().function.get(id)
        Errores.append({'Descripcion': "Error: la Funcion " + id + " no existe", 'Linea': "0", 'Columna': "0",
                        'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return None


def ComprobarParam(id):
    for i in Simbolos:
        if i["Nombre"] == id:
            return False
    return True


def obtener(numero):
    if numero == 0:
        return "String"
    elif numero == 1:
        return "Int64"
    elif numero == 2:
        return "Float64"
    elif numero == 3:
        return "Bool"
    elif numero == 4:
        return "Char"
    elif numero == 5:
        return "Nothing"
    elif numero == 6:
        return "Array{String}"
    elif numero == 7:
        return "Array{Int64}"
    elif numero == 8:
        return "Array{Float64}"
    elif numero == 9:
        return "Array{Bool}"
    elif numero == 10:
        return "Array{Char}"
    elif numero == 11:
        return "Array{Any}"
