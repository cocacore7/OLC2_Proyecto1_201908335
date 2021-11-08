from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Generator.Generator import Generator


class Function(Instruction):

    def __init__(self, id: str, parameters, type: typeExpression, block) -> None:
        self.id = id
        self.parameters = parameters
        self.block = block
        self.type = type

    def compile(self, environment: Environment) -> Value:
        generator: Generator = Generator()
        generator.addFunction(self.id)
        generator.temporal = self.generator.temporal
        generator.label = self.generator.label
        generator.tempList = self.generator.tempList
        newEnv = Environment(environment)
        newEnv.size = newEnv.size + 1
        newEnv.localSize = newEnv.localSize + 1
        for ins in self.block:
            ins.generator = generator
            ins.compile(newEnv)
        generator.addCloseFunction()

        self.generator.temporal = generator.temporal
        self.generator.label = generator.label
        self.generator.tempList = generator.tempList
        self.generator.functions.append(generator.code)

