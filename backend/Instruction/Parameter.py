from math import fabs
from Expression.Primitive import Primitive
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Abstract.Instruction import Instruction


class Parameter(Instruction):

    def __init__(self, id: str, type: typeExpression) -> None:
        self.id = id
        self.type = type
        self.value = None
        self.array = False

    def setValue(self, value: Expression):
        self.value = value

    def execute(self, environment: Environment):
        tempValue = self.value.execute(environment)
        if self.type is not None:
            if self.type.value != tempValue.getType().value:
                print("Los tipos no coinciden")
                environment.saveParameter(self.id, Primitive('nothing', typeExpression.NULO).execute(environment),
                                          typeExpression.NULO, False)
                return
            environment.saveParameter(self.id, tempValue, tempValue.type, tempValue.array)
        else:
            environment.saveParameter(self.id, tempValue, tempValue.type, tempValue.array)

    def getId(self):
        return self.id

    def getValue(self):
        return self.value

    def getType(self):
        return self.type

    def isArray(self):
        return self.array
