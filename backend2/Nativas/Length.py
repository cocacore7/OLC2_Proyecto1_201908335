from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class Length(Instruction):

    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def compile(self, environment: Environment) -> Value:
        self.value.generator = self.generator
        value = self.value.compile(environment)
        tmp = self.generator.newTemp()
        tmp1 = self.generator.newTemp()
        tmp2 = self.generator.newTemp()
        trueLabel = self.generator.newLabel()
        falseLabel = self.generator.newLabel()
        Label1 = self.generator.newLabel()
        if value.type == typeExpression.STRING:
            self.generator.addExpression(tmp, value.getValue(), "", "")
            self.generator.addExpression(tmp1, "0", "", "")
            self.generator.addLabel(trueLabel)
            self.generator.addExpression(tmp2, "heap[int(" + tmp + ")]", "", "")
            self.generator.addIf(tmp2, "-1", "==", falseLabel)
            self.generator.addGoto(Label1)
            self.generator.addLabel(Label1)
            self.generator.addExpression(tmp, tmp, "1", "+")
            self.generator.addExpression(tmp1, tmp1, "1", "+")
            self.generator.addGoto(trueLabel)
            self.generator.addLabel(falseLabel)
            return Value(tmp1, True, typeExpression.INTEGER)
