from AbstractC3D.InstruccionC3D import Instruccion
from Enum.typeInstructionC3D import typeInstruction


class LabelC3D(Instruccion):

    def __init__(self, value: str, line: str) -> None:
        super().__init__()
        self.value = value
        self.line = line

    def getType(self) -> typeInstruction:
        return typeInstruction.LABEL

    def writeC3D(self) -> str:
        if self.write:
            return self.value + ":"
        return ""
