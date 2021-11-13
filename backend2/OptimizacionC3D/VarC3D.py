from AbstractC3D.InstruccionC3D import Instruccion
from Enum.typeInstructionC3D import typeInstruction


class VarC3D(Instruccion):

    def __init__(self, ids, line: str) -> None:
        super().__init__()
        self.ids = ids
        self.line = line

    def getType(self) -> typeInstruction:
        return typeInstruction.VAR

    def writeC3D(self) -> str:
        if self.write:
            if type(self.ids) == str:
                return "var " + self.ids + " [30101999]float64;"
            else:
                return "var " + ",".join(self.ids) + " float64;"
        return ""
