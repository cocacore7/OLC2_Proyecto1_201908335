from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Expression.VariableCall import VariableCall
from Expression.ArrayCall import ArrayCall
from Globales.Tablas import Errores
from datetime import datetime


class Push(Instruction):

    def __init__(self, id: str, llamada: VariableCall, indices, value: Expression) -> None:
        self.id = id
        self.llamada = llamada
        self.indices = indices
        self.value = value

    def execute(self, environment: Environment):

        if not isinstance(self.value, list):
            tempValue = self.value.execute(environment)
            tempArray = self.llamada.execute(environment)
            if tempArray.isArray():
                tempInd = self.indices.copy()
                newArray = nuevoArreglo(tempArray, tempInd, tempValue, self.type, environment)
                if type(self.value) == VariableCall:
                    environment.PopPushArray(self.value.id, newArray, self.value.id)
                elif type(self.value) == ArrayCall:
                    environment.PopPushArray(obtenerID(self.value), newArray, obtenerID(self.value))
                environment.PopPushArray(self.id, newArray, "")
                return newArray
            else:
                Errores.append({'Descripcion': "La Variable No Es Un Arreglo", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        else:
            tempExp = []
            for i in self.value:
                tempExp.append(i.execute(environment))
            tempArray = self.llamada.execute(environment)
            if tempArray.isArray():
                tempInd = self.indices.copy()
                newArray = nuevoArreglo2(tempArray, tempInd, tempExp, typeExpression.ANY, environment)
                newArray.array = True
                if type(self.value) == VariableCall:
                    environment.PopPushArray(self.value.id, newArray, self.value.id)
                elif type(self.value) == ArrayCall:
                    environment.PopPushArray(obtenerID(self.value), newArray, obtenerID(self.value))
                environment.PopPushArray(self.id, newArray, "")
                return newArray
            else:
                Errores.append({'Descripcion': "La Variable No Es Un Arreglo", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        return Symbol("", 'nothing', typeExpression.NULO)


def nuevoArreglo(arr, indices, newValue, type, environment):
    if len(indices) != 0:
        tempindex = indices.pop(0).execute(environment)
        if tempindex.type == typeExpression.INTEGER:
            if arr.isArray():
                if len(arr.value) >= tempindex.value > 0:
                    temp = arr.value[tempindex.value - 1]
                    arr.value[tempindex.value - 1] = nuevoArreglo(temp, indices, newValue, type, environment)
                    return arr
                else:
                    Errores.append({'Descripcion': "Indice Solicitado Fuera De Rango", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    return arr
            else:
                Errores.append({'Descripcion': "No Se Puede Acceder, No Es Arreglo", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return arr
        else:
            Errores.append({'Descripcion': "Indice No Es Tipo Int64", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return arr
    else:
        arr.value.append(newValue)
        return arr


def nuevoArreglo2(arr, indices, newValue, type, environment):
    if len(indices) != 0:
        tempindex = indices.pop(0).execute(environment)
        if tempindex.type == typeExpression.INTEGER:
            if arr.isArray():
                if len(arr.value) >= tempindex.value > 0:
                    temp = arr.value[tempindex.value - 1]
                    arr.value[tempindex.value - 1] = nuevoArreglo2(temp, indices, newValue, type, environment)
                    return arr
                else:
                    Errores.append({'Descripcion': "Indice Solicitado Fuera De Rango", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    return arr
            else:
                Errores.append({'Descripcion': "No Se Puede Acceder, No Es Arreglo", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return arr
        else:
            Errores.append({'Descripcion': "Indice No Es Tipo Int64", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return arr
    else:
        if arr.isArray():
            tempSymbol: Symbol = Symbol('', newValue, type)
            tempSymbol.array = True
            arr.value.append(tempSymbol)
        else:
            Errores.append({'Descripcion': "El Objeto De Arreglo En Indice Solicitado No Es Un Arreglo, No Se Puede Usar Push", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return arr


def obtenerID(i):
    if type(i) == ArrayCall:
        a = obtenerID(i.array)
        return a
    else:
        return i.id
