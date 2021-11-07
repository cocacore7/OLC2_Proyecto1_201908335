from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.TransferSentence import TransferSentence


class Break(Instruction):

    def __init__(self, type: TransferSentence) -> None:
        super().__init__()
        self.type = type
        self.labelFalse = ""

    def compile(self, environment: Environment) -> Value:
        self.generator.addGoto(self.labelFalse)
