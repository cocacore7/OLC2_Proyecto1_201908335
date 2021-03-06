from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class Array(Expression):

    def __init__(self, values, type) -> None:
        super().__init__()
        self.values = values
        self.type = type

    def compile(self, environment: Environment) -> Value:

        tmparray = []
        newTemp = self.generator.newTemp()
        self.generator.addExpression(newTemp, '-0.000001', '', '')
        newTemp2 = self.generator.newTemp()
        self.generator.addExpression(newTemp2, str(len(self.values)), '', '')
        tmparray.append(newTemp)
        tmparray.append(newTemp2)

        for exp in self.values:
            exp.generator = self.generator

            valExp = exp.compile(environment)
            if self.type == typeExpression.ANY:
                self.type = obtener(valExp.type)
            if obtenertipo(valExp.type):
                valtmp = self.generator.newTemp()
                self.generator.addExpression(valtmp, valExp.value, "", "")
                tmparray.append(valtmp)
            else:
                tmparray.append(valExp.array)

        newTemp3 = self.generator.newTemp()
        self.generator.addExpression(newTemp3, '-0.000002', '', '')
        tmparray.append(newTemp3)
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
