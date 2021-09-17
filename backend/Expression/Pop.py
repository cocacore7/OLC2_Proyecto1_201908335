from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Expression.VariableCall import VariableCall
from Globales.Tablas import Errores
from datetime import datetime


class Pop(Instruction):

    def __init__(self, id: str, llamada: VariableCall, indices) -> None:
        self.id = id
        self.llamada = llamada
        self.indices = indices

    def execute(self, environment: Environment):

        tempArray = self.llamada.execute(environment)
        if tempArray.isArray():
            tempInd = self.indices.copy()
            newArray = nuevoArreglo(tempArray, tempInd, environment)
            environment.PopPushArray(self.id, newArray, "")
            environment.getGlobal().PopPushArray(self.id, newArray, "")

            return newArray
        else:
            Errores.append({'Descripcion': "La Variable No Es Un Arreglo", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        return Symbol("", 'nothing', typeExpression.NULO)


def nuevoArreglo(arr, indices, environment):
    if len(indices) != 0:
        tempindex = indices.pop(0).execute(environment)
        if tempindex.type == typeExpression.INTEGER:
            if arr.isArray():
                if len(arr.value) >= tempindex.value > 0:
                        temp = arr.value[tempindex.value - 1]
                        arr.value[tempindex.value - 1] = nuevoArreglo(temp, indices, environment)
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
            if len(arr.value) > 0:
                arr.value.pop()
            else:
                Errores.append({'Descripcion': "El Arreglo No Tiene Valores", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        else:
            Errores.append({'Descripcion': "El Objeto De Arreglo En Indice Solicitado No Es Un Arreglo, No Se Puede Usar Pop", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return arr
