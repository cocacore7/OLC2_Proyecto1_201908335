from abc import ABC, abstractclassmethod
from Environment.Environment import Environment

salida = ""


class Instruction(ABC):

    @abstractclassmethod
    def execute(cls, environment: Environment):
        pass
