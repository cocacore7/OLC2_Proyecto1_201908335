from AbstractC3D.InstruccionC3D import Instruccion
from Enum.typeInstructionC3D import typeInstruction


class FuncCallC3D(Instruccion):

    def __init__(self, id: str, line: str) -> None:
        super().__init__()
        self.id = id
        self.line = line

    def getType(self) -> typeInstruction:
        return typeInstruction.FUNCCALL

    def writeC3D(self) -> str:
        if self.write:
            return self.id + " ();"
        return ""
