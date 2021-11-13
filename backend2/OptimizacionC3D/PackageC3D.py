from AbstractC3D.InstruccionC3D import Instruccion
from Enum.typeInstructionC3D import typeInstruction


class PackageC3D(Instruccion):

    def __init__(self, line: str) -> None:
        super().__init__()
        self.line = line

    def getType(self) -> typeInstruction:
        return typeInstruction.PACKAGE

    def writeC3D(self) -> str:
        if self.write:
            return "package main;"
        return ""
