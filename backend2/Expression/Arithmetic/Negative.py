from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class Negative(Expression):

    def __init__(self, left: Expression) -> None:
        super().__init__()
        self.leftExpression = left

    def compile(self, environment: Environment) -> Value:

        self.leftExpression.generator = self.generator

        leftValue: Value = self.leftExpression.compile(environment)

        newTemp = self.generator.newTemp()

        if leftValue.type == typeExpression.INTEGER or leftValue.type == typeExpression.FLOAT:
            TempRigth = self.generator.newTemp()
            self.generator.addExpression(TempRigth, "-1", "", "")
            self.generator.addExpression(newTemp, leftValue.getValue(), TempRigth, "*")
            return Value(newTemp, True, leftValue.type)
        else:
            print("Error en negativo")
            return Value("0", False, typeExpression.INTEGER)
