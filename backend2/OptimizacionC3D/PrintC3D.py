from AbstractC3D.InstruccionC3D import Instruccion
from AbstractC3D.ExpressionC3D import Expression
from Enum.typeInstructionC3D import typeInstruction


class PrintC3D(Instruccion):

    def __init__(self, tipo: str, value: Expression, line: str, isint) -> None:
        super().__init__()
        self.tipo = tipo
        self.value = value
        self.line = line
        self.isint = isint

    def getType(self) -> typeInstruction:
        return typeInstruction.PRINT

    def writeC3D(self) -> str:
        if self.write:
            if self.isint:
                return "fmt.println(" + self.tipo + " , int(" + self.value.writeC3D() + " ) );"
            else:
                return "fmt.println(" + self.tipo + " , " + self.value.writeC3D() + " );"
        return ""
