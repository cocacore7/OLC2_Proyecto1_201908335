from Enum.relationalOperation import relationalOperation
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression


class Relational(Expression):

    def __init__(self, leftExp: Expression, rightExp: Expression, operation: relationalOperation) -> None:
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation

    def execute(self, environment: Environment) -> Symbol:

        leftValue = self.leftExp.execute(environment)
        rightValue = self.rightExp.execute(environment)

        if self.operation == relationalOperation.MAYOR:
            if leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.STRING:
                    return Symbol(
                        "",
                        leftValue.getValue() > rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Mayor Con " + rightValue.getType() + " y " + leftValue.getType())
            elif leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) > float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) > int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Mayor Con " + rightValue.getType() + " y " + leftValue.getType())
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) > float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) > float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Mayor Con " + rightValue.getType() + " y " + leftValue.getType())
            else:
                print("No Se Permite Evaluar Operacion Mayor Con " + rightValue.getType() + " y " + leftValue.getType())

        elif self.operation == relationalOperation.MENOR:
            if leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.STRING:
                    return Symbol(
                        "",
                        leftValue.getValue() < rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Menor Con " + rightValue.getType() + " y " + leftValue.getType())
            elif leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) < float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) < int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Menor Con " + rightValue.getType() + " y " + leftValue.getType())
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) < float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) < float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Menor Con " + rightValue.getType() + " y " + leftValue.getType())
            else:
                print("No Se Permite Evaluar Operacion Menor Con " + rightValue.getType() + " y " + leftValue.getType())

        elif self.operation == relationalOperation.IGUAL:
            return Symbol(
                "",
                leftValue.getValue() == rightValue.getValue(),
                typeExpression.BOOL
            )

        elif self.operation == relationalOperation.MAYORIGUAL:
            if leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.STRING:
                    return Symbol(
                        "",
                        leftValue.getValue() >= rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Mayor Igual Con " + rightValue.getType() + " y " + leftValue.getType())
            elif leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) >= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) >= int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Mayor Igual Con " + rightValue.getType() + " y " + leftValue.getType())
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) >= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) >= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Mayor Igual Con " + rightValue.getType() + " y " + leftValue.getType())
            else:
                print(
                    "No Se Permite Evaluar Operacion Mayor Con Igual " + rightValue.getType() + " y " + leftValue.getType())

        elif self.operation == relationalOperation.MENORIGUAL:
            if leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.STRING:
                    return Symbol(
                        "",
                        leftValue.getValue() <= rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Menor Igual Con " + rightValue.getType() + " y " + leftValue.getType())
            elif leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) <= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) <= int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Menor Igual Con " + rightValue.getType() + " y " + leftValue.getType())
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) <= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) <= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    print(
                        "No Se Permite Evaluar Operacion Menor Igual Con " + rightValue.getType() + " y " + leftValue.getType())
            else:
                print(
                    "No Se Permite Evaluar Operacion Menor Igual Con " + rightValue.getType() + " y " + leftValue.getType())

        elif self.operation == relationalOperation.DISTINTO:
            return Symbol(
                "",
                leftValue.getValue() != rightValue.getValue(),
                typeExpression.BOOL
            )
