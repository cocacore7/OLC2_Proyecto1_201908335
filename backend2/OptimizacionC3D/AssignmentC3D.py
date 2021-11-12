from AbstractC3D.InstruccionC3D import Instruccion
from AbstractC3D.ExpressionC3D import Expression
from Enum.typeInstructionC3D import typeInstruction


class AssignmentC3D(Instruccion):

    def __init__(self, target: str, value: Expression, line: str) -> None:
        super().__init__()
        self.target = target
        self.value = value
        self.line = line

    def getType(self) -> typeInstruction:
        return typeInstruction.ASSIGNMENT

    def writeC3D(self) -> str:
        if self.write:
            return self.target + " = " + self.value.writeC3D() + ";"
        return ""
