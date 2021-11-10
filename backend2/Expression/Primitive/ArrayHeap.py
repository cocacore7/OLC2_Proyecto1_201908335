from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class ArrayHeap(Expression):

    def __init__(self, arr, type) -> None:
        super().__init__()
        self.arr = arr
        self.type = type

    def compile(self, environment: Environment) -> Value:
        tmparray = []
        newTemp = ""
        for i in self.arr:
            if isinstance(i, list):
                crear = ArrayHeap(i, self.type)
                crear.generator = self.generator
                nuevo = crear.compile(environment)
                tmparray.append(nuevo.array)
            else:
                newTemp = self.generator.newTemp()
                self.generator.addExpression(newTemp, "H", '', '')
                self.generator.addSetHeap('H', i)
                self.generator.addExpression('H', 'H', '1', '+')
                tmparray.append(newTemp)

        retorno = Value(newTemp, True, self.type)
        retorno.array = tmparray
        return retorno


def obtener(type):
    if type == typeExpression.INTEGER:
        return typeExpression.INTEGERA
    elif type == typeExpression.FLOAT:
        return typeExpression.FLOATA
    elif type == typeExpression.CHAR:
        return typeExpression.CHARA
    elif type == typeExpression.STRING:
        return typeExpression.STRINGA
    elif type == typeExpression.BOOL:
        return typeExpression.BOOLA
    return typeExpression.ANY


def obtenertipo(type):
    if type == typeExpression.INTEGER:
        return True
    elif type == typeExpression.FLOAT:
        return True
    elif type == typeExpression.CHAR:
        return True
    elif type == typeExpression.STRING:
        return True
    elif type == typeExpression.BOOL:
        return True
    return False
