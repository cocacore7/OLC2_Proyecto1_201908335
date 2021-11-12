from abc import ABC, abstractclassmethod
from Enum.typeInstructionC3D import typeInstruction


class Instruccion(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.typeInstruction: typeInstruction = None
        self.write = True

    @abstractclassmethod
    def getType(self) -> typeInstruction:
        pass

    @abstractclassmethod
    def writeC3D(self) -> str:
        pass