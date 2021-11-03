from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class NotEqual(Expression):

    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__()
        self.leftExpression = left
        self.rightExpression = right

    def compile(self, environment: Environment) -> Value:

        self.leftExpression.generator = self.generator
        self.rightExpression.generator = self.generator

        leftValue: Value = self.leftExpression.compile(environment)
        rightValue: Value = self.rightExpression.compile(environment)

        if leftValue.type == typeExpression.INTEGER or leftValue.type == typeExpression.FLOAT:
            if rightValue.type == typeExpression.INTEGER or rightValue.type == typeExpression.FLOAT:

                newValue = Value("", False, typeExpression.BOOL)

                if self.trueLabel == "":
                    self.trueLabel = self.generator.newLabel()

                if self.falseLabel == "":
                    self.falseLabel = self.generator.newLabel()

                self.generator.addIf(leftValue.value, rightValue.value, "!=", self.trueLabel)
                self.generator.addGoto(self.falseLabel)

                self.generator.addLabel(self.trueLabel)
                tmp = self.generator.newTemp()
                self.generator.addExpression(tmp, "1", "", "")
                newLabel = self.generator.newLabel()
                self.generator.addGoto(newLabel)
                self.generator.addLabel(self.falseLabel)
                self.generator.addExpression(tmp, "0", "", "")
                self.generator.addLabel(newLabel)

                newValue.value = tmp
                return newValue
            else:
                print("Error en desigualdad")
                return Value("0", False, typeExpression.INTEGER)
        else:
            print("Error en desigualdad")
            return Value("0", False, typeExpression.INTEGER)
