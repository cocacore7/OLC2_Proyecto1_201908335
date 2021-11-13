from AbstractC3D.InstruccionC3D import Instruccion
from Enum.typeInstructionC3D import typeInstruction


class FunctionC3D(Instruccion):

    def __init__(self, func: str, line: str) -> None:
        super().__init__()
        self.func = func
        self.line = line

    def getType(self) -> typeInstruction:
        return typeInstruction.FUNCTION

    def writeC3D(self) -> str:
        if self.write:
            return "func " + self.func + " (){"
        return ""
