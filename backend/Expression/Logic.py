from Enum.LogicOperation import logicOperation
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression


class Logic(Expression):

    def __init__(self, leftExp: Expression, rightExp: Expression, operation: logicOperation) -> None:
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation

    def execute(self, environment: Environment) -> Symbol:

        leftValue = self.leftExp.execute(environment)
        rightValue = self.rightExp.execute(environment)

        if self.operation == logicOperation.AND:
            if leftValue.getType() == typeExpression.BOOL:
                if rightValue.getType() == typeExpression.BOOL:
                    return Symbol(
                    "",
                    leftValue.getValue() and rightValue.getValue(),
                    typeExpression.BOOL
                    )
                else:
                    print("No Se Permite Evaluar And De "+ rightValue.getType() + " y " +leftValue.getType())
            else:
                print("No Se Permite Evaluar And De "+ rightValue.getType() + " y " +leftValue.getType())

        elif self.operation == logicOperation.OR:
            if leftValue.getType() == typeExpression.BOOL:
                if rightValue.getType() == typeExpression.BOOL:
                    return Symbol(
                    "",
                    leftValue.getValue() or rightValue.getValue(),
                    typeExpression.BOOL
                    )
                else:
                    print("No Se Permite Evaluar Or De "+ rightValue.getType() + " y " +leftValue.getType())
            else:
                print("No Se Permite Evaluar Or De "+ rightValue.getType() + " y " +leftValue.getType())

        elif self.operation == logicOperation.NOT:
            if leftValue.getType() == typeExpression.BOOL:
                return Symbol(
                "",
                not leftValue.getValue(),
                typeExpression.BOOL
                )
            else:
                print("No Se Permite Evaluar Not De " + leftValue.getType())
