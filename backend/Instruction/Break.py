from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Enum.TransferSentence import TransferSentence


class Break(Instruction):

    def __init__(self, type: TransferSentence) -> None:
        self.type = type

    def execute(self, environment: Environment):
        return self
