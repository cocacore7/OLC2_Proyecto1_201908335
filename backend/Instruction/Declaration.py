from Expression.Primitive import Primitive
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression


class Declaration(Instruction):

    def __init__(self, id: str, value: Expression, type: typeExpression, isArray: bool, tipoD: str, entorno: str) -> None:
        self.id = id
        self.value = value
        self.type = type
        self.isArray = isArray
        self.tipoD = tipoD
        self.entorno = entorno

    def execute(self, environment: Environment):

        if self.value is not None:
            tempValue = self.value.execute(environment)
            if self.type is not None:
                if self.type != typeExpression.NULO:
                    if self.type.value != tempValue.getType().value:
                        print("Los tipos no coinciden, Se obtuvo un " + obtener(
                            tempValue.getType().value) + ", Se Esperaba Un " + obtener(self.type.value))
                        environment.saveVariable(self.id, Primitive('nothing', typeExpression.NULO).execute(environment), typeExpression.NULO, False, self.tipoD, self.entorno)
                        return
                    environment.saveVariable(self.id, tempValue, self.type, self.isArray, self.tipoD, self.entorno)
                else:
                    environment.saveVariable(self.id, tempValue, tempValue.getType(), self.isArray, self.tipoD, self.entorno)
            else:
                print("Tipo De Dato Incorrecto, Se Esperaba: String, Int64, Float64, Bool o Char")
                environment.saveVariable(self.id, Primitive('nothing', typeExpression.NULO).execute(environment),
                                         typeExpression.NULO, False, self.tipoD, self.entorno)
        else:

            environment.saveVariable(self.id, Primitive('nothing', typeExpression.NULO).execute(environment),
                                     typeExpression.NULO, False, self.tipoD, self.entorno)


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
        return "Error"
