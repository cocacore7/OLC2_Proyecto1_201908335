from AbstractC3D.InstruccionC3D import Instruccion
from Enum.typeInstructionC3D import typeInstruction


class GotoC3D(Instruccion):

    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value

    def getType(self) -> typeInstruction:
        return typeInstruction.GOTO

    def writeC3D(self) -> str:
        if self.write:
            return "goto " + self.value + ";"
        return ""
