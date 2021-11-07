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
            return Value(str(ord(self.value)), False, self.type)

        elif self.type == typeExpression.BOOL:
            tmp = Value(str(self.value), False, self.type)
            falseLabel = self.generator.newLabel()
            trueLabel = self.generator.newLabel()

            self.generator.addIf(str(tmp.value), "1", "==", trueLabel)
            self.generator.addGoto(falseLabel)

            self.generator.addLabel(trueLabel)
            tmp2 = self.generator.newTemp()
            self.generator.addExpression(tmp2, "1", "", "")
            newLabel = self.generator.newLabel()
            self.generator.addGoto(newLabel)
            self.generator.addLabel(falseLabel)
            self.generator.addExpression(tmp2, "0", "", "")
            self.generator.addLabel(newLabel)

            tmp.value = tmp2
            return tmp

        elif self.type == typeExpression.STRING:
            tmp = self.generator.newTemp()
            self.generator.addActHeap(tmp)

            for x in self.value:
                self.generator.addSetHeap("H", str(ord(x)))
                self.generator.addNextHeap()
            self.generator.addSetHeap("H", str(-1))
            self.generator.addNextHeap()
            return Value(tmp, False, self.type)

        elif self.type == typeExpression.NULO:
            return Value(str(self.value), False, self.type)

        print("No se reconoce el tipo")
        return Value("0", False, typeExpression.INTEGER)
