from AbstractC3D.InstruccionC3D import Instruccion
from AbstractC3D.ExpressionC3D import Expression
from Enum.typeInstructionC3D import typeInstruction


class IfC3D(Instruccion):

    def __init__(self, exp: Expression, goto: Instruccion, line: str) -> None:
        super().__init__()
        self.exp = exp
        self.goto = goto
        self.line = line

    def getType(self) -> typeInstruction:
        return typeInstruction.IF

    def writeC3D(self) -> str:
        if self.write:
            return "if " + self.exp.writeC3D() + " { " + self.goto.writeC3D() + " }"
        return ""
