from AbstractC3D.InstruccionC3D import Instruccion
from AbstractC3D.ExpressionC3D import Expression
from Enum.typeInstructionC3D import typeInstruction


class LabelC3D(Instruccion):

    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value

    def getType(self) -> typeInstruction:
        return typeInstruction.LABEL

    def writeC3D(self) -> str:
        if self.write:
            return self.value + ":"
        return ""
