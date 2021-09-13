from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Enum.TransferSentence import TransferSentence


class Block(Instruction):

    def __init__(self, block) -> None:
        self.block = block

    def execute(self, environment: Environment):

        for ins in self.block:
            temp = ins.execute(environment)
            if temp is not None:
                if temp.type == TransferSentence.RETURN:
                    return temp
                elif temp.type == TransferSentence.BREAK:
                    return temp
                elif temp.type == TransferSentence.CONTINUE:
                    return temp
