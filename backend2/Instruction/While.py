from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class While(Instruction):

    def __init__(self, condition: Expression, block) -> None:
        self.condition = condition
        self.block = block

    def compile(self, environment: Environment) -> Value:
        self.condition.generator = self.generator

        newLabel = self.generator.newLabel()
        self.generator.addLabel(newLabel)

        valueCondition = self.condition.compile(environment)
        if valueCondition.trueLabel == "":
            valueCondition.trueLabel = self.generator.newLabel()
        if valueCondition.falseLabel == "":
            valueCondition.falseLabel = self.generator.newLabel()

        if valueCondition.type == typeExpression.BOOL:
            self.generator.addIf(str(valueCondition.value), "1", "==", valueCondition.trueLabel)
            self.generator.addGoto(valueCondition.falseLabel)
            self.generator.addLabel(valueCondition.trueLabel)

            newEnv = Environment(environment)
            for ins in self.block:
                ins.generator = self.generator
                ins.compile(newEnv)

            self.generator.addGoto(newLabel)
            self.generator.addLabel(valueCondition.falseLabel)
        else:
            print("ERROR EN WHILE")
