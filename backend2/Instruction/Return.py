from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.TransferSentence import TransferSentence


class Return(Instruction):

    def __init__(self, type: TransferSentence, exp: Expression) -> None:
        super().__init__()
        self.type = type
        self.exp = exp

    def compile(self, environment: Environment) -> Value:
        tmp = self.generator.newTemp()
        self.exp.generator = self.generator
        value = self.exp.compile(environment)
        self.generator.addExpression(tmp, value.getValue(), "", "")
        self.generator.addSetStack(str(environment.size-environment.localSize), tmp)
        return value
