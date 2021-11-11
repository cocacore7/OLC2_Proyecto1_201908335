from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Enum.TransferSentence import TransferSentence


class Block(Instruction):

    def __init__(self, block) -> None:
        super().__init__()
        self.block = block

    def compile(self, environment: Environment):

        for ins in self.block:
            ins.generator = self.generator
            temp = ins.compile(environment)
            if temp is not None:
                if temp.type == TransferSentence.RETURN:
                    return temp
                elif temp.type == TransferSentence.BREAK:
                    return temp
                elif temp.type == TransferSentence.CONTINUE:
                    return temp
