from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class Array(Expression):

    def __init__(self, values, type) -> None:
        self.values = values
        self.type = type

    def compile(self, environment: Environment) -> Value:
        newTemp = self.generator.newTemp()

        self.generator.addExpression(newTemp, 'H', '', '')
        self.generator.addSetHeap('H', "-0.000001")
        self.generator.addExpression('H', 'H', '1', '+')
        self.generator.addSetHeap('H', str(len(self.values)))
        self.generator.addExpression('H', 'H', '1', '+')

        for exp in self.values:
            exp.generator = self.generator

            valExp = exp.compile(environment)
            if self.type == typeExpression.ANY:
                self.type = obtener(valExp.type)

            self.generator.addSetHeap('H', valExp.getValue())
            self.generator.addExpression('H', 'H', '1', '+')

        return Value(newTemp, True, self.type)


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
