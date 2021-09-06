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

    def setValue(self, value: Expression):
        self.value = value

    def execute(self, environment: Environment):
        tempValue = self.value.execute(environment)
        if self.type is not None:
            if self.type.value != tempValue.getType().value:
                print("Los tipos no coinciden")
                environment.saveVariable(self.id,Primitive('nothing',typeExpression.NULO).execute(environment),typeExpression.NULO,False)
                #Error De Tipos No Coincidentes En Valor Y Parametro
                return
            environment.saveVariable(self.id, tempValue, self.type,False)
        else:
            environment.saveVariable(self.id, tempValue, tempValue.getType(),False)
