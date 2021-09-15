from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Expression.VariableCall import VariableCall


class Pop(Instruction):

    def __init__(self, id: str, llamada: VariableCall, indices) -> None:
        self.id = id
        self.llamada = llamada
        self.indices = indices

    def execute(self, environment: Environment):

        tempArray = self.llamada.execute(environment)
        if tempArray.isArray():
            newArray = nuevoArreglo(tempArray, self.indices, environment)
            environment.PopPushArray(self.id, newArray)
            return newArray
        else:
            print("La Variable No Es Un Arreglo")

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
                    print("Indice Solicitado Fuera De Rango")
                    return arr
            else:
                print("No Se Puede Acceder, No Es Arreglo")
                return arr
        else:
            print("Indice No Es Tipo Int64")
            return arr
    else:
        if arr.isArray():
            if len(arr.value) > 0:
                arr.value.pop()
            else:
                print("El Arreglo No Tiene Valores")
        else:
            print("El Objeto De Arreglo En Indice Solicitado No Es Un Arreglo, No Se Puede Usar Pop")
        return arr
