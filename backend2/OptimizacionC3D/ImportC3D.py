from AbstractC3D.InstruccionC3D import Instruccion
from Enum.typeInstructionC3D import typeInstruction


class ImportC3D(Instruccion):

    def __init__(self, value: str, line: str) -> None:
        super().__init__()
        self.value = value
        self.line = line

    def getType(self) -> typeInstruction:
        return typeInstruction.IMPORT

    def writeC3D(self) -> str:
        if self.write:
            return "import ( " + self.value + " );"
        return ""
