from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression


class ArrayCall(Expression):

    def __init__(self, array: Expression, index: Expression) -> None:
        self.array = array
        self.index = index

    def execute(self, environment: Environment) -> Symbol:

        tempArray = self.array.execute(environment)

        if tempArray.isArray():
            tempIndex = self.index.execute(environment)
            tempValue = tempArray.getValue()
            if len(tempValue) > int(tempIndex.getValue())-1 > -1:
                return tempValue[int(tempIndex.getValue())-1]
            else:
                print("Indice De Arreglo Fuera De Rango")
                return Symbol('', 'nothing', typeExpression.NULO)
        else:
            print("Error: No es posible acceder a un " + str(tempArray.getType()))
            return Symbol('', 'nothing', typeExpression.NULO)
