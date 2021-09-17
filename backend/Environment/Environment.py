from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Globales.Tablas import Errores, Simbolos
from datetime import datetime


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

    def saveVariable(self, id: str, value, type: typeExpression, isArray: bool, entorno: str, tipoD: str, ref: str):
        if self.father is not None:
            if tipoD == "F":
                if entorno == "G":
                    globalenv = self.getGlobal()
                    if globalenv.variable.get(id) is not None:
                        tempVar: Symbol = globalenv.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        globalenv.variable[id] = tempVar
                        self.globalAccess[id] = id
                        if self.variable.get(id) is not None:
                            del self.variable[id]
                        return
                    tempVar = Symbol(id, value, type)
                    tempVar.array = isArray
                    if tempVar.ref == "":
                        tempVar.ref = ref
                    globalenv.variable[id] = tempVar
                    self.globalAccess[id] = id
                    if self.variable.get(id) is not None:
                        del self.variable[id]
                    Simbolos.append({'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Global", 'Linea': "", 'Columna': ""})
                    return
                elif entorno == "L":
                    if self.globalAccess.get(id) is None:
                        if self.variable.get(id) is not None:
                            tempVar: Symbol = self.variable.get(id)
                            tempVar.value = value
                            tempVar.type = value.getType()
                            tempVar.array = value.isArray()
                            if tempVar.ref == "":
                                tempVar.ref = ref
                            self.variable[id] = tempVar
                            return
                        elif self.father.variable.get(id) is not None:
                            tempVar: Symbol = self.father.variable.get(id)
                            tempVar.value = value
                            tempVar.type = value.getType()
                            tempVar.array = value.isArray()
                            if tempVar.ref == "":
                                tempVar.ref = ref
                            self.father.variable[id] = tempVar
                            return
                        tempVar = Symbol(id, value, type)
                        tempVar.array = isArray
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.variable[id] = tempVar
                        if ComprobarParam(id):
                            Simbolos.append({'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Local", 'Linea': "", 'Columna': ""})
                        return
                    else:
                        globalenv = self.getGlobal()
                        tempVar: Symbol = globalenv.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        if tempVar.ref == "":
                            tempVar.ref = ref
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
                                if tempVar.ref == "":
                                    tempVar.ref = ref
                                tempEnv.variable[id] = tempVar
                                return
                            tempEnv = tempEnv.father
                        globalenv = self.getGlobal()
                        tempVar = Symbol(id, value, type)
                        tempVar.array = isArray
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        globalenv.variable[id] = tempVar
                        Simbolos.append({'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Global", 'Linea': "", 'Columna': ""})
                        return
                    else:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.variable[id] = tempVar
                        return
                elif entorno == "L":
                    if self.variable.get(id) is not None:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.variable[id] = tempVar
                        self.localAccess[id] = id
                        return
                    tempVar = Symbol(id, value, type)
                    tempVar.array = isArray
                    if tempVar.ref == "":
                        tempVar.ref = ref
                    self.variable[id] = tempVar
                    self.localAccess[id] = id
                    if ComprobarParam(id):
                        Simbolos.append({'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Local", 'Linea': "", 'Columna': ""})
                    return
        else:
            if self.variable.get(id) is not None:
                tempVar: Symbol = self.variable.get(id)
                tempVar.value = value
                tempVar.type = value.getType()
                tempVar.array = value.isArray()
                if tempVar.ref == "":
                    tempVar.ref = ref
                self.variable[id] = tempVar
                return
            tempVar = Symbol(id, value, type)
            tempVar.array = isArray
            if tempVar.ref == "":
                tempVar.ref = ref
            self.variable[id] = tempVar
            Simbolos.append({'Nombre': id, 'Tipo': obtener(type.value), 'Ambito': "Global", 'Linea': "", 'Columna': ""})

    def alterArray(self, id: str, value, entorno: str, tipoD: str, ref: str):
        if self.father is not None:
            if tipoD == "F":
                if entorno == "G":
                    globalenv = self.getGlobal()
                    if globalenv.variable.get(id) is not None:
                        tempVar: Symbol = globalenv.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        globalenv.variable[id] = tempVar
                        self.globalAccess[id] = id
                        if self.variable.get(id) is not None:
                            del self.variable[id]
                    else:
                        Errores.append({'Descripcion': "Arreglo: " + id + ", No Existe", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                elif entorno == "L":
                    if self.globalAccess.get(id) is None:
                        if self.variable.get(id) is not None:
                            tempVar: Symbol = self.variable.get(id)
                            tempVar.value = value
                            tempVar.type = value.getType()
                            tempVar.array = value.isArray()
                            if tempVar.ref == "":
                                tempVar.ref = ref
                            self.variable[id] = tempVar
                        elif self.father.variable.get(id) is not None:
                            tempVar: Symbol = self.father.variable.get(id)
                            tempVar.value = value
                            tempVar.type = value.getType()
                            tempVar.array = value.isArray()
                            if tempVar.ref == "":
                                tempVar.ref = ref
                            self.father.variable[id] = tempVar
                        else:
                            Errores.append({'Descripcion': "Arreglo: " + id + ", No Existe", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    else:
                        globalenv = self.getGlobal()
                        tempVar: Symbol = globalenv.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        if tempVar.ref == "":
                            tempVar.ref = ref
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
                                if tempVar.ref == "":
                                    tempVar.ref = ref
                                tempEnv.variable[id] = tempVar
                                return
                            tempEnv = tempEnv.father
                        Errores.append({'Descripcion': "Arreglo: " + id + ", No Existe", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    else:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.variable[id] = tempVar
                elif entorno == "L":
                    if self.variable.get(id) is not None:
                        tempVar: Symbol = self.variable.get(id)
                        tempVar.value = value
                        tempVar.type = value.getType()
                        tempVar.array = value.isArray()
                        if tempVar.ref == "":
                            tempVar.ref = ref
                        self.variable[id] = tempVar
                        self.localAccess[id] = id
                    else:
                        Errores.append({'Descripcion': "Arreglo: " + id + ", No Existe", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        else:
            if self.variable.get(id) is not None:
                tempVar: Symbol = self.variable.get(id)
                tempVar.value = value
                tempVar.type = value.getType()
                tempVar.array = value.isArray()
                if tempVar.ref == "":
                    tempVar.ref = ref
                self.variable[id] = tempVar
            else:
                Errores.append({'Descripcion': "Arreglo: " + id + ", No Existe", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return

    def PopPushArray(self, id: str, value, ref: str):
        tempEnv = self
        while tempEnv is not None:
            if tempEnv.variable.get(id) is not None:
                tempVar: Symbol = tempEnv.variable.get(id)
                tempVar.value = value
                tempVar.type = value.getType()
                tempVar.array = value.isArray()
                if tempVar.ref == "":
                    tempVar.ref = ref
                tempEnv.variable[id] = tempVar
                return
            tempEnv = tempEnv.father
        Errores.append({'Descripcion': "Arreglo: " + id + ", No Existe", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return

    def saveParameter(self, id: str, value, type: typeExpression, isArray: bool, ref: str):
        tempVar = Symbol(id, value, type)
        tempVar.array = isArray
        if tempVar.ref == "":
            tempVar.ref = ref
        if ComprobarParam(id):
            Simbolos.append({'Nombre': id, 'Tipo': "Parametro", 'Ambito': "Local", 'Linea': "", 'Columna': ""})
        self.variable[id] = tempVar

    def getVariable(self, id: str) -> Symbol:
        tempEnv = self
        while tempEnv is not None:
            if tempEnv.variable.get(id) is not None:
                return tempEnv.variable.get(id).getValue()
            tempEnv = tempEnv.father
        Errores.append({'Descripcion': "Arreglo: " + id + ", No Existe", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return None

    def saveFunction(self, id: str, function):
        if self.function.get(id) is not None:
            Errores.append({'Descripcion': "La función " + id + " ya existe", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return
        Simbolos.append({'Nombre': id, 'Tipo': "Funcion", 'Ambito': "Global", 'Linea': "", 'Columna': ""})
        self.function[id] = function

    def getFunction(self, id: str):
        tempEnv = self
        while tempEnv is not None:
            if tempEnv.function.get(id) is not None:
                return tempEnv.function.get(id)
            tempEnv = tempEnv.father
            
        Errores.append({'Descripcion': "Error: la función " + id + " no existe", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
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
