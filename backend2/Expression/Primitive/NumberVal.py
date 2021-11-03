from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class NumberVal(Expression):

    def __init__(self, type: typeExpression, value) -> None:
        super().__init__()
        self.type = type
        self.value = value

    def compile(self, environment: Environment) -> Value:
        if self.type == typeExpression.INTEGER or self.type == typeExpression.FLOAT:
            return Value(str(self.value), False, self.type)

        elif self.type == typeExpression.CHAR:
            return Value(self.value, False, self.type)

        elif self.type == typeExpression.BOOL:
            tmp = Value(str(self.value), False, self.type)
            if tmp.trueLabel == "":
                tmp.trueLabel = self.generator.newLabel()

            if tmp.falseLabel == "":
                tmp.falseLabel = self.generator.newLabel()

            self.generator.addIf(str(tmp.value), "1", "==", tmp.trueLabel)
            self.generator.addGoto(tmp.falseLabel)

            self.generator.addLabel(tmp.trueLabel)
            tmp2 = self.generator.newTemp()
            self.generator.addExpression(tmp2, "1", "", "")
            newLabel = self.generator.newLabel()
            self.generator.addGoto(newLabel)
            self.generator.addLabel(tmp.falseLabel)
            self.generator.addExpression(tmp2, "0", "", "")
            self.generator.addLabel(newLabel)

            tmp.value = tmp2
            return tmp

        elif self.type == typeExpression.STRING:
            return Value(self.value, False, self.type)

        elif self.type == typeExpression.NULO:
            return Value(str(self.value), False, self.type)

        print("No se reconoce el tipo")
        return Value("0", False, typeExpression.INTEGER)
