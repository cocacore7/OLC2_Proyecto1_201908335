from AbstractC3D.InstruccionC3D import Instruccion
from AbstractC3D.ExpressionC3D import Expression
from Enum.typeInstructionC3D import typeInstruction


class StackGC3D(Instruccion):

    def __init__(self, target: str, value: Expression, line: str) -> None:
        super().__init__()
        self.target = target
        self.value = value
        self.line = line

    def getType(self) -> typeInstruction:
        return typeInstruction.STACKG

    def writeC3D(self) -> str:
        if self.write:
            return self.target + " = stack[int( " + self.value.writeC3D() + ")];"
        return ""
