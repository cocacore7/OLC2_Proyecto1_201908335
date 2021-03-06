from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Expression.VariableCall import VariableCall
from Expression.ArrayCall import ArrayCall
from Globales.Tablas import Errores
from datetime import datetime


class AssignmentArray(Instruction):

    def __init__(self, id: str, llamada: VariableCall, indices, value: Expression, type: typeExpression, isArray: bool,
                 tipoD: str, entorno: str) -> None:
        self.id = id
        self.llamada = llamada
        self.indices = indices
        self.value = value
        self.type = type
        self.isArray = isArray
        self.tipoD = tipoD
        self.entorno = entorno

    def execute(self, environment: Environment):

        if not isinstance(self.value, list):
            tempValue = self.value.execute(environment)
            if self.type is not None:
                if self.type != typeExpression.NULO:
                    if self.type.value != tempValue.getType().value:
                        Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(tempValue.getType().value) + ", Se Esperaba Un " + obtener(self.type.value), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        return
                    tempArray = self.llamada.execute(environment)
                    if tempArray.isArray():
                        tempInd = self.indices.copy()
                        newArray = nuevoArreglo(tempArray, tempInd, tempValue, self.type, environment)
                        if type(self.value) == VariableCall:
                            environment.alterArray(self.value.id, newArray, "", "", self.value.id)
                        elif type(self.value) == ArrayCall:
                            environment.alterArray(obtenerID(self.value), newArray, "", "", obtenerID(self.value))
                        environment.alterArray(self.id, newArray, self.tipoD, self.entorno, "")
                    else:
                        Errores.append({'Descripcion': "La Variable No Es Un Arreglo", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        return
                else:
                    tempArray = self.llamada.execute(environment)
                    if tempArray.isArray():
                        tempInd = self.indices.copy()
                        newArray = nuevoArreglo(tempArray, tempInd, tempValue, self.type, environment)
                        if type(self.value) == VariableCall:
                            environment.alterArray(self.id, newArray, self.tipoD, self.entorno, self.value.id)
                        elif type(self.value) == ArrayCall:
                            environment.alterArray(obtenerID(self.value), newArray, "", "", obtenerID(self.value))
                        environment.alterArray(self.id, newArray, self.tipoD, self.entorno, "")
                    else:
                        Errores.append({'Descripcion': "La Variable No Es Un Arreglo", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        return
            else:
                Errores.append({'Descripcion': "Tipo De Dato Incorrecto, Se Esperaba: String, Int64, Float64, Bool o Char", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        else:
            tempExp = []
            for i in self.value:
                tempExp.append(i.execute(environment))
            if self.type != typeExpression.ANY:
                for i in tempExp:
                    if self.type == typeExpression.INTEGERA:
                        if i.getType() != typeExpression.INTEGER:
                            Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(i.getType().value) + ", Se Esperaba Un Int64", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                            return
                    elif self.type == typeExpression.FLOATA:
                        if i.getType() != typeExpression.FLOAT:
                            Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(i.getType().value) + ", Se Esperaba Un Float64", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                            return
                    elif self.type == typeExpression.STRINGA:
                        if i.getType() != typeExpression.STRING:
                            Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(i.getType().value) + ", Se Esperaba Un String", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                            return
                    elif self.type == typeExpression.BOOLA:
                        if i.getType() != typeExpression.BOOL:
                            Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(i.getType().value) + ", Se Esperaba Un Bool", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                            return
                    elif self.type == typeExpression.CHARA:
                        if i.getType() != typeExpression.CHAR:
                            Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(i.getType().value) + ", Se Esperaba Un Char", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                            return
                    else:
                        Errores.append({'Descripcion': "Declaracion Incorrecta: " + obtener(self.type.value) + ", No es Tipo Array", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        return
                tempArray = self.llamada.execute(environment)
                if tempArray.isArray():
                    tempInd = self.indices.copy()
                    newArray = nuevoArreglo2(tempArray, tempInd, tempExp, self.type, environment)
                    newArray.array = True
                    environment.alterArray(self.id, newArray, self.tipoD, self.entorno, "")
                else:
                    Errores.append({'Descripcion': "La Variable No Es Un Arreglo", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    return
            else:
                tempArray = self.llamada.execute(environment)
                if tempArray.isArray():
                    tempInd = self.indices.copy()
                    newArray = nuevoArreglo2(tempArray, tempInd, tempExp, self.type, environment)
                    newArray.array = True
                    environment.alterArray(self.id, newArray, self.tipoD, self.entorno, "")
                else:
                    Errores.append({'Descripcion': "La Variable No Es Un Arreglo", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    return


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


def nuevoArreglo(arr, indices, newValue, type, environment):
    if len(indices) != 0:
        tempindex = indices.pop(0).execute(environment)
        if tempindex.type == typeExpression.INTEGER:
            if len(arr.value) >= tempindex.value > 0:
                temp = arr.value[tempindex.value - 1]
                arr.value[tempindex.value - 1] = nuevoArreglo(temp, indices, newValue, type, environment)
                return arr
            else:
                Errores.append({'Descripcion': "Indice Solicitado Fuera De Rango", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return arr
        else:
            Errores.append({'Descripcion': "Indice No Es Tipo Int64", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return arr
    else:
        return newValue


def nuevoArreglo2(arr, indices, newValue, type, environment):
    if len(indices) != 0:
        tempindex = indices.pop(0).execute(environment)
        if tempindex.type == typeExpression.INTEGER:
            if len(arr.value) >= tempindex.value > 0:
                temp = arr.value[tempindex.value - 1]
                arr.value[tempindex.value - 1] = nuevoArreglo2(temp, indices, newValue, type, environment)
                return arr
            else:
                Errores.append({'Descripcion': "Indice Solicitado Fuera De Rango", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return arr
        else:
            Errores.append({'Descripcion': "Indice No Es Tipo Int64", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return arr
    else:
        tempSymbol: Symbol = Symbol('', newValue, type)
        tempSymbol.array = True
        return tempSymbol


def obtenerID(i):
    if type(i) == ArrayCall:
        a = obtenerID(i.array)
        return a
    else:
        return i.id
