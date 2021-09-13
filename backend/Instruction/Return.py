from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Enum.TransferSentence import TransferSentence
import copy


class Return(Instruction):

    def __init__(self, type: TransferSentence, exp: Expression) -> None:
        self.type = type
        self.exp = exp
        self.ciclo = False
        self.funcion = False

    def execute(self, environment: Environment):
        temp = copy.copy(self)
        temp.exp = temp.exp.execute(environment)
        return temp
