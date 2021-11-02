from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class Not(Expression):

    def __init__(self, left: Expression) -> None:
        super().__init__()
        self.leftExpression = left

    def compile(self, environment: Environment) -> Value:

        self.leftExpression.generator = self.generator

        leftValue: Value = self.leftExpression.compile(environment)

        if leftValue.type == typeExpression.BOOL:
            newValue = Value("", False, typeExpression.BOOL)

            if self.trueLabel == "":
                self.trueLabel = self.generator.newLabel()

            if self.falseLabel == "":
                self.falseLabel = self.generator.newLabel()

            self.generator.addIf(leftValue.value, leftValue.value, "!", self.trueLabel)
            self.generator.addGoto(self.falseLabel)

            newValue.trueLabel = self.trueLabel
            newValue.falseLabel = self.falseLabel
            return newValue
        else:
            print("Error en not")
            return Value("0", False, typeExpression.INTEGER)
