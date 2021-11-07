from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.TransferSentence import TransferSentence


class Continue(Instruction):

    def __init__(self, type: TransferSentence) -> None:
        super().__init__()
        self.type = type
        self.labelTrue = ""

    def compile(self, environment: Environment) -> Value:
        self.generator.addGoto(self.labelTrue)
