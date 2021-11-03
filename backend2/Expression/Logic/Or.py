from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class Or(Expression):

    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__()
        self.leftExpression = left
        self.rightExpression = right

    def compile(self, environment: Environment) -> Value:

        self.leftExpression.generator = self.generator
        self.rightExpression.generator = self.generator

        leftValue: Value = self.leftExpression.compile(environment)
        rightValue: Value = self.rightExpression.compile(environment)

        if leftValue.type == typeExpression.BOOL:
            if rightValue.type == typeExpression.BOOL:

                newValue = Value("", False, typeExpression.BOOL)

                newLabelTrue = self.generator.newLabel()
                newLabelFalse = self.generator.newLabel()

                self.generator.addIf(leftValue.value, "1", "==", newLabelTrue)
                self.generator.addIf(rightValue.value, "1", "==", newLabelTrue)
                self.generator.addGoto(newLabelFalse)

                self.generator.addLabel(newLabelFalse)
                tmp = self.generator.newTemp()
                self.generator.addExpression(tmp, "0", "", "")
                newLabel = self.generator.newLabel()
                self.generator.addGoto(newLabel)
                self.generator.addLabel(newLabelTrue)
                self.generator.addExpression(tmp, "1", "", "")
                self.generator.addLabel(newLabel)

                newValue.value = tmp
                return newValue
            else:
                print("Error en or")
                return Value("0", False, typeExpression.INTEGER)
        else:
            print("Error en or")
            return Value("0", False, typeExpression.INTEGER)
