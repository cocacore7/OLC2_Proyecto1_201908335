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
        self.funtioncReturn = ""
        self.espacioReturn = 0
        self.tmpSalir = ""

    def compile(self, environment: Environment) -> Value:
        self.exp.generator = self.generator
        value = self.exp.compile(environment)
        self.generator.addExpression(self.funtioncReturn, value.getValue(), "", "")
        self.generator.addSetStack(str(self.espacioReturn), self.funtioncReturn)
        if self.tmpSalir != "":
            self.generator.addGoto(self.tmpSalir)
        return value
