from Enum.LogicOperation import logicOperation
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Instruction.Parameter import Parameter


class Logic(Expression):

    def __init__(self, leftExp: Expression, rightExp: Expression, operation: logicOperation) -> None:
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation

    def execute(self, environment: Environment) -> Symbol:

        leftValue = self.leftExp.execute(environment)
        if type(leftValue) is Parameter:
            if type(leftValue.value) is Symbol:
                leftValue = leftValue.value
        rightValue = self.rightExp.execute(environment)
        if type(rightValue) is Parameter:
            if type(rightValue.value) is Symbol:
                rightValue.value = rightValue.value.getValue()

        if self.operation == logicOperation.AND:
            if leftValue.getType() == typeExpression.BOOL:
                if rightValue.getType() == typeExpression.BOOL:
                    return Symbol(
                        "",
                        leftValue.getValue() and rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    print("No Se Permite Evaluar And De " + str(rightValue.getValue()) + " y " + str(
                        leftValue.getValue()))
            else:
                print("No Se Permite Evaluar And De " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()))

        elif self.operation == logicOperation.OR:
            if leftValue.getType() == typeExpression.BOOL:
                if rightValue.getType() == typeExpression.BOOL:
                    return Symbol(
                        "",
                        leftValue.getValue() or rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Or De " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()))
            else:
                print("No Se Permite Evaluar Or De " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()))

        elif self.operation == logicOperation.NOT:
            if leftValue.getType() == typeExpression.BOOL:
                return Symbol(
                    "",
                    not leftValue.getValue(),
                    typeExpression.BOOL
                )
            else:
                print("No Se Permite Evaluar Not De " + str(leftValue.getValue()))

        return Symbol("", 'nothing', typeExpression.NULO)
