from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Globales.Tablas import Errores
from datetime import datetime


class ArrayCall(Expression):

    def __init__(self, array: Expression, index: Expression) -> None:
        self.array = array
        self.index = index

    def execute(self, environment: Environment) -> Symbol:

        tempArray = self.array.execute(environment)

        if tempArray.isArray():
            tempIndex = self.index.execute(environment)
            if type(tempIndex.value) is Symbol:
                tempIndex.value = tempIndex.value.getValue()
            if tempIndex.type == typeExpression.INTEGER:
                tempValue = tempArray.getValue()
                if len(tempValue) >= int(tempIndex.getValue()) > 0:
                    return tempValue[int(tempIndex.getValue())-1]
                else:
                    Errores.append({'Descripcion': "Indice De Arreglo Fuera De Rango", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    print()
                    return Symbol('', 'nothing', typeExpression.NULO)
            else:
                Errores.append({'Descripcion': "Indice De Arreglo No Es Int64o", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return Symbol('', 'nothing', typeExpression.NULO)
        else:
            Errores.append({'Descripcion': "Error: No es posible acceder a un " + str(tempArray.getType()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return Symbol('', 'nothing', typeExpression.NULO)
