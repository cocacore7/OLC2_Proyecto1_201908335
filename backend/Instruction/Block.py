from Environment.Environment import Environment
from Abstract.Instruction import Instruction


class Block(Instruction):

    def __init__(self, block) -> None:
        self.block = block

    def execute(self, environment: Environment):

        for ins in self.block:
            ins.execute(environment)
