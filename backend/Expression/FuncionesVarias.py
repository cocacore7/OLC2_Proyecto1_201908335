from Enum.OperacionVaria import operacionVaria
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
import math


class FuncionVaria(Expression):

    def __init__(self, leftExp: Expression, rigthExp: Expression, operation: operacionVaria) -> None:
        self.leftExp = leftExp
        self.rigthExp = rigthExp
        self.operation = operation

    def execute(self, environment: Environment) -> Symbol:

        leftValue = self.leftExp.execute(environment)
        rigthValue = self.rigthExp.execute(environment)

        if self.operation == operacionVaria.LOWER:
            if leftValue.getType() == typeExpression.STRING:
                return Symbol(
                    "",
                    leftValue.getValue().lower(),
                    typeExpression.STRING
                )
            else:
                print("No Se Puede Realizar LowerCase De " + str(leftValue.getValue()))

        elif self.operation == operacionVaria.UPPER:
            if leftValue.getType() == typeExpression.STRING:
                return Symbol(
                    "",
                    leftValue.getValue().upper(),
                    typeExpression.STRING
                )
            else:
                print("No Se Puede Realizar UpperCase De " + str(leftValue.getValue()))

        elif self.operation == operacionVaria.LOG10:
            if leftValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    math.log10(int(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            elif leftValue.getType() == typeExpression.FLOAT:
                return Symbol(
                    "",
                    math.log10(float(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            else:
                print("No Se Puede Realizar LOG10 De " + str(leftValue.getValue()))

        elif self.operation == operacionVaria.LOG:
            if leftValue.getType() == typeExpression.INTEGER:
                if rigthValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        math.log(int(rigthValue.getValue()),int(leftValue.getValue())),
                        typeExpression.FLOAT
                    )
                elif rigthValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        math.log(int(rigthValue.getValue()),float(leftValue.getValue())),
                        typeExpression.FLOAT
                    )
                else:
                    print("No Se Puede Realizar LOG De " + str(leftValue.getValue()) + " Con base " + str(rigthValue.getValue()))
            elif leftValue.getType() == typeExpression.FLOAT:
                if rigthValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        math.log(float(rigthValue.getValue()),int(leftValue.getValue())),
                        typeExpression.FLOAT
                    )
                elif rigthValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        math.log(float(rigthValue.getValue()),float(leftValue.getValue())),
                        typeExpression.FLOAT
                    )
                else:
                    print("No Se Puede Realizar LOG De " + str(leftValue.getValue()) + " Con base " + str(rigthValue.getValue()))
            else:
                print("No Se Puede Realizar LOG De " + str(leftValue.getValue()) + " Con base " + str(rigthValue.getValue()))

        elif self.operation == operacionVaria.SIN:
            if leftValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    math.sin(int(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            elif leftValue.getType() == typeExpression.FLOAT:
                return Symbol(
                    "",
                    math.sin(float(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            else:
                print("No Se Puede Realizar Seno De " + str(leftValue.getValue()))

        elif self.operation == operacionVaria.COS:
            if leftValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    math.cos(int(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            elif leftValue.getType() == typeExpression.FLOAT:
                return Symbol(
                    "",
                    math.cos(float(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            else:
                print("No Se Puede Realizar Coseno De " + str(leftValue.getValue()))

        elif self.operation == operacionVaria.TAN:
            if leftValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    math.tan(int(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            elif leftValue.getType() == typeExpression.FLOAT:
                return Symbol(
                    "",
                    math.tan(float(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            else:
                print("No Se Puede Realizar Tangente De " + str(leftValue.getValue()))

        elif self.operation == operacionVaria.SQRT:
            if leftValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    math.sqrt(int(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            elif leftValue.getType() == typeExpression.FLOAT:
                return Symbol(
                    "",
                    math.sqrt(float(leftValue.getValue())),
                    typeExpression.FLOAT
                )
            else:
                print("No Se Puede Realizar Raiz Cuadrada De " + str(leftValue.getValue()))

        return Symbol("", 'nothing', typeExpression.NULO)
